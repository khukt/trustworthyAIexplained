import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Why it matters", page_icon="⚠️", layout="wide")

# --- Style B: modern, clean, formal, high readability ---
st.markdown(
    """
    <style>
      .stApp { background:#ffffff; }
      h1, h2, h3 { color:#0f172a; }
      p, li, div { color:#111827; font-size:1.02rem; line-height:1.55; }
      .muted { color:#475569; }
      .hero {
        border:1px solid #e5e7eb; border-radius:14px; padding:18px 18px;
        background: linear-gradient(180deg, #ffffff, #f8fafc);
      }
      .callout {
        border-left:4px solid #1d4ed8;
        background:#eff6ff;
        padding:12px 14px; border-radius:10px;
        color:#0f172a;
      }
      .card {
        border:1px solid #e5e7eb; border-radius:12px;
        padding:14px 14px; background:#ffffff;
      }
      .card-title { font-weight:750; color:#0f172a; margin-bottom:6px; }
      .card-desc { color:#475569; }
      .pill { display:inline-block; padding:5px 10px; border-radius:999px;
              background:#f1f5f9; border:1px solid #e2e8f0; color:#0f172a;
              font-size:0.92rem; margin-right:8px; margin-top:6px; }
      .kpi { border:1px solid #e5e7eb; border-radius:12px; padding:12px 14px; background:#ffffff; }
      .kpi .label { color:#475569; font-size:0.92rem; }
      .kpi .value { color:#0f172a; font-size:1.35rem; font-weight:800; margin-top:2px; }
      .small { color:#64748b; font-size:0.95rem; }
      hr { border:none; height:1px; background:#e5e7eb; margin:18px 0; }
      a { color:#1d4ed8; text-decoration:none; }
      a:hover { text-decoration:underline; }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# HERO
# -----------------------------------------------------------------------------
st.markdown(
    """
    <div class="hero">
      <div style="display:flex; align-items:flex-start; gap:10px;">
        <div style="font-size:1.8rem;">⚠️</div>
        <div>
          <h1 style="margin:0;">Why it matters</h1>
          <p class="muted" style="margin:8px 0 0 0;">
            For decision makers, the question is simple:
            <strong>If AI is wrong, who pays the price?</strong>
          </p>
        </div>
      </div>

      <div style="margin-top:12px;" class="callout">
        Trustworthy AI is a <strong>risk and governance</strong> issue — not a technical luxury.
        It protects people, institutions, budgets, and compliance.
      </div>

      <div style="margin-top:10px;">
        <span class="pill">Public harm</span>
        <span class="pill">Trust & legitimacy</span>
        <span class="pill">Legal & financial risk</span>
        <span class="pill">Operational resilience</span>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<hr>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 1) WHAT CAN GO WRONG (3 clean cards)
# -----------------------------------------------------------------------------
st.markdown("## What can go wrong (plain language)")
st.markdown(
    '<p class="muted">These are the failure modes that matter most for leadership — because they create real consequences.</p>',
    unsafe_allow_html=True,
)

