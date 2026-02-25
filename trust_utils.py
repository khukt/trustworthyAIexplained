from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Any, Tuple
import numpy as np
import pandas as pd


@dataclass
class Safeguards:
    data_quality_checks: bool = True
    bias_check: bool = True
    confidence_threshold: bool = True
    human_review_low_conf: bool = True


def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-x))


def simulate_model_outputs(df: pd.DataFrame, seed: int = 7) -> pd.DataFrame:
    """
    Simulate a simple prediction + confidence based on case features.
    This is intentionally lightweight and demo-friendly (no heavy ML).
    """
    rng = np.random.default_rng(seed)

    # Linear score influenced by need, missingness, OOD, data age
    x = (
        2.4 * df["need_score"].to_numpy()
        - 1.3 * df["missing_rate"].to_numpy()
        - 1.0 * df["ood_score"].to_numpy()
        - 0.004 * df["data_age_days"].to_numpy()
        + rng.normal(0, 0.25, size=len(df))
    )
    prob = sigmoid(x)

    # Simulated confidence: lower when OOD/missingness high
    conf = np.clip(
        0.92 - 0.55 * df["ood_score"].to_numpy() - 0.85 * df["missing_rate"].to_numpy() + rng.normal(0, 0.03, size=len(df)),
        0.05,
        0.99
    )

    out = df.copy()
    out["pred_prob"] = np.round(prob, 3)
    out["pred_label"] = (prob >= 0.5).astype(int)
    out["confidence"] = np.round(conf, 3)
    return out


def compute_bias_gap(df: pd.DataFrame) -> float:
    """
    A simple fairness proxy: difference in positive prediction rate
    between the two groups.
    """
    rates = df.groupby("sensitive_group")["pred_label"].mean()
    if len(rates) < 2:
        return 0.0
    # max-min gap (0..1)
    return float((rates.max() - rates.min()))


def risk_flags_for_case(row: pd.Series, s: Safeguards) -> Dict[str, Any]:
    """
    Create human-friendly "risk reasons" and a combined risk level.
    """
    reasons = []
    risk_points = 0

    # Data quality
    if s.data_quality_checks:
        if row["missing_rate"] > 0.10:
            reasons.append("Data quality issue: too much missing information.")
            risk_points += 2
        if row["data_age_days"] > 60:
            reasons.append("Data is old; the situation may have changed.")
            risk_points += 1
    else:
        # Without checks, risk is implicitly higher
        reasons.append("No data quality checks enabled.")
        risk_points += 2

    # OOD
    if row["ood_score"] > 0.45:
        reasons.append("Case looks unusual compared to training examples (out-of-context).")
        risk_points += 2

    # Confidence threshold
    if s.confidence_threshold:
        if row["confidence"] < 0.65:
            reasons.append("Low confidence prediction.")
            risk_points += 2
    else:
        reasons.append("No confidence threshold — AI decisions may be used even when uncertain.")
        risk_points += 1

    # Human review
    needs_review = False
    if s.human_review_low_conf and row["confidence"] < 0.65:
        needs_review = True
        reasons.append("Human review required for low-confidence cases.")
        # review reduces operational risk
        risk_points = max(0, risk_points - 1)

    # Convert points to traffic-light risk
    if risk_points >= 5:
        level = "RED"
    elif risk_points >= 3:
        level = "YELLOW"
    else:
        level = "GREEN"

    return {
        "risk_level": level,
        "risk_points": int(risk_points),
        "needs_review": bool(needs_review),
        "reasons": reasons if reasons else ["No major risk flags triggered."]
    }


def overall_risk_summary(df: pd.DataFrame, s: Safeguards) -> Dict[str, Any]:
    """
    Provide a simple, management-friendly snapshot.
    """
    # aggregate low confidence
    low_conf_rate = float((df["confidence"] < 0.65).mean())

    # bias gap (only if check enabled)
    bias_gap = compute_bias_gap(df) if s.bias_check else None

    # Quality incidents (only if enabled)
    quality_incident_rate = None
    if s.data_quality_checks:
        quality_incident_rate = float(((df["missing_rate"] > 0.10) | (df["data_age_days"] > 60)).mean())

    # Compose a simple overall "risk index"
    risk_index = 0.0
    risk_index += 0.55 * low_conf_rate
    risk_index += 0.25 * float((df["ood_score"] > 0.45).mean())
    if s.data_quality_checks and quality_incident_rate is not None:
        risk_index += 0.20 * quality_incident_rate
    else:
        risk_index += 0.20 * 0.50  # assume higher baseline if no checks

    if s.bias_check and bias_gap is not None:
        risk_index += 0.35 * bias_gap
    else:
        risk_index += 0.12  # unmeasured fairness risk

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
        "quality_incident_rate": None if quality_incident_rate is None else round(quality_incident_rate, 3),
        "bias_gap": None if bias_gap is None else round(float(bias_gap), 3),
    }
