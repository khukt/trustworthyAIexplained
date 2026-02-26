import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from trust_utils import apply_dark_theme

# Keep your global CSS injector (it is already light background)
apply_dark_theme()

# Local readability upgrades (Style B)
st.markdown(
    """
    <style>
      .stApp { background:#ffffff; }
      h1, h2, h3 { color:#0f172a !important; }
      p, li { color:#111827; font-size:1.03rem; line-height:1.55; }
      .muted { color:#475569; font-size:1.02rem; }
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
              background:#f1f5f9; border:1px solid #e2e8f0; color:#0f172a; font-size:0.92rem; margin-right:8px; }
      hr { border:none; height:1px; background:#e5e7eb; margin:18px 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
      <h1 style="margin:0;">2️⃣ Why it matters</h1>
      <p class="muted" style="margin:8px 0 0 0;">
        For decision makers, the question is simple:
        <strong>If AI is wrong, who pays the price?</strong>
      </p>
      <div style="margin-top:12px;" class="callout">
        Trustworthy AI is not “nice to have”.
        It reduces <strong>harm</strong>, protects <strong>public trust</strong>, and manages <strong>legal + financial risk</strong>.
      </div>
      <div style="margin-top:10px;">
        <span class="pill">Safety</span>
        <span class="pill">Legitimacy</span>
        <span class="pill">Legal & financial risk</span>
        <span class="pill">Operational resilience</span>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<hr>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 1) Consequences (human + institutional) — clean and short
# -----------------------------------------------------------------------------
st.markdown("## What can go wrong (in plain terms)")
c1, c2, c3 = st.columns(3, gap="large")

with c1:
    st.markdown(
        """
        <div class="card">
          <div class="card-title">🧯 Public safety & harm</div>
          <div class="card-desc">
            Wrong recommendations can lead to wrong actions — and real harm.
            In high-impact settings, uncertainty must trigger safeguards and review.
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
            Unreliable systems create waste: bad prioritization, rework, delays, and
            costly failures discovered late.
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
            Unfair or unexplained decisions reduce public trust, trigger backlash,
            and harm institutional credibility.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<hr>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2) EU AI Act — fines + interactive calculator (no fake %)
# -----------------------------------------------------------------------------
st.markdown("## Legal & financial risk (EU AI Act)")
st.markdown(
    """
    <p class="muted">
      The EU AI Act introduces enforceable obligations. Non-compliance can lead to substantial administrative fines.
      Use the calculator below to translate the fine rules into a concrete number for decision makers.
    </p>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns([1.0, 1.1], gap="large")

with left:
    st.markdown(
        """
        <div class="card">
          <div class="card-title">Fine categories (summary)</div>
          <div class="card-desc">
            This demo uses a simplified, decision-maker-friendly summary of maximum fines:
            <ul>
              <li><strong>Prohibited AI practices</strong> → up to €35M or 7% of global annual turnover (whichever is higher)</li>
              <li><strong>High-risk requirements violations</strong> → up to €15M or 3%</li>
              <li><strong>Incorrect / misleading information to authorities</strong> → up to €7.5M or 1%</li>
            </ul>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.caption(
        "Reference (official text): https://eur-lex.europa.eu/eli/reg/2024/1689/oj"
    )

with right:
    st.markdown("### Interactive fine calculator")
    st.write("Enter an estimated **global annual turnover** (EUR). The chart shows the maximum fine per category.")

    turnover_m = st.number_input(
        "Global annual turnover (€ millions)",
        min_value=0.0,
        value=500.0,
        step=50.0,
        help="Use a rough value for communication. The AI Act uses 'whichever is higher' (fixed cap vs % of turnover).",
    )

    turnover = turnover_m * 1_000_000

    rules = [
        {"Category": "Prohibited practices", "FixedCap": 35_000_000, "Pct": 0.07},
        {"Category": "High-risk requirements violations", "FixedCap": 15_000_000, "Pct": 0.03},
        {"Category": "Misleading info to authorities", "FixedCap": 7_500_000, "Pct": 0.01},
    ]

    rows = []
    for r in rules:
        pct_val = turnover * r["Pct"]
        max_fine = max(r["FixedCap"], pct_val)
        rows.append(
            {
                "Category": r["Category"],
                "Fixed cap (€M)": r["FixedCap"] / 1_000_000,
                "% of turnover (€M)": pct_val / 1_000_000,
                "Maximum (€M)": max_fine / 1_000_000,
                "Rule": f"max({r['FixedCap']/1e6:.1f}M, {int(r['Pct']*100)}% of turnover)",
            }
        )

    df = pd.DataFrame(rows)

    # Clean bar chart (no “fake” data; derived from input + rule)
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            name="Fixed cap",
            x=df["Category"],
            y=df["Fixed cap (€M)"],
            text=df["Fixed cap (€M)"].map(lambda v: f"€{v:.1f}M"),
            textposition="outside",
        )
    )
    fig.add_trace(
        go.Bar(
            name="% of turnover",
            x=df["Category"],
            y=df["% of turnover (€M)"],
            text=df["% of turnover (€M)"].map(lambda v: f"€{v:.1f}M"),
            textposition="outside",
        )
    )
    fig.add_trace(
        go.Scatter(
            name="Maximum (whichever higher)",
            x=df["Category"],
            y=df["Maximum (€M)"],
            mode="markers+text",
            text=df["Maximum (€M)"].map(lambda v: f"Max €{v:.1f}M"),
            textposition="top center",
            marker=dict(size=12, symbol="diamond"),
        )
    )
    fig.update_layout(
        barmode="group",
        height=380,
        margin=dict(l=10, r=10, t=30, b=10),
        title="EU AI Act: maximum fine depends on turnover",
        yaxis=dict(title="€ Millions", showgrid=True, gridcolor="#eef2f7"),
        xaxis=dict(title="", showgrid=False),
        paper_bgcolor="#ffffff",
        plot_bgcolor="#ffffff",
        font=dict(color="#0f172a"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0.0),
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### At a glance")
    m1, m2, m3 = st.columns(3)
    m1.metric("Prohibited practices (max)", f"€{df.loc[0,'Maximum (€M)']:.1f}M")
    m2.metric("High-risk violations (max)", f"€{df.loc[1,'Maximum (€M)']:.1f}M")
    m3.metric("Misleading info (max)", f"€{df.loc[2,'Maximum (€M)']:.1f}M")

st.markdown("<hr>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3) Management takeaway — short checklist
# -----------------------------------------------------------------------------
st.markdown("## What leaders should require (minimum)")
st.markdown(
    """
    <div class="card">
      <div class="card-title">Decision-ready checklist</div>
      <div class="card-desc">
        <ul>
          <li><strong>Define scope</strong>: what the AI is for (and not for)</li>
          <li><strong>Human oversight</strong> for high-impact decisions</li>
          <li><strong>Documentation & traceability</strong>: data, model, decisions, changes</li>
          <li><strong>Monitoring</strong>: detect drift, failures, and unexpected behavior</li>
          <li><strong>Accountability</strong>: named owner, audit trail, incident response</li>
        </ul>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("Next: the mini-demo shows how safeguards change outcomes in a concrete scenario.")
