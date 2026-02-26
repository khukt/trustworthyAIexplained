import streamlit as st
import pandas as pd
from trust_utils import apply_dark_theme

apply_dark_theme()

# -----------------------------
# Page: What is Trustworthy AI?
# -----------------------------
st.title("1️⃣ What is Trustworthy AI?")

st.markdown(
    """
    <p style="color:#cbd5e1; font-size:1.05rem; line-height:1.55; margin-top:0.2rem;">
      <strong>Trustworthy AI</strong> is AI that people can <strong>depend on</strong> in real-world decisions:
      it is <strong>reliable</strong>, <strong>safe</strong>, <strong>fair</strong>,
      <strong>transparent</strong>, and <strong>accountable</strong>.
    </p>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div style="background:rgba(37,99,235,0.10); border:1px solid rgba(37,99,235,0.35);
                border-radius:10px; padding:12px 14px; margin-top:10px; color:#bfdbfe;">
      <strong>Key idea:</strong> Trustworthy AI is <strong>not only accuracy</strong> — it is <strong>risk management</strong>
      for AI-assisted decisions.
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

# ── Five pillars (low cognitive load cards) ───────────────────────────────────
items = [
    ("✅", "Reliable", "#22c55e", "Gives consistent results in similar situations."),
    ("🧯", "Safe", "#ef4444", "Does not automate risky decisions."),
    ("⚖️", "Fair", "#f59e0b", "Does not disadvantage groups."),
    ("🔎", "Transparent", "#3b82f6", "Provides understandable reasons."),
    ("🧾", "Accountable", "#a855f7", "Clear ownership and audit trail."),
]

cols = st.columns(5, gap="small")
for col, (icon, label, color, desc) in zip(cols, items):
    with col:
        st.markdown(
            f"""
            <div style="
                background: rgba(255,255,255,0.03);
                border: 1px solid rgba(148,163,184,0.25);
                border-top: 4px solid {color};
                border-radius: 12px;
                padding: 16px 12px;
                text-align: center;
                height: 150px;
                display: flex;
                flex-direction: column;
                justify-content: center;
            ">
              <div style="font-size:2rem; line-height:1;">{icon}</div>
              <div style="color:{color}; font-weight:800; font-size:1.05rem; margin:8px 0 6px;">
                {label}
              </div>
              <div style="color:#cbd5e1; font-size:0.86rem; line-height:1.35;">
                {desc}
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.divider()

# ── Progressive disclosure: frameworks + ISO ──────────────────────────────────
with st.expander("How do major organizations describe Trustworthy AI? (EU • OECD • NIST • ISO)", expanded=False):
    st.markdown(
        """
**Different organizations group the ideas differently**, but the core themes overlap strongly.

- **EU (Ethics Guidelines for Trustworthy AI)** describes 7 requirements (e.g., human oversight, robustness/safety, privacy,
  transparency, fairness, societal wellbeing, accountability).
- **OECD AI Principles** are policy-focused (human rights, transparency, robustness/safety, accountability, etc.).
- **NIST AI Risk Management Framework** describes “trustworthy characteristics” (valid/reliable, safe/secure/resilient,
  explainable/interpretable, privacy-enhanced, fair, accountable/transparent).
- **ISO/IEC standards** turn trust into **auditable management and risk practices** (e.g., AI management system and AI risk management).
        """
    )

    mapping = pd.DataFrame(
        [
            [
                "Reliable",
                "Technical robustness & safety",
                "Robustness, security & safety",
                "Valid & reliable",
                "Quality / management controls (supports reliability)",
            ],
            [
                "Safe",
                "Technical robustness & safety + Human oversight",
                "Robustness, security & safety",
                "Safe, secure & resilient",
                "Risk management and controls (supports safety)",
            ],
            [
                "Fair",
                "Diversity, non-discrimination & fairness",
                "Human rights & democratic values",
                "Fair (harmful bias managed)",
                "Bias considerations / risk controls (supports fairness)",
            ],
            [
                "Transparent",
                "Transparency",
                "Transparency & explainability",
                "Explainable/interpretable + transparent",
                "Documentation and governance (supports transparency)",
            ],
            [
                "Accountable",
                "Accountability",
                "Accountability",
                "Accountable (governance)",
                "AI management system / governance (supports accountability)",
            ],
        ],
        columns=[
            "Our 5 pillars",
            "EU (7 requirements)",
            "OECD (principles)",
            "NIST (trustworthy characteristics)",
            "ISO (standards support)",
        ],
    )
    st.dataframe(mapping, use_container_width=True, hide_index=True)

    st.caption(
        "This table is a communication aid: frameworks differ in structure, but they converge on these core ideas."
    )

st.divider()

# ── References (with links) ───────────────────────────────────────────────────
st.subheader("References (official sources)")
st.markdown(
    """
- EU High-Level Expert Group on AI — *Ethics Guidelines for Trustworthy AI* (2019):  
  https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai

- OECD — *OECD AI Principles*:  
  https://www.oecd.org/en/topics/ai-principles.html

- NIST — *AI Risk Management Framework (AI RMF) resources* (trustworthy characteristics):  
  https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/

- ISO/IEC — *ISO/IEC 42001* (AI management system) overview page (useful as an entry point):  
  https://www.iso.org/standard/81230.html
"""
)

st.caption("Tip: keep this page simple; use the Interactive mini-demo to show examples and visuals.")
