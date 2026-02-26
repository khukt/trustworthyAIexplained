import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

from trust_utils import apply_dark_theme

apply_dark_theme()

st.title("1️⃣ What is Trustworthy AI?")

st.markdown(
    """
    <p style='color:#cbd5e1; font-size:1.05rem; line-height:1.5;'>
    <strong>Trustworthy AI</strong> is AI that is <strong>reliable</strong>, <strong>safe</strong>,
    <strong>fair</strong>, <strong>transparent</strong>, and <strong>accountable</strong> —
    so people can depend on it in real-world decisions.
    </p>
    """,
    unsafe_allow_html=True,
)

st.divider()

# ── Five pillars as styled cards ───────────────────────────────────────────────
items = [
    ("✅", "Reliable", "#22c55e", "Works consistently and predictably."),
    ("🧯", "Safe", "#ef4444", "Failures do not create harm; risky cases are handled safely."),
    ("⚖️", "Fair", "#f59e0b", "Decisions are not biased or discriminatory."),
    ("🔎", "Transparent", "#3b82f6", "We can explain why a result happened (practically)."),
    ("🧾", "Accountable", "#a855f7", "Responsibilities, auditing, and governance are defined."),
]
cols = st.columns(5)
for col, (icon, label, color, desc) in zip(cols, items):
    with col:
        st.markdown(
            f"""
            <div style='background:rgba(255,255,255,0.03); border:1px solid rgba(148,163,184,0.25);
                        border-top: 4px solid {color}; border-radius:12px;
                        padding:18px 12px; text-align:center; height:160px;
                        display:flex; flex-direction:column; justify-content:center;'>
              <div style='font-size:2rem;'>{icon}</div>
              <div style='color:{color}; font-weight:700; font-size:1.05rem;
                          margin:6px 0 4px;'>{label}</div>
              <div style='color:#cbd5e1; font-size:0.85rem;'>{desc}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.divider()

# ── Why pillars differ across orgs (simple explanation) ───────────────────────
st.markdown(
    """
### Why do different organizations use different “pillars”?
They group the same ideas in different ways:
- **EU** describes *7 requirements* (adds human oversight, privacy/data governance, societal wellbeing).  
- **OECD** uses *5 principles* (policy-focused, human rights + robustness + transparency + accountability).  
- **NIST** lists *trustworthy characteristics* (engineering-focused: valid/reliable, safe, secure, explainable, privacy, fairness, accountability).  
"""
)

# ── Mapping section (interactive + visual) ────────────────────────────────────
with st.expander("Show how our 5 pillars map to major frameworks (EU / OECD / NIST)", expanded=True):
    st.markdown(
        """
**Our 5 pillars are a “compressed” way to communicate the common core**:
they align strongly with EU/OECD/NIST, even if naming and grouping differ.
"""
    )

    mapping = pd.DataFrame(
        [
            ["Reliable", "Technical robustness & safety", "Robustness, security & safety", "Valid & reliable"],
            ["Safe", "Technical robustness & safety + Human oversight", "Robustness, security & safety", "Safe, secure & resilient"],
            ["Fair", "Diversity, non-discrimination & fairness", "Human rights & democratic values", "Fair (harmful bias managed)"],
            ["Transparent", "Transparency", "Transparency & explainability", "Explainable/interpretable + transparent"],
            ["Accountable", "Accountability", "Accountability", "Accountable (governance)"],
        ],
        columns=["Our pillar", "EU (7 requirements)", "OECD (principles)", "NIST (trustworthy characteristics)"],
    )

    st.dataframe(mapping, use_container_width=True, hide_index=True)

    # Heatmap “strength of alignment” (simple + visual)
    heat = pd.DataFrame(
        {
            "Pillar": ["Reliable","Safe","Fair","Transparent","Accountable"],
            "EU":    [5, 5, 5, 5, 5],
            "OECD":  [5, 5, 5, 5, 5],
            "NIST":  [5, 5, 5, 5, 5],
        }
    )

    fig_h = px.imshow(
        heat.set_index("Pillar"),
        text_auto=True,
        aspect="auto",
        title="Alignment overview (simplified): our 5 pillars vs major frameworks",
    )
    fig_h.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#e5e7eb"),
    )
    st.plotly_chart(fig_h, use_container_width=True)

    st.caption(
        "Note: This heatmap is a communication aid. Exact wording differs, but the core themes overlap strongly."
    )

st.divider()

# ── Radar chart (keep yours, but explain it clearly) ──────────────────────────
left, right = st.columns([1.15, 1], gap="large")

with left:
    pillar_labels = ["Reliable", "Safe", "Fair", "Transparent", "Accountable"]
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=[0.90, 0.85, 0.80, 0.88, 0.82, 0.90],
        theta=pillar_labels + [pillar_labels[0]],
        fill="toself",
        name="With safeguards",
    ))
    fig.add_trace(go.Scatterpolar(
        r=[0.45, 0.30, 0.35, 0.40, 0.28, 0.45],
        theta=pillar_labels + [pillar_labels[0]],
        fill="toself",
        name="Without safeguards",
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 1]),
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=30, r=30, t=50, b=30),
        title="Impact of Trustworthy AI practices (illustrative)",
        font=dict(color="#e5e7eb"),
        legend=dict(font=dict(color="#e5e7eb")),
    )
    st.plotly_chart(fig, use_container_width=True)
    st.caption("This radar is illustrative: it shows how safeguards typically increase trustworthiness across pillars.")

with right:
    st.markdown("### What Trustworthy AI is *not*")
    for txt in ["A 'luxury feature'", "Only about accuracy", "About replacing people"]:
        st.markdown(
            f"<div style='background:rgba(255,255,255,0.03); border:1px solid rgba(148,163,184,0.25); "
            f"border-radius:8px; padding:10px 14px; margin:6px 0; color:#fca5a5;'>"
            f"❌ {txt}</div>",
            unsafe_allow_html=True,
        )

    st.markdown("### ✅ What it is")
    st.markdown(
        "<div style='background:rgba(37,99,235,0.12); border:1px solid rgba(37,99,235,0.5); "
        "border-radius:8px; padding:14px 18px; color:#bfdbfe; font-size:1rem;'>"
        "🛡️ <strong>Risk management</strong> for AI-assisted decisions."
        "</div>",
        unsafe_allow_html=True,
    )

st.divider()

# ── References (citations you can show in the demo) ───────────────────────────
st.markdown("### References (official frameworks)")
st.markdown(
    """
- **EU High-Level Expert Group on AI (2019)** — *Ethics Guidelines for Trustworthy AI* (7 requirements: oversight, robustness/safety, privacy, transparency, fairness, societal wellbeing, accountability).  
  https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai

- **NIST AI Risk Management Framework** — *Characteristics of trustworthy AI* (valid/reliable, safe/secure/resilient, accountable/transparent, explainable, privacy-enhanced, fair).  
  https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/

- **OECD AI Principles (adopted 2019; updated 2024)** — Intergovernmental principles for trustworthy AI (human rights, transparency, robustness/safety, accountability, etc.).  
  https://www.oecd.org/en/topics/ai-principles.html
"""
)
