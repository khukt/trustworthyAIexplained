import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

st.title("2\ufe0f\u20e3 Why should we care?")
st.markdown(
    "<p style='color:#94a3b8; font-size:1.05rem;'>For decision makers, the question is simple: "
    "<strong>If AI is wrong, who pays the price?</strong></p>",
    unsafe_allow_html=True,
)

st.divider()

# ── Three risk cards ──────────────────────────────────────────────────────────
c1, c2, c3 = st.columns(3)
risk_cards = [
    (c1, "\U0001f9cd", "Public safety risk", "#ef4444",
     "Wrong AI recommendation \u2192 wrong action \u2192 harm, legal consequences."),
    (c2, "\U0001f4b6", "Economic / operational risk", "#f59e0b",
     "Unreliable AI \u2192 downtime, wasted resources, wrong forecasts or allocations."),
    (c3, "\U0001f5f3\ufe0f", "Trust & legitimacy risk", "#3b82f6",
     "Unfair or unexplained decisions \u2192 distrust, backlash, reputation damage."),
]
for col, icon, title, color, desc in risk_cards:
    with col:
        st.markdown(
            f"""
            <div style='background:#1e293b; border:1px solid {color};
                        border-top:4px solid {color}; border-radius:12px;
                        padding:22px 16px; text-align:center; min-height:160px;'>
              <div style='font-size:2.4rem;'>{icon}</div>
              <div style='color:{color}; font-weight:700; font-size:1rem;
                          margin:8px 0 6px;'>{title}</div>
              <div style='color:#94a3b8; font-size:0.88rem;'>{desc}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.divider()

# ── Comparison chart ──────────────────────────────────────────────────────────
left, right = st.columns([1, 1], gap="large")

with left:
    st.markdown("### Without vs With Trustworthy AI")
    compare = pd.DataFrame({
        "Category": ["Uncertain decisions", "Accountability", "Bias detection", "Early failure detection"],
        "Without safeguards": [95, 15, 10, 20],
        "With safeguards": [25, 90, 85, 88],
    })
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name="Without safeguards",
        x=compare["Category"],
        y=compare["Without safeguards"],
        marker_color="#ef4444",
        text=compare["Without safeguards"],
        texttemplate="%{text}%",
        textposition="outside",
    ))
    fig.add_trace(go.Bar(
        name="With safeguards",
        x=compare["Category"],
        y=compare["With safeguards"],
        marker_color="#22c55e",
        text=compare["With safeguards"],
        texttemplate="%{text}%",
        textposition="outside",
    ))
    fig.update_layout(
        barmode="group",
        paper_bgcolor="#1e293b",
        plot_bgcolor="#1e293b",
        font=dict(color="#cbd5e1"),
        legend=dict(font=dict(color="#cbd5e1"), bgcolor="#1e293b"),
        yaxis=dict(range=[0, 120], showgrid=False, title=""),
        xaxis=dict(showgrid=False, title=""),
        margin=dict(l=10, r=10, t=10, b=10),
    )
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.markdown("### Key safeguards comparison")
    rows_without = [
        "AI used even when uncertain",
        "No clear accountability",
        "Bias remains hidden",
        "Failures discovered too late",
    ]
    rows_with = [
        "Confidence thresholds + human review",
        "Defined ownership + audit trail",
        "Fairness checks + documentation",
        "Monitoring + incident response",
    ]
    for wo, wi in zip(rows_without, rows_with):
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown(
                f"<div style='background:#2d1515; border:1px solid #ef4444; "
                f"border-radius:8px; padding:8px 12px; color:#fca5a5; "
                f"font-size:0.85rem; margin:4px 0;'>\u274c {wo}</div>",
                unsafe_allow_html=True,
            )
        with col_b:
            st.markdown(
                f"<div style='background:#14291e; border:1px solid #22c55e; "
                f"border-radius:8px; padding:8px 12px; color:#86efac; "
                f"font-size:0.85rem; margin:4px 0;'>\u2705 {wi}</div>",
                unsafe_allow_html=True,
            )

st.divider()

# ── Mindset quote ────────────────────────────────────────────────────────────
st.markdown(
    """
    <div style='background:#1e3a5f; border-left:4px solid #2563eb;
                border-radius:8px; padding:20px 24px; margin:12px 0;'>
      <h3 style='color:#93c5fd; margin-top:0;'>A useful mindset</h3>
      <p style='color:#cbd5e1; margin:4px 0;'>We don\u2019t need <em>perfect</em> AI. We need AI that:</p>
      <ul style='color:#cbd5e1; margin:8px 0;'>
        <li><strong style='color:#22c55e;'>fails safely</strong></li>
        <li><strong style='color:#3b82f6;'>is reviewable</strong></li>
        <li><strong style='color:#f59e0b;'>is governed</strong></li>
        <li><strong style='color:#a855f7;'>earns public trust</strong></li>
      </ul>
    </div>
    """,
    unsafe_allow_html=True,
)
