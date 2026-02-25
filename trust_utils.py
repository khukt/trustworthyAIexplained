from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Any, Optional
import numpy as np
import pandas as pd
import streamlit as st


def apply_dark_theme() -> None:
    """Inject the global dark-theme CSS used across all pages."""
    st.markdown(
        """
        <style>
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        }
        [data-testid="stSidebar"] {
            background: #1e293b;
        }
        [data-testid="metric-container"] {
            background: #1e3a5f;
            border: 1px solid #2563eb;
            border-radius: 10px;
            padding: 12px;
        }
        details summary {
            font-size: 1.05rem;
            font-weight: 600;
        }
        h1, h2, h3 { color: #93c5fd !important; }
        .stAlert { border-radius: 10px; }
        hr { border-color: #334155; }
        .pillar-card {
            background: #1e3a5f;
            border: 1px solid #2563eb;
            border-radius: 12px;
            padding: 18px 16px;
            text-align: center;
            height: 100%;
        }
        .pillar-card h3 { color: #93c5fd !important; margin-bottom: 6px; }
        .pillar-card p { color: #cbd5e1; font-size: 0.9rem; margin: 0; }
        </style>
        """,
        unsafe_allow_html=True,
    )


@dataclass
class Safeguards:
    """
    Safeguards are the *policy knobs* that make AI safer for real-world use.
    """
    data_quality_checks: bool = True
    bias_check: bool = True
    confidence_threshold_on: bool = True
    human_review_low_conf: bool = True

    # Policy thresholds (interactive)
    conf_threshold: float = 0.65            # below => low confidence
    missing_threshold: float = 0.10         # above => quality issue
    max_data_age_days: int = 60             # above => stale data
    ood_threshold: float = 0.45             # above => out-of-context


def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-x))


def simulate_model_outputs(df: pd.DataFrame, seed: int = 7) -> pd.DataFrame:
    """
    Simulate a simple prediction + confidence based on case features.
    Intentionally lightweight and transparent for demo purposes.
    """
    rng = np.random.default_rng(seed)

    # Model score influenced by need (positive), data issues (negative), plus noise
    x = (
        2.4 * df["need_score"].to_numpy()
        - 1.3 * df["missing_rate"].to_numpy()
        - 1.0 * df["ood_score"].to_numpy()
        - 0.004 * df["data_age_days"].to_numpy()
        + rng.normal(0, 0.25, size=len(df))
    )
    prob = sigmoid(x)

    # Confidence is lower when the case is out-of-context or has missing values
    conf = np.clip(
        0.92
        - 0.55 * df["ood_score"].to_numpy()
        - 0.85 * df["missing_rate"].to_numpy()
        + rng.normal(0, 0.03, size=len(df)),
        0.05,
        0.99,
    )

    out = df.copy()
    out["pred_prob"] = np.round(prob, 3)
    out["pred_label"] = (prob >= 0.5).astype(int)
    out["confidence"] = np.round(conf, 3)
    return out


def compute_bias_gap(df: pd.DataFrame) -> float:
    """
    Fairness proxy: difference in positive prediction rate between groups.
    """
    rates = df.groupby("sensitive_group")["pred_label"].mean()
    if len(rates) < 2:
        return 0.0
    return float((rates.max() - rates.min()))


