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
st.markdown(
    '<p class="muted">A practical narrative: risks lead to consequences; safeguards reduce exposure.</p>',
    unsafe_allow_html=True,
)

left, right = st.columns([1.2, 0.8], gap="large")

with left:
    labels = [
        "Uncertainty / low confidence",
        "Hidden bias",
        "Opaque decisions",
        "Harm / safety incidents",
        "Loss of trust",
        "Legal & audit findings",
        "Safeguards:\nHuman oversight",
        "Safeguards:\nMonitoring & logging",
        "Safeguards:\nFairness checks",
        "Safeguards:\nDocumentation & governance",
    ]
    # Links: risk nodes → consequence nodes; safeguards also → consequences (reducing narrative)
    source = [0, 1, 2, 0, 1, 2, 6, 7, 8, 9]
    target = [3, 4, 5, 5, 5, 4, 3, 5, 4, 5]
    value  = [4, 3, 3, 2, 2, 2, 2, 2, 2, 2]

    sankey = go.Figure(
        data=[
            go.Sankey(
                node=dict(
                    pad=18,
                    thickness=18,
                    line=dict(color="#e5e7eb", width=1),
                    label=labels,
                ),
                link=dict(source=source, target=target, value=value),
            )
        ]
    )
    sankey.update_layout(
        height=360,
        margin=dict(l=10, r=10, t=10, b=10),
        paper_bgcolor="#ffffff",
        font=dict(color="#0f172a"),
    )
    st.plotly_chart(sankey, use_container_width=True)

with right:
    st.markdown(
        """
        <div class="card">
          <div class="card-title">Leadership takeaway</div>
          <div class="card-desc">
            You do not need “perfect AI”. You need AI that is:
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

st.markdown("<hr>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3) EU AI ACT: FINES (Article 99) + calculator
# -----------------------------------------------------------------------------
st.markdown("## Legal & financial risk (EU AI Act)")
st.markdown(
    """
    <p class="muted">
      The EU AI Act formalizes obligations for certain AI uses. Under <strong>Article 99</strong>, authorities can impose
      administrative fines depending on the infringement category.
    </p>
    """,
    unsafe_allow_html=True,
)

colA, colB = st.columns([1.0, 1.2], gap="large")

with colA:
    st.markdown(
        """
        <div class="card">
          <div class="card-title">Article 99 — fine categories (summary)</div>
          <div class="card-desc">
            <ul>
              <li><strong>Prohibited AI practices</strong> → up to €35M or 7% of global annual turnover (whichever is higher)</li>
              <li><strong>High-risk requirements violations</strong> → up to €15M or 3%</li>
              <li><strong>Incorrect or misleading information</strong> → up to €7.5M or 1%</li>
              <li><strong>SMEs & startups</strong> → proportional approach to avoid disproportionate burden</li>
            </ul>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="card" style="margin-top:10px;">
          <div class="card-title">Legal reference</div>
          <div class="card-desc">
            Regulation (EU) 2024/1689 (AI Act) — <strong>Article 99</strong> (Administrative fines):<br>
            • Art. 99(4) Prohibited practices<br>
            • Art. 99(5) High-risk requirements violations<br>
            • Art. 99(6) Misleading information to authorities<br>
            • Art. 99(7) SMEs & startups proportionality<br><br>
            Official text (EUR-Lex): <a href="https://eur-lex.europa.eu/eli/reg/2024/1689/oj" target="_blank">
            https://eur-lex.europa.eu/eli/reg/2024/1689/oj</a>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with colB:
    st.markdown("### Interactive fine calculator (communication tool)")
    st.markdown('<p class="muted">Enter a rough turnover to translate “% of turnover” into an understandable number.</p>',
                unsafe_allow_html=True)

    turnover_m = st.number_input(
        "Global annual turnover (€ millions)",
        min_value=0.0,
        value=500.0,
        step=50.0,
        help="This is a communication aid: maximum fines depend on the higher of a fixed cap or % of turnover.",
    )
    turnover = turnover_m * 1_000_000

    rules = [
        {"Category": "Prohibited AI practices", "Article": "Art. 99(4)", "FixedCap": 35_000_000, "Pct": 0.07},
        {"Category": "High-risk requirements violations", "Article": "Art. 99(5)", "FixedCap": 15_000_000, "Pct": 0.03},
        {"Category": "Misleading info to authorities", "Article": "Art. 99(6)", "FixedCap": 7_500_000, "Pct": 0.01},
    ]

    rows = []
    for r in rules:
        pct_val = turnover * r["Pct"]
        max_fine = max(r["FixedCap"], pct_val)
        rows.append(
            {
                "Category": r["Category"],
                "Article": r["Article"],
                "Fixed cap (€M)": r["FixedCap"] / 1_000_000,
                "% of turnover (€M)": pct_val / 1_000_000,
                "Maximum (€M)": max_fine / 1_000_000,
            }
        )
    df = pd.DataFrame(rows)

    # KPI row (clear)
    k1, k2, k3 = st.columns(3)
    with k1:
        st.markdown(f'<div class="kpi"><div class="label">{df.loc[0,"Article"]}</div>'
                    f'<div class="value">€{df.loc[0,"Maximum (€M)"]:.1f}M</div>'
                    f'<div class="small">{df.loc[0,"Category"]}</div></div>', unsafe_allow_html=True)
    with k2:
        st.markdown(f'<div class="kpi"><div class="label">{df.loc[1,"Article"]}</div>'
                    f'<div class="value">€{df.loc[1,"Maximum (€M)"]:.1f}M</div>'
                    f'<div class="small">{df.loc[1,"Category"]}</div></div>', unsafe_allow_html=True)
    with k3:
        st.markdown(f'<div class="kpi"><div class="label">{df.loc[2,"Article"]}</div>'
                    f'<div class="value">€{df.loc[2,"Maximum (€M)"]:.1f}M</div>'
                    f'<div class="small">{df.loc[2,"Category"]}</div></div>', unsafe_allow_html=True)

    st.markdown("")

    # Chart: fixed vs % vs max
    fig = go.Figure()
    fig.add_trace(go.Bar(name="Fixed cap", x=df["Category"], y=df["Fixed cap (€M)"]))
    fig.add_trace(go.Bar(name="% of turnover", x=df["Category"], y=df["% of turnover (€M)"]))
    fig.add_trace(
        go.Scatter(
            name="Maximum (higher of the two)",
            x=df["Category"],
            y=df["Maximum (€M)"],
            mode="markers+text",
            text=[f"Max €{v:.1f}M" for v in df["Maximum (€M)"]],
            textposition="top center",
            marker=dict(size=11, symbol="diamond"),
        )
    )
    fig.update_layout(
        barmode="group",
        height=380,
        margin=dict(l=10, r=10, t=10, b=10),
        paper_bgcolor="#ffffff",
        plot_bgcolor="#ffffff",
        font=dict(color="#0f172a"),
        yaxis=dict(title="€ Millions", gridcolor="#eef2f7"),
        xaxis=dict(title="", tickangle=0),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0.0),
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

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