c1, c2, c3 = st.columns(3, gap="large")
with c1:
    st.markdown(
        """
        <div class="card">
          <div class="card-title">🧯 Safety & harm</div>
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
          <div class="card-title">💶 Operational & economic loss</div>
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
          <div class="card-title">🏛️ Trust & legitimacy</div>
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
st.markdown("## A simple way to explain it")
st.markdown('<p class="muted">Risks lead to consequences; safeguards reduce exposure.</p>', unsafe_allow_html=True)

left, right = st.columns([1.25, 0.75], gap="large")

with left:
    # Short labels (readable)
    labels = [
        "Uncertainty", "Hidden bias", "Opaque decisions",
        "Harm", "Loss of trust", "Audit findings",
        "Human oversight", "Monitoring & logging", "Fairness checks", "Docs & governance"
    ]

    # Optional: richer hover text
    hover = [
        "Uncertainty / low confidence cases",
        "Hidden bias in data or model behavior",
        "Opaque decisions without practical explanations",
        "Safety incidents / harm",
        "Public distrust / backlash / legitimacy loss",
        "Legal & audit findings / enforcement risk",
        "Safeguard: human review for high-impact or low-confidence cases",
        "Safeguard: monitoring, logging, incident response",
        "Safeguard: bias testing, fairness checks, documentation",
        "Safeguard: policies, roles, approvals, traceability"
    ]

    source = [0, 1, 2, 0, 1, 2, 6, 7, 8, 9]
    target = [3, 4, 5, 5, 5, 4, 3, 5, 4, 5]
    value  = [4, 3, 3, 2, 2, 2, 2, 2, 2, 2]

    # Node colors (high contrast)
    node_colors = [
        "#2563eb", "#f59e0b", "#7c3aed",   # risks
        "#ef4444", "#fb923c", "#0ea5e9",   # consequences
        "#22c55e", "#22c55e", "#22c55e", "#22c55e"  # safeguards
    ]

    # Link colors: color by consequence for clarity
    link_colors = []
    for t in target:
        if t == 3:   # Harm
            link_colors.append("rgba(239,68,68,0.35)")
        elif t == 4: # Loss of trust
            link_colors.append("rgba(251,146,60,0.35)")
        else:        # Audit findings
            link_colors.append("rgba(14,165,233,0.30)")

    fig = go.Figure(
        data=[go.Sankey(
            arrangement="snap",
            node=dict(
                pad=22,
                thickness=22,
                line=dict(color="#cbd5e1", width=1),
                label=labels,
                color=node_colors,
                customdata=hover,
                hovertemplate="%{customdata}<extra></extra>",
            ),
            link=dict(
                source=source,
                target=target,
                value=value,
                color=link_colors,
                hovertemplate="Flow strength: %{value}<extra></extra>",
            ),
        )]
    )

    fig.update_layout(
        height=460,
        margin=dict(l=10, r=10, t=10, b=10),
        paper_bgcolor="#ffffff",
        font=dict(color="#0f172a", size=16),  # bigger font
    )

    st.plotly_chart(fig, use_container_width=True)

with right:
    st.markdown(
        """
        <div class="card">
          <div class="card-title">How to read the diagram</div>
          <div class="card-desc">
            <ul>
              <li><strong>Left</strong>: common AI risks</li>
              <li><strong>Middle/Right</strong>: consequences</li>
              <li><strong>Bottom</strong>: safeguards that reduce exposure</li>
            </ul>
            <div class="small">Tip: hover over nodes to see the full explanation.</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="card" style="margin-top:10px;">
          <div class="card-title">Leadership takeaway</div>
          <div class="card-desc">
            You don’t need “perfect AI”. You need AI that is:
            <ul>
              <li><strong>controlled</strong> when uncertain</li>
              <li><strong>auditable</strong> after decisions</li>
              <li><strong>governed</strong> with clear responsibility</li>
            </ul>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------------------------------------------------------
# 3) EU AI ACT: FINES (Article 99) + calculator
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# EU AI ACT — ADMINISTRATIVE FINES (LEGALLY PRECISE VERSION)
# -----------------------------------------------------------------------------
st.markdown("## Legal & financial exposure under the EU AI Act")

st.markdown(
    """
    <p class="muted">
      Regulation (EU) 2024/1689 (AI Act) introduces administrative fines under <strong>Article 99</strong>.
      The amounts below represent the <strong>maximum legal ceilings</strong>.
      The actual fine is determined by the competent supervisory authority.
    </p>
    """,
    unsafe_allow_html=True,
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
    st.markdown("### Maximum exposure under Article 99 (illustrative)")
    st.markdown(
        '<p class="muted">Enter estimated global annual turnover to visualize the legal ceiling.</p>',
        unsafe_allow_html=True,
    )

    turnover_m = st.number_input(
        "Global annual turnover (€ millions)",
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
st.markdown("## What leaders should require (minimum)")
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