def case_risk(row: pd.Series, s: Safeguards) -> Dict[str, Any]:
    """
    Human-friendly risk flags for a single case.
    """
    reasons = []
    points = 0

    # Data quality
    if s.data_quality_checks:
        if row["missing_rate"] > s.missing_threshold:
            reasons.append("Data quality issue: too much missing information.")
            points += 2
        if row["data_age_days"] > s.max_data_age_days:
            reasons.append("Data is old; the situation may have changed.")
            points += 1
    else:
        reasons.append("No data quality checks enabled.")
        points += 2

    # Out-of-context (OOD)
    if row["ood_score"] > s.ood_threshold:
        reasons.append("Case looks unusual compared to training examples (out-of-context).")
        points += 2

    # Confidence threshold
    low_conf = row["confidence"] < s.conf_threshold
    if s.confidence_threshold_on:
        if low_conf:
            reasons.append("Low confidence prediction.")
            points += 2
    else:
        reasons.append("No confidence threshold — AI may be used even when uncertain.")
        points += 1

    # Human review for low confidence
    needs_review = False
    if s.human_review_low_conf and low_conf:
        needs_review = True
        reasons.append("Human review required for low-confidence cases.")
        # review reduces operational risk a bit
        points = max(0, points - 1)

    # Map points to traffic light
    if points >= 5:
        level = "RED"
    elif points >= 3:
        level = "YELLOW"
    else:
        level = "GREEN"

    return {
        "risk_level": level,
        "risk_points": int(points),
        "needs_review": bool(needs_review),
        "low_conf": bool(low_conf),
        "reasons": reasons if reasons else ["No major risk flags triggered."],
    }


def add_risk_columns(df: pd.DataFrame, s: Safeguards) -> pd.DataFrame:
    """
    Vector-friendly risk labels for dashboards.
    """
    out = df.copy()
    # Flags
    out["flag_quality"] = False
    out["flag_stale"] = False
    out["flag_ood"] = out["ood_score"] > s.ood_threshold
    out["flag_low_conf"] = out["confidence"] < s.conf_threshold

    if s.data_quality_checks:
        out["flag_quality"] = out["missing_rate"] > s.missing_threshold
        out["flag_stale"] = out["data_age_days"] > s.max_data_age_days
    else:
        # if checks are off, treat as "unknown/higher baseline"
        out["flag_quality"] = True

    # Risk points
    pts = np.zeros(len(out), dtype=int)
    pts += out["flag_quality"].astype(int) * 2
    pts += out["flag_stale"].astype(int) * 1
    pts += out["flag_ood"].astype(int) * 2

    if s.confidence_threshold_on:
        pts += out["flag_low_conf"].astype(int) * 2
    else:
        pts += 1  # baseline risk if threshold isn't used

    # Human review reduces a point for low-confidence cases (when enabled)
    out["needs_review"] = False
    if s.human_review_low_conf:
        out["needs_review"] = out["flag_low_conf"]
        pts = np.where(out["needs_review"], np.maximum(0, pts - 1), pts)

    out["risk_points"] = pts
    out["risk_level"] = np.where(pts >= 5, "RED", np.where(pts >= 3, "YELLOW", "GREEN"))
    return out


def overall_summary(df: pd.DataFrame, s: Safeguards) -> Dict[str, Any]:
    """
    Management-friendly KPIs.
    """
    low_conf_rate = float((df["confidence"] < s.conf_threshold).mean())
    ood_rate = float((df["ood_score"] > s.ood_threshold).mean())

    quality_incident_rate: Optional[float] = None
    if s.data_quality_checks:
        quality_incident_rate = float(((df["missing_rate"] > s.missing_threshold) | (df["data_age_days"] > s.max_data_age_days)).mean())

    bias_gap: Optional[float] = compute_bias_gap(df) if s.bias_check else None

    # Risk index (0..1) - intentionally simple and explainable
    risk_index = 0.0
    risk_index += 0.45 * low_conf_rate
    risk_index += 0.25 * ood_rate
    if quality_incident_rate is not None:
        risk_index += 0.20 * quality_incident_rate
    else:
        risk_index += 0.20 * 0.50  # assume higher baseline if not measured
    if bias_gap is not None:
        risk_index += 0.35 * bias_gap
    else:
        risk_index += 0.12

    risk_index = float(np.clip(risk_index, 0, 1))
    if risk_index >= 0.62:
        overall = "RED"
    elif risk_index >= 0.38:
        overall = "YELLOW"
    else:
        overall = "GREEN"

    return {
        "overall_risk": overall,
        "risk_index": round(risk_index, 3),
        "low_conf_rate": round(low_conf_rate, 3),
        "ood_rate": round(ood_rate, 3),
        "quality_incident_rate": None if quality_incident_rate is None else round(quality_incident_rate, 3),
        "bias_gap": None if bias_gap is None else round(float(bias_gap), 3),
    }
