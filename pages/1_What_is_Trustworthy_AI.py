import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from trust_utils import apply_dark_theme



st.title("1️⃣ What is Trustworthy AI?")

# -----------------------------------------------------------------------------
# 1) Definition (academic + EU-aligned)
# -----------------------------------------------------------------------------
st.markdown(
    """
    <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(148,163,184,0.25);
                border-radius:12px; padding:14px 16px;">
      <div style="color:#e5e7eb; font-size:1.05rem; line-height:1.6;">
        <strong>Trustworthy AI</strong> refers to AI systems that are developed, deployed, and governed
        in a way that is <strong>lawful</strong>, <strong>ethical</strong>, and <strong>technically robust</strong>,
        so they can be used responsibly in real-world contexts under appropriate oversight.
      </div>
      <div style="margin-top:10px; color:#cbd5e1;">
        Different organizations structure “trustworthiness” differently, but the core concerns strongly overlap.
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

tabs = st.tabs(
    [
        "Core dimensions",
        "EU: 7 requirements",
        "Compare frameworks",
        "References",
    ]
)

# -----------------------------------------------------------------------------
# TAB A — Core dimensions (neutral synthesis; low cognitive load)
# -----------------------------------------------------------------------------
with tabs[0]:
    st.subheader("Common dimensions across major frameworks")
    st.markdown(
        """
        Across policy (EU/OECD), engineering (NIST), standards (ISO/IEC), and sector frameworks,
        several **recurring dimensions** appear repeatedly:
        """
    )

    dims = [
        ("Technical robustness & reliability", "Consistent performance; resilience to errors and changing conditions."),
        ("Safety & risk mitigation", "Failures do not cause harm; uncertain cases are controlled and reviewed."),
        ("Fairness & non-discrimination", "Avoids unjustified disparities across individuals or groups."),
        ("Transparency & explainability", "Practical explanations and traceability for outcomes and processes."),
        ("Accountability & governance", "Clear responsibility, oversight, auditability, and decision ownership."),
        ("Privacy & data governance", "Appropriate data handling, protection, and lifecycle governance."),
        ("Societal & environmental impact", "Broader effects on society, institutions, and environment."),
    ]

    # Compact “dimension cards” (clean, readable)
    for title, desc in dims:
        st.markdown(
            f"""
            <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(148,163,184,0.20);
                        border-radius:10px; padding:10px 12px; margin:8px 0;">
              <div style="color:#e5e7eb; font-weight:700;">{title}</div>
              <div style="color:#cbd5e1; margin-top:2px;">{desc}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### A simple mental model")
    st.markdown(
        """
        Trustworthy AI is often understood as the intersection of:
        **(1) technical quality**, **(2) human oversight**, and **(3) governance** — with
        **rights, privacy, and societal impact** explicitly considered in policy frameworks.
        """
    )

    # Minimal, clear visual: triangle (not “busy”)
    tri = go.Figure()
    tri.add_trace(
        go.Scatter(
            x=[0, 1, 2, 0],
            y=[0, 0, 0, 0],
            mode="lines",
            line=dict(width=0),
            showlegend=False,
        )
    )
    tri.add_shape(type="path", path="M 0 0 L 2 0 L 1 1.8 Z",
                  line=dict(color="rgba(148,163,184,0.55)", width=2),
                  fillcolor="rgba(37,99,235,0.08)")
    tri.add_annotation(x=1, y=1.05, text="Trustworthy AI", showarrow=False,
                       font=dict(size=16, color="#e5e7eb"))
    tri.add_annotation(x=0, y=-0.15, text="Technical quality", showarrow=False,
                       font=dict(color="#cbd5e1"))
    tri.add_annotation(x=2, y=-0.15, text="Governance & accountability", showarrow=False,
                       font=dict(color="#cbd5e1"))
    tri.add_annotation(x=1, y=1.95, text="Human oversight", showarrow=False,
                       font=dict(color="#cbd5e1"))
    tri.update_layout(
        height=280,
        margin=dict(l=10, r=10, t=10, b=10),
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )
    st.plotly_chart(tri, use_container_width=True)

# -----------------------------------------------------------------------------
# TAB B — EU: 7 requirements (policy-aligned; exactly 7 rows)
# -----------------------------------------------------------------------------
with tabs[1]:
    st.subheader("EU Ethics Guidelines for Trustworthy AI: 7 key requirements (2019)")

    eu7 = [
        ("1) Human agency & oversight",
         "AI should support human decision-making; appropriate oversight mechanisms should exist."),
        ("2) Technical robustness & safety",
         "Systems should be resilient, reliable, secure, and safe across expected and unexpected conditions."),
        ("3) Privacy & data governance",
         "Data should be handled responsibly (quality, integrity, access control, privacy protection)."),
        ("4) Transparency",
         "Appropriate traceability and explainability; people should know when they interact with AI where relevant."),
        ("5) Diversity, non-discrimination & fairness",
         "Avoid unfair bias; ensure accessibility and equal treatment."),
        ("6) Societal & environmental well-being",
         "Consider impacts on society, institutions, democracy, and environmental sustainability."),
        ("7) Accountability",
         "Clear responsibility, auditability, governance, and mechanisms for redress."),
    ]

    # 7-row table (clean) + short descriptions
    df_eu = pd.DataFrame(eu7, columns=["EU requirement", "What it means (plain language)"])
    st.dataframe(df_eu, use_container_width=True, hide_index=True)

    st.caption(
        "This is the EU structure (7 requirements). Other frameworks may group these topics differently."
    )

# -----------------------------------------------------------------------------
# TAB C — Compare frameworks (visual, but honest: overlap + differences)
# -----------------------------------------------------------------------------
with tabs[2]:
    st.subheader("How frameworks overlap (and why counts differ)")

    st.markdown(
        """
        Frameworks differ because they emphasize different layers:
        policy (rights & societal impact), engineering (measurable system properties),
        and standards (auditable management systems).
        """
    )

    # Heatmap: “coverage strength” (0 = not emphasized, 0.5 = indirect/partial, 1 = explicit/strong)
    # NOTE: This is a communication aid, not a compliance claim.
    dimensions = [
        "Technical robustness & reliability",
        "Safety & risk mitigation",
        "Fairness & non-discrimination",
        "Transparency & explainability",
        "Accountability & governance",
        "Privacy & data governance",
        "Societal & environmental impact",
    ]
    frameworks = [
        "EU (HLEG 2019)",
        "OECD (2019+)",
        "NIST AI RMF",
        "ISO/IEC (42001/23894)",
        "Ericsson (industry)",
        "US VA (gov)",
        "UCSF (health)",
    ]

    # Carefully chosen, non-1:1, non-identical values to reflect grouping differences.
    # - EU explicitly includes all 7.
    # - OECD emphasizes principles; societal/wellbeing is present via inclusive growth/wellbeing.
    # - NIST emphasizes engineering properties; societal/environment not a primary “characteristic”.
    # - ISO focuses on management system & risk mgmt; privacy often via other standards/family.
    # - Ericsson emphasizes privacy, robustness/safety, transparency; societal/env appears.
    # - VA explicitly includes purposeful + monitored; strong on governance/accountability.
    # - UCSF highlights fairness/robustness/privacy/safety/accountability/transparency.
    M = pd.DataFrame(
        [
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],  # EU
            [0.8, 1.0, 1.0, 1.0, 1.0, 0.8, 0.8],  # OECD
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.3],  # NIST
            [0.8, 1.0, 0.5, 0.7, 1.0, 0.5, 0.4],  # ISO/IEC
            [0.8, 1.0, 0.4, 0.8, 0.4, 1.0, 0.7],  # Ericsson
            [0.7, 1.0, 1.0, 1.0, 1.0, 1.0, 0.6],  # VA
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.4],  # UCSF
        ],
        index=frameworks,
        columns=dimensions,
    )

    fig = px.imshow(
        M,
        color_continuous_scale="Blues",
        zmin=0,
        zmax=1,
        labels=dict(x="Dimension", y="Framework", color="Coverage"),
        title="Overlap across frameworks (0 = indirect, 1 = explicit)",
    )
    fig.update_layout(
        height=420,
        margin=dict(l=10, r=10, t=50, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#e5e7eb"),
        coloraxis_colorbar=dict(tickcolor="#cbd5e1"),
    )
    st.plotly_chart(fig, use_container_width=True)

    st.caption(
        "This heatmap is an interpretive summary to explain why different pillar counts exist. "
        "It is not a certification/compliance statement."
    )

# -----------------------------------------------------------------------------
# TAB D — References (official + the three examples you showed)
# -----------------------------------------------------------------------------
with tabs[3]:
    st.subheader("References (official and commonly cited sources)")

    st.markdown(
        """
**Policy / principles**
- EU High-Level Expert Group on AI — *Ethics Guidelines for Trustworthy AI* (2019):  
  https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai

- OECD — *OECD AI Principles*:  
  https://www.oecd.org/en/topics/ai-principles.html

**Risk management / engineering**
- NIST — AI Risk Management Framework resources (trustworthy characteristics):  
  https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/

**Standards**
- ISO/IEC 42001 — AI management system (AIMS):  
  https://www.iso.org/standard/81230.html

**Examples of differing “pillar sets” (as in your slide)**
- Ericsson — Trustworthy AI (white paper / overview):  
  https://www.ericsson.com/en/reports-and-papers/white-papers/trustworthy-ai

- U.S. Department of Veterans Affairs — Trustworthy AI:  
  https://department.va.gov/ai/trustworthy-ai/

- UCSF — Trustworthy AI:  
  https://ai.ucsf.edu/trustworthy
        """
    )

    st.caption(
        "Tip for presentations: keep the definition + EU 7 requirements on this page; "
        "use the mini-demo to show concrete examples of risk, bias, transparency, and governance."
    )
