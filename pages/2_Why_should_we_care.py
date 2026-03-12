import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from trust_utils import material_icon, render_callout, render_page_header, render_section_intro, setup_page

setup_page("why", "Why it matters")

render_page_header(
    title="Why it matters",
  subtitle="If AI is wrong, people, budgets, and institutions pay the price.",
    icon_name="warning",
    accent="#ea580c",
    chips=["Public harm", "Trust & legitimacy", "Legal & financial risk", "Operational resilience"],
    eyebrow="Why leaders should care",
)

render_callout(
    title="Core message",
  body="Trustworthy AI is a governance issue, not a technical luxury. It protects people, budgets, and compliance.",
    icon_name="campaign",
    accent="#1d4ed8",
)

st.markdown("<hr>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 1) WHAT CAN GO WRONG (3 clean cards)
# -----------------------------------------------------------------------------
render_section_intro(
  title="What can go wrong",
  body="These are the failure modes leaders should care about most.",
  icon_name="crisis_alert",
)

c1, c2, c3 = st.columns(3, gap="large")
with c1:
    st.markdown(
        """
        <div class="card">
          <div class="card-title">""" + material_icon("health_and_safety", 18, "#dc2626") + """ Safety & harm</div>
          <div class="card-desc">
            Incorrect recommendations can trigger wrong actions and real harm.
            High-impact use cases require safeguards and human oversight.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        """
        <div class="card">
          <div class="card-title">""" + material_icon("payments", 18, "#0f766e") + """ Operational & economic loss</div>
          <div class="card-desc">
            Unreliable AI creates rework, delays, misallocation, and late discovery of failures —
            which increases cost and reduces service quality.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with c3:
    st.markdown(
        """
        <div class="card">
          <div class="card-title">""" + material_icon("account_balance", 18, "#1d4ed8") + """ Trust & legitimacy</div>
          <div class="card-desc">
            Unfair or unexplained decisions reduce public trust and institutional credibility,
            and can escalate into reputational and political risk.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<hr>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2) SIMPLE VISUAL STORY: Risk → Consequence → Control (Sankey)
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# EU AI ACT — ADMINISTRATIVE FINES (LEGALLY PRECISE VERSION)
# -----------------------------------------------------------------------------
render_section_intro(
    title="Legal & financial exposure under the EU AI Act",
  body="Article 99 sets maximum fine levels. The figures below show legal ceilings, not automatic penalties.",
    icon_name="gavel",
)

colA, colB = st.columns([1.0, 1.2], gap="large")

# --- Left: Legal summary (precise wording) ---
with colA:
    st.markdown(
        """
        <div class="card">
          <div class="card-title">Article 99 — Fine categories</div>
          <div class="card-desc">
            <ul>
              <li>
                <strong>Art. 99(4)</strong> – Violations of Article 5 (Prohibited AI Practices):<br>
                Up to <strong>€35 million</strong> or <strong>7% of total worldwide annual turnover</strong>,
                whichever is higher.
              </li>
              <br>
              <li>
                <strong>Art. 99(5)</strong> – Violations of high-risk AI obligations:<br>
                Up to <strong>€15 million</strong> or <strong>3% of total worldwide annual turnover</strong>,
                whichever is higher.
              </li>
              <br>
              <li>
                <strong>Art. 99(6)</strong> – Supplying incorrect, incomplete, or misleading information:<br>
                Up to <strong>€7.5 million</strong> or <strong>1% of total worldwide annual turnover</strong>,
                whichever is higher.
              </li>
              <br>
              <li>
                <strong>Art. 99(7)</strong> – For SMEs and startups:<br>
                Fines must be <strong>effective, proportionate, and dissuasive</strong>,
                taking into account the size and economic capacity of the undertaking.
              </li>
            </ul>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="card" style="margin-top:10px;">
          <div class="card-title">Important legal nuance</div>
          <div class="card-desc">
            Under <strong>Art. 99(2)</strong>, fines must be effective, proportionate,
            and dissuasive. Authorities consider factors such as:
            <ul>
              <li>Nature and gravity of the infringement</li>
              <li>Intentional or negligent character</li>
              <li>Mitigating actions taken</li>
              <li>Size and economic capacity of the undertaking</li>
            </ul>
            The calculator below shows <strong>maximum exposure</strong>, not an automatic penalty.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.caption(
        "Official text: Regulation (EU) 2024/1689 — Article 99 (EUR-Lex): "
        "https://eur-lex.europa.eu/eli/reg/2024/1689/oj"
    )


# --- Right: Exposure calculator (renamed + clarified) ---
with colB:
  st.markdown("### Article 99 exposure calculator")
    st.markdown(
    '<p class="muted">Enter global annual turnover to estimate the legal ceiling.</p>',
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
    for r in rules:
        pct_val = turnover * r["Pct"]
        max_val = max(r["FixedCap"], pct_val)
        rows.append({
            "Category": r["Category"],
            "Fixed cap (€M)": r["FixedCap"] / 1_000_000,
            "% of turnover (€M)": pct_val / 1_000_000,
            "Maximum exposure (€M)": max_val / 1_000_000,
        })

    df = pd.DataFrame(rows)

    # KPI summary
    for i in range(len(df)):
        st.metric(
            label=df.loc[i, "Category"],
            value=f"€{df.loc[i, 'Maximum exposure (€M)']:.1f}M",
        )

    # Visual comparison
    fig = go.Figure()
    fig.add_trace(go.Bar(name="Fixed cap", x=df["Category"], y=df["Fixed cap (€M)"]))
    fig.add_trace(go.Bar(name="% of turnover", x=df["Category"], y=df["% of turnover (€M)"]))
    fig.add_trace(
        go.Scatter(
            name="Maximum (whichever higher)",
            x=df["Category"],
            y=df["Maximum exposure (€M)"],
            mode="markers+text",
            text=[f"€{v:.1f}M" for v in df["Maximum exposure (€M)"]],
            textposition="top center",
        )
    )

    fig.update_layout(
        barmode="group",
        height=380,
        paper_bgcolor="#ffffff",
        plot_bgcolor="#ffffff",
        font=dict(color="#0f172a"),
        yaxis=dict(title="€ Millions"),
    )

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------------------------------
# 4) What leaders should require (short, decision-ready)
# -----------------------------------------------------------------------------
render_section_intro(
  title="What leaders should require",
  body="A minimum checklist for responsible adoption and oversight.",
  icon_name="checklist",
)
st.markdown(
    """
    <div class="card">
      <div class="card-title">Decision-ready checklist</div>
      <div class="card-desc">
        <ol>
          <li><strong>Define scope</strong> — what the AI is for (and not for)</li>
          <li><strong>Classify risk</strong> — higher impact ⇒ stronger controls</li>
          <li><strong>Assign accountability</strong> — named owner and audit trail</li>
          <li><strong>Require human oversight</strong> for high-impact decisions</li>
          <li><strong>Monitor & respond</strong> — drift, failures, incidents, updates</li>
        </ol>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("Next: the interactive mini-demo shows concrete safeguards in action.")
