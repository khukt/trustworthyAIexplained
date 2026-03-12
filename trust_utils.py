from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Any, Optional, Sequence
import numpy as np
import pandas as pd
import streamlit as st


PAGE_ICONS = {
    "home": ":material/robot_2:",
    "what_is": ":material/verified_user:",
    "why": ":material/warning:",
    "risk": ":material/policy:",
    "demo": ":material/tune:",
    "stories": ":material/auto_stories:",
    "roadmap": ":material/route:",
}


NAV_ITEMS = [
    ("home", "app.py", "Home"),
    ("what_is", "pages/1_What_is_Trustworthy_AI.py", "1) What is Trustworthy AI?"),
    ("why", "pages/2_Why_should_we_care.py", "2) Why it matters"),
    ("risk", "pages/3_EU_AI_Act_Risk_Categories.py", "3) EU AI Act risk categories"),
    ("demo", "pages/3_Interactive_mini_demo.py", "4) Interactive mini-demo"),
    ("stories", "pages/4_Failure_stories.py", "5) Failure stories"),
    ("roadmap", "pages/5_Roadmap.py", "6) Roadmap"),
]


def inject_icon_font() -> None:
    """Load Material Symbols for consistent icon rendering in custom HTML."""
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,400,0,0');

        .material-symbols-rounded {
            font-family: 'Material Symbols Rounded';
            font-weight: normal;
            font-style: normal;
            line-height: 1;
            letter-spacing: normal;
            text-transform: none;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            white-space: nowrap;
            word-wrap: normal;
            direction: ltr;
            -webkit-font-feature-settings: 'liga';
            -webkit-font-smoothing: antialiased;
            font-variation-settings: 'FILL' 0, 'wght' 500, 'GRAD' 0, 'opsz' 24;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def material_icon(name: str, size: int = 24, color: str = "currentColor") -> str:
    """Return a Material Symbols icon span for use in custom HTML blocks."""
    return (
        f"<span class='material-symbols-rounded' "
        f"style='font-size:{size}px; color:{color};' aria-hidden='true'>{name}</span>"
    )


def _join_chips(chips: Sequence[str]) -> str:
    return "".join(f"<span class='chip'>{chip}</span>" for chip in chips)


def render_sidebar(active_page: str) -> None:
    """Render the shared story-first sidebar navigation."""
    current_label = next((label for key, _, label in NAV_ITEMS if key == active_page), "Current page")
    with st.sidebar:
        st.markdown(
            f"<div class='sidebar-panel'>"
            f"<div class='sidebar-title'>{material_icon('explore', 20, '#1d4ed8')} Start here</div>"
            f"<div class='sidebar-copy'>A short, decision-maker friendly walkthrough from definition to action.</div>"
            f"</div>",
            unsafe_allow_html=True,
        )
        for key, path, label in NAV_ITEMS:
            st.page_link(path, label=label, icon=PAGE_ICONS[key])

        st.divider()
        st.markdown(
            f"<div class='sidebar-note'>"
            f"<strong>{material_icon('flag', 16, '#0f172a')} Current focus:</strong><br>{current_label}"
            f"</div>",
            unsafe_allow_html=True,
        )
        st.page_link(
            "pages/3_Interactive_mini_demo.py",
            label="Open the live mini-demo",
            icon=":material/play_circle:",
        )


def inject_global_styles() -> None:
    """Inject the shared visual design system used across pages."""
    st.markdown(
        """
        <style>
        :root {
            --bg: #f8fbff;
            --surface: rgba(255, 255, 255, 0.92);
            --surface-strong: #ffffff;
            --border: #dbe5f1;
            --text: #0f172a;
            --muted: #475569;
            --accent: #2563eb;
            --shadow: 0 20px 50px rgba(15, 23, 42, 0.08);
        }
        .stApp {
            background:
                radial-gradient(circle at top left, rgba(37, 99, 235, 0.08), transparent 30%),
                linear-gradient(180deg, #f8fbff 0%, #ffffff 38%, #f8fafc 100%);
        }
        [data-testid="stAppViewContainer"] {
            background: transparent;
        }
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #f8fbff 0%, #f8fafc 100%);
            border-right: 1px solid var(--border);
        }
        .block-container {
            padding-top: 1.5rem;
            padding-bottom: 3.5rem;
            max-width: 1180px;
        }
        [data-testid="metric-container"] {
            background: rgba(255, 255, 255, 0.95);
            border: 1px solid var(--border);
            border-radius: 18px;
            padding: 14px;
            box-shadow: 0 8px 24px rgba(15, 23, 42, 0.05);
        }
        h1, h2, h3 {
            color: var(--text) !important;
            letter-spacing: -0.02em;
        }
        p, li, div {
            color: #111827;
        }
        details summary {
            font-size: 1.02rem;
            font-weight: 600;
        }
        .stAlert {
            border-radius: 16px;
        }
        hr {
            border-color: #e2e8f0;
            margin: 1.15rem 0;
        }
        .hero-panel {
            background: linear-gradient(180deg, rgba(255,255,255,0.95), rgba(248,250,252,0.98));
            border: 1px solid var(--border);
            border-radius: 24px;
            padding: 24px 26px;
            box-shadow: var(--shadow);
            margin-bottom: 0.35rem;
        }
        .hero-row {
            display: flex;
            align-items: flex-start;
            gap: 14px;
        }
        .hero-icon {
            width: 52px;
            height: 52px;
            border-radius: 16px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background: rgba(37, 99, 235, 0.10);
            flex-shrink: 0;
        }
        .muted {
            color: var(--muted);
            font-size: 1rem;
            line-height: 1.6;
        }
        .hero-panel h1 {
            line-height: 1.08;
            margin-bottom: 0.35rem !important;
        }
        .hero-panel .muted {
            max-width: 60rem;
        }
        .hero-kicker {
            color: var(--muted);
            text-transform: uppercase;
            letter-spacing: 0.08em;
            font-size: 0.78rem;
            font-weight: 700;
            margin-bottom: 6px;
        }
        .chip {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 11px;
            border-radius: 999px;
            background: #eff6ff;
            border: 1px solid #bfdbfe;
            color: #1d4ed8;
            font-size: 0.92rem;
            margin: 8px 8px 0 0;
        }
        .callout {
            border-left: 4px solid var(--accent);
            background: #eff6ff;
            padding: 14px 16px;
            border-radius: 14px;
            color: var(--text);
            margin: 14px 0 2px;
            box-shadow: 0 8px 22px rgba(37, 99, 235, 0.08);
        }
        .section-intro {
            margin: 0.25rem 0 0.85rem;
        }
        .section-intro h2 {
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 4px;
        }
        .card {
            border: 1px solid var(--border);
            border-radius: 18px;
            padding: 16px 18px;
            background: rgba(255,255,255,0.95);
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.04);
            height: 100%;
        }
        .card-title {
            font-weight: 750;
            color: var(--text);
            margin-bottom: 6px;
        }
        .card-desc {
            color: var(--muted);
            line-height: 1.6;
        }
        .card p:last-child,
        .card ul:last-child {
            margin-bottom: 0;
        }
        .card ul {
            padding-left: 1.1rem;
        }
        .card li + li {
            margin-top: 0.28rem;
        }
        .sidebar-panel, .sidebar-note {
            background: rgba(255,255,255,0.9);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 14px 14px;
            margin-bottom: 12px;
        }
        .sidebar-title {
            display: flex;
            align-items: center;
            gap: 8px;
            font-weight: 750;
            color: var(--text);
            margin-bottom: 4px;
        }
        .sidebar-copy {
            color: var(--muted);
            font-size: 0.95rem;
            line-height: 1.5;
        }
        .sidebar-note {
            color: var(--muted);
            font-size: 0.92rem;
            line-height: 1.5;
        }
        .surface-strip {
            border: 1px solid var(--border);
            background: rgba(255,255,255,0.92);
            border-radius: 18px;
            padding: 14px 18px;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.04);
        }
        [data-testid="stMain"] [data-testid="stPageLink"] {
            margin-top: -0.55rem;
            margin-bottom: 0.95rem;
        }
        [data-testid="stMain"] [data-testid="stPageLink"] a {
            display: flex;
            align-items: center;
            justify-content: space-between;
            width: 100%;
            min-height: 2.6rem;
            padding: 0.72rem 0.95rem;
            border: 1px solid var(--border);
            border-top: none;
            border-radius: 0 0 16px 16px;
            background: linear-gradient(180deg, #eff6ff 0%, #f8fbff 100%);
            color: #1d4ed8;
            font-weight: 600;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.04);
        }
        [data-testid="stMain"] [data-testid="stPageLink"] a:hover {
            border-color: #bfdbfe;
            background: linear-gradient(180deg, #dbeafe 0%, #eff6ff 100%);
            color: #1d4ed8;
        }
        [data-testid="stSidebar"] [data-testid="stPageLink"] {
            margin-top: 0;
            margin-bottom: 0.35rem;
        }
        [data-testid="stSidebar"] [data-testid="stPageLink"] a {
            border-radius: 12px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def setup_page(page_key: str, page_title: str, layout: str = "wide") -> None:
    """Configure a page and apply the shared chrome."""
    st.set_page_config(page_title=page_title, page_icon=PAGE_ICONS[page_key], layout=layout)
    inject_icon_font()
    inject_global_styles()
    render_sidebar(page_key)


def render_page_header(
    title: str,
    subtitle: str,
    icon_name: str,
    accent: str = "#2563eb",
    chips: Optional[Sequence[str]] = None,
    eyebrow: Optional[str] = None,
) -> None:
    """Render the shared page hero section."""
    chips_html = _join_chips(chips or [])
    eyebrow_html = f"<div class='hero-kicker'>{eyebrow}</div>" if eyebrow else ""
    st.markdown(
        f"""
        <div class='hero-panel' style='--accent:{accent};'>
          <div class='hero-row'>
            <div class='hero-icon' style='background:{accent}12;'>
              {material_icon(icon_name, 30, accent)}
            </div>
            <div>
              {eyebrow_html}
              <h1 style='margin:0;'>{title}</h1>
              <div class='muted'>{subtitle}</div>
            </div>
          </div>
          {f"<div style='margin-top:10px;'>{chips_html}</div>" if chips_html else ""}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_callout(title: str, body: str, icon_name: str = "info", accent: str = "#2563eb") -> None:
    """Render a consistent callout panel."""
    st.markdown(
        f"""
        <div class='callout' style='--accent:{accent};'>
          <strong>{material_icon(icon_name, 18, accent)} {title}</strong><br>
          <span>{body}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_section_intro(title: str, body: str, icon_name: Optional[str] = None, accent: str = "#2563eb") -> None:
    """Render a section heading with optional icon and short explanation."""
    title_html = (
        f"<h2>{material_icon(icon_name, 20, accent)}<span>{title}</span></h2>"
        if icon_name
        else f"<h2>{title}</h2>"
    )
    st.markdown(
        f"<div class='section-intro'>{title_html}<div class='muted'>{body}</div></div>",
        unsafe_allow_html=True,
    )


def apply_dark_theme() -> None:
    """Inject the global CSS used across all pages."""
    inject_icon_font()
    inject_global_styles()


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
