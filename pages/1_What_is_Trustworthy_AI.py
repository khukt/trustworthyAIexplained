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
      <strong>Trustworthy AI</strong> is AI that people can <strong>depend on</strong> in real-world decisions.
      It is designed to be <strong>reliable</strong>, <strong>safe</strong>, <strong>fair</strong>,
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

# ── Simple interactive lens (low cognitive load) ──────────────────────────────
view = st.radio(
    "Choose how you want to learn this:",
    ["Simple view (5 pillars)", "Framework view (EU • OECD • NIST • ISO)"],
    horizontal=True,
)

# ── Five pillars cards (always central) ───────────────────────────────────────
items = [
    ("✅", "Reliable", "#22c55e", "Gives consistent results in similar situations."),
    ("🧯", "Safe", "#ef4444", "Does not automate risky decisions; failures avoid harm."),
    ("⚖️", "Fair", "#f59e0b", "Does not disadvantage groups."),
    ("🔎", "Transparent", "#3b82f6", "Provides understandable reasons for outcomes."),
    ("🧾", "Accountable", "#a855f7", "Clear ownership, logging, and audit trail."),
]

st.markdown("### Our simple model: 5 pillars (easy to follow)")
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
                height: 155px;
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

st.caption(
    "Why 5 pillars? Because they are easier to communicate and generalize across sectors, "
    "while still matching the core themes used by major frameworks."
)

st.divider()

# ── Framework view (only if user asks) ────────────────────────────────────────
if view == "Framework view (EU • OECD • NIST • ISO)":
    st.markdown("### Why do different organizations use different pillar sets?")
    st.markdown(
        """
They focus on different layers:

- **Policy frameworks** emphasize human rights and societal impacts (e.g., EU, OECD).  
- **Engineering risk frameworks** emphasize measurable system properties (e.g., NIST).  
- **Standards (ISO/IEC)** emphasize auditable management systems and risk processes.

Despite different structures and wording, they converge on the same core ideas.
        """
    )

    with st.expander("Show a simple mapping from our 5 pillars to major frameworks", expanded=True):
        mapping = pd.DataFrame(
            [
                [
                    "Reliable",
                    "Technical robustness & safety",
                    "Robustness, security & safety",
                    "Valid & reliable",
                    "Quality / management controls supporting reliability",
                ],
                [
                    "Safe",
                    "Technical robustness & safety + Human oversight",
                    "Robustness, security & safety",
                    "Safe, secure & resilient",
                    "Risk management processes supporting safety",
                ],
                [
                    "Fair",
                    "Diversity, non-discrimination & fairness",
                    "Human rights & democratic values",
                    "Fair (harmful bias managed)",
                    "Bias-related risk controls (and related guidance)",
                ],
                [
                    "Transparent",
                    "Transparency",
                    "Transparency & explainability",
                    "Explainable/interpretable + transparent",
                    "Documentation + governance supporting transparency",
                ],
                [
                    "Accountable",
                    "Accountability",
                    "Accountability",
                    "Accountable (governance)",
                    "AI management system and governance practices",
                ],
            ],
            columns=[
                "Our 5 pillars (simple)",
                "EU (Ethics Guidelines)",
                "OECD (AI Principles)",
                "NIST (AI RMF)",
                "ISO/IEC (standards support)",
            ],
        )
        st.dataframe(mapping, use_container_width=True, hide_index=True)

    st.markdown("### References (official sources)")
    st.markdown(
        """
- EU High-Level Expert Group on AI — *Ethics Guidelines for Trustworthy AI* (2019):  
  https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai

- OECD — *OECD AI Principles*:  
  https://www.oecd.org/en/topics/ai-principles.html

- NIST — *AI RMF resources* (trustworthy characteristics):  
  https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/

- ISO/IEC — *ISO/IEC 42001* (AI management system) overview page:  
  https://www.iso.org/standard/81230.html
        """
    )
else:
    # In simple view, keep it minimal and avoid extra info.
    with st.expander("Want to see how other organizations define Trustworthy AI?", expanded=False):
        st.markdown(
            """
Different organizations use different “pillar sets”, but they converge on the same ideas.
Open **Framework view** above to see a simple mapping to EU / OECD / NIST / ISO.
            """
        )

st.caption("Tip: Use the Interactive mini-demo page to show concrete examples of each pillar in action.")
