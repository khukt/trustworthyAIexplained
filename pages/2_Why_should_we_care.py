import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from trust_utils import material_icon, render_callout, render_page_header, render_section_intro, setup_page


setup_page("why", "Why it matters")

render_page_header(
    title="Why it matters",
    subtitle="When AI is wrong, the cost is not only technical. It can affect people, operations, trust, and legal exposure.",
    icon_name="warning",
    accent="#ea580c",
    chips=["Public harm", "Operational impact", "Trust & legitimacy", "Legal exposure"],
    eyebrow="Why leaders should care",
)

render_callout(
    title="Core message",
    body="In practice, trustworthy AI helps organizations reduce avoidable harm, protect credibility, and stay in control of AI-supported decisions.",
    icon_name="campaign",
    accent="#1d4ed8",
)

st.markdown("<hr>", unsafe_allow_html=True)

render_section_intro(
    title="Why leaders should care now",
    body="The same failure can create multiple kinds of damage at once: harm to people, operational disruption, and loss of trust.",
    icon_name="crisis_alert",
)

impact_a, impact_b, impact_c = st.columns(3, gap="large")
for column, kicker, title, body, accent, icon in [
    (
        impact_a,
        "People",
        "Safety and real-world harm",
        "Wrong recommendations, bad classifications, or poor escalation can lead to harmful outcomes in high-impact contexts.",
        "#dc2626",
        "health_and_safety",
    ),
    (
        impact_b,
        "Operations",
        "Delays, rework, and cost",
        "Unreliable AI creates hidden operational drag: teams correct errors, repeat work, and discover failures too late.",
        "#0f766e",
        "payments",
    ),
    (
        impact_c,
        "Institutions",
        "Trust and legitimacy loss",
        "Unfair or unexplained decisions damage public trust, weaken credibility, and create reputational and political risk.",
        "#1d4ed8",
        "account_balance",
    ),
]:
    with column:
        st.markdown(
            f"""
            <div class="impact-card">
              <div class="impact-card-kicker">{kicker}</div>
              <div class="impact-card-title">{material_icon(icon, 18, accent)} {title}</div>
              <div class="impact-card-copy">{body}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("<hr>", unsafe_allow_html=True)

render_section_intro(
    title="How small failures become leadership problems",
    body="What looks like a technical issue at first often grows into an operational, legal, or institutional issue.",
    icon_name="conversion_path",
)

risk_left, risk_right = st.columns([1.05, 0.95], gap="large")

with risk_left:
    st.markdown(
        """
        <div class="card">
          <div class="card-title">Typical escalation path</div>
          <div class="risk-chain">
            <div class="risk-chain-item">
              <div class="risk-chain-number">1</div>
              <div>
                <div class="risk-chain-title">The AI is used outside its safe limits</div>
                <div class="risk-chain-copy">The model is applied in a context it does not understand well, or with poor data and weak oversight.</div>
              </div>
            </div>
            <div class="risk-chain-item">
              <div class="risk-chain-number">2</div>
              <div>
                <div class="risk-chain-title">Bad outputs shape real decisions</div>
                <div class="risk-chain-copy">People rely on wrong recommendations, miss warning signs, or cannot challenge the decision in time.</div>
              </div>
            </div>
            <div class="risk-chain-item">
              <div class="risk-chain-number">3</div>
              <div>
                <div class="risk-chain-title">The organization absorbs the consequences</div>
                <div class="risk-chain-copy">The result can be harm, complaints, delays, regulatory scrutiny, and long-term loss of trust.</div>
              </div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with risk_right:
    st.markdown(
        """
        <div class="card">
          <div class="card-title">What changes when AI is trustworthy</div>
          <ul>
            <li>Use cases are scoped clearly, including what the system should <strong>not</strong> do.</li>
            <li>Higher-risk decisions receive stronger human oversight and documentation.</li>
            <li>Data quality, monitoring, and escalation paths are part of the design from the start.</li>
            <li>Leaders can explain why the system is being used and who remains accountable.</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<hr>", unsafe_allow_html=True)

render_section_intro(
    title="Legal and financial exposure under the EU AI Act",
    body="Article 99 sets maximum fine levels. These are legal ceilings, not automatic penalties, and they should be read together with the Act's phased application dates: February 2, 2025; August 2, 2025; August 2, 2026; and August 2, 2027.",
    icon_name="gavel",
)

exposure_left, exposure_right = st.columns([1.0, 1.2], gap="large")

with exposure_left:
    st.markdown(
        """
        <div class="card">
          <div class="card-title">How to read Article 99</div>
          <div class="card-desc">
            The EU AI Act defines different maximum fine levels depending on the type of violation.
            For a leadership audience, the practical takeaway is that <strong>certain AI Act failures can become financially material</strong>.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="fine-tier-grid">
          <div class="fine-tier">
            <div class="fine-tier-top">
              <div class="fine-tier-title">Prohibited AI practices</div>
              <div class="fine-tier-value">Up to €35M / 7%</div>
            </div>
            <div class="fine-tier-copy">The highest ceiling applies to violations of Article 5 prohibited practices.</div>
          </div>
          <div class="fine-tier">
            <div class="fine-tier-top">
              <div class="fine-tier-title">High-risk AI obligation failures</div>
              <div class="fine-tier-value">Up to €15M / 3%</div>
            </div>
            <div class="fine-tier-copy">These ceilings apply when high-risk requirements are not met.</div>
          </div>
          <div class="fine-tier">
            <div class="fine-tier-top">
              <div class="fine-tier-title">Incorrect or misleading information</div>
              <div class="fine-tier-value">Up to €7.5M / 1%</div>
            </div>
            <div class="fine-tier-copy">Supplying incomplete or misleading information can trigger a separate ceiling.</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="fine-note">
          Fines must still be effective, proportionate, and dissuasive. Authorities consider context, severity, intent, and mitigating action.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="section-note">
          Timing matters. The AI Act applies in phases: some provisions applied from <strong>February 2, 2025</strong>, additional provisions from <strong>August 2, 2025</strong>,
          the general application date is <strong>August 2, 2026</strong>, and some provisions apply later from <strong>August 2, 2027</strong>.
          This page uses Article 99 to show the <strong>possible ceiling of exposure</strong>, not to suggest that every requirement is already in force in the same way.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.caption(
        "Official text: Regulation (EU) 2024/1689 — Article 99 (EUR-Lex): "
        "https://eur-lex.europa.eu/eli/reg/2024/1689/oj"
    )

with exposure_right:
    st.markdown("### Article 99 exposure calculator")
    st.markdown(
        '<p class="muted">Enter global annual turnover to estimate the legal ceiling under each fine category.</p>',
        unsafe_allow_html=True,
    )

    turnover_m = st.number_input(
        "Annual turnover (€ millions)",
        min_value=0.0,
        value=500.0,
        step=50.0,
    )

    turnover = turnover_m * 1_000_000
    rules = [
        {"Category": "Art. 99(4) – Prohibited practices", "FixedCap": 35_000_000, "Pct": 0.07},
        {"Category": "Art. 99(5) – High-risk violations", "FixedCap": 15_000_000, "Pct": 0.03},
        {"Category": "Art. 99(6) – Misleading information", "FixedCap": 7_500_000, "Pct": 0.01},
    ]

    rows = []
    for rule in rules:
        pct_val = turnover * rule["Pct"]
        max_val = max(rule["FixedCap"], pct_val)
        rows.append(
            {
                "Category": rule["Category"],
                "Fixed cap (€M)": rule["FixedCap"] / 1_000_000,
                "% of turnover (€M)": pct_val / 1_000_000,
                "Maximum exposure (€M)": max_val / 1_000_000,
            }
        )

    df = pd.DataFrame(rows)

    metric_a, metric_b, metric_c = st.columns(3, gap="small")
    metric_columns = [metric_a, metric_b, metric_c]
    for column, (_, row) in zip(metric_columns, df.iterrows()):
        with column:
            st.metric(label=row["Category"], value=f"€{row['Maximum exposure (€M)']:.1f}M")

    fig = go.Figure()
    fig.add_trace(go.Bar(name="Fixed cap", x=df["Category"], y=df["Fixed cap (€M)"], marker_color="#cbd5e1"))
    fig.add_trace(go.Bar(name="% of turnover", x=df["Category"], y=df["% of turnover (€M)"], marker_color="#fdba74"))
    fig.add_trace(
        go.Scatter(
            name="Maximum ceiling",
            x=df["Category"],
            y=df["Maximum exposure (€M)"],
            mode="markers+text",
            marker=dict(color="#ea580c", size=11),
            text=[f"€{v:.1f}M" for v in df["Maximum exposure (€M)"]],
            textposition="top center",
        )
    )
    fig.update_layout(
        barmode="group",
        height=380,
        paper_bgcolor="rgba(255,255,255,0)",
        plot_bgcolor="rgba(255,255,255,0)",
        font=dict(color="#0f172a"),
        yaxis=dict(title="€ Millions", gridcolor="#e2e8f0"),
        margin=dict(l=10, r=10, t=20, b=10),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

render_section_intro(
    title="What leaders should require",
    body="The list below is practical governance guidance, not quoted legal text, for leaders before an organization relies on AI in important contexts.",
    icon_name="checklist",
)

leader_steps = [
    ("1", "Define the role of the AI", "Be explicit about what the system is for, where it supports people, and where it should not be used."),
    ("2", "Classify the risk", "The higher the impact on people or rights, the stronger the controls, documentation, and oversight must be."),
    ("3", "Assign accountability", "A named owner, a review process, and an audit trail should exist before deployment."),
    ("4", "Require human oversight", "High-impact decisions should not depend on AI alone when uncertainty or harm is significant."),
    ("5", "Monitor and respond", "Track drift, incidents, failures, complaints, and model updates after launch, not only before it."),
]

steps_html = "".join(
    f"""
    <div class="checklist-item">
      <div class="checklist-number">{number}</div>
      <div>
        <div class="checklist-title">{title}</div>
        <div class="checklist-copy">{copy}</div>
      </div>
    </div>
    """
    for number, title, copy in leader_steps
)

st.markdown(f"<div class='checklist-grid'>{steps_html}</div>", unsafe_allow_html=True)

st.caption("Next: the interactive mini-demo shows how safeguards change outcomes in practice.")
