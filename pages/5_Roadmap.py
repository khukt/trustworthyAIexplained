import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from trust_utils import apply_dark_theme

apply_dark_theme()

st.title("5\ufe0f\u20e3 What we recommend \u2014 a decision-ready roadmap")
st.caption("A simple, non-technical roadmap that leaders can act on.")

# ── Phase cards ───────────────────────────────────────────────────────────────
phases = [
    {
        "phase": "Phase A",
        "name": "Minimum Safety Baseline",
        "subtitle": "Quick wins",
        "color": "#22c55e",
        "bg": "#f0fdf4",
        "icon": "🛡️",
        "effort": 2,
        "impact": 8,
        "items": [
            "Define what the AI is for and what it is not for",
            "Add confidence thresholds (do not auto-act on uncertain outputs)",
            "Add human review for low-confidence / high-impact cases",
            "Basic data quality and data freshness checks",
        ],
    },
    {
        "phase": "Phase B",
        "name": "Robust Governance",
        "subtitle": "Structural safeguards",
        "color": "#3b82f6",
        "bg": "#eff6ff",
        "icon": "🏛️",
        "effort": 5,
        "impact": 9,
        "items": [
            "Monitoring + alerts (detect drift and abnormal behavior)",
            "Logging and audit trails (who/what/when)",
            "Roles and accountability (ownership is clear)",
            "Fairness evaluation, documented and repeated",
        ],
    },
    {
        "phase": "Phase C",
        "name": "Continuous Improvement",
        "subtitle": "Long-term excellence",
        "color": "#a855f7",
        "bg": "#faf5ff",
        "icon": "🔄",
        "effort": 8,
        "impact": 10,
        "items": [
            "Regular re-evaluation and updates",
            "Improve data coverage and reduce bias",
            "Independent review for high-impact uses",
            "Learning from incidents (like safety engineering)",
        ],
    },
]

cols = st.columns(3, gap="large")
for col, p in zip(cols, phases):
    with col:
        items_html = "".join(
            f"<li style='margin:4px 0; color:#334155;'>{it}</li>" for it in p["items"]
        )
        st.markdown(
            f"""
            <div style='background:{p['bg']}; border:1px solid {p['color']};
                        border-top:5px solid {p['color']}; border-radius:12px;
                        padding:20px 16px; min-height:300px;'>
              <div style='font-size:2rem; margin-bottom:6px;'>{p['icon']}</div>
              <div style='color:{p['color']}; font-size:0.8rem; font-weight:600;
                          text-transform:uppercase; letter-spacing:1px;'>{p['phase']}</div>
              <div style='color:#1e293b; font-weight:700; font-size:1.1rem;
                          margin:4px 0 2px;'>{p['name']}</div>
              <div style='color:#64748b; font-size:0.85rem; margin-bottom:12px;'>{p['subtitle']}</div>
              <ul style='padding-left:18px; margin:0;'>{items_html}</ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.divider()

# ── Bubble chart: effort vs impact ────────────────────────────────────────────
left, right = st.columns([1, 1], gap="large")

with left:
    st.markdown("### Effort vs Impact by phase")
    df_bubble = pd.DataFrame({
        "Phase": [p["phase"] + ": " + p["name"] for p in phases],
        "Effort": [p["effort"] for p in phases],
        "Impact": [p["impact"] for p in phases],
        "Size": [30, 40, 50],
        "Color": [p["color"] for p in phases],
    })
    fig = px.scatter(
        df_bubble,
        x="Effort",
        y="Impact",
        size="Size",
        color="Phase",
        color_discrete_map={row["Phase"]: phases[i]["color"] for i, row in df_bubble.iterrows()},
        text="Phase",
    )
    fig.update_traces(textposition="top center")
    fig.update_layout(
        paper_bgcolor="#ffffff",
        plot_bgcolor="#ffffff",
        font=dict(color="#334155"),
        legend=dict(font=dict(color="#334155"), bgcolor="#ffffff"),
        xaxis=dict(title="Implementation effort (1-10)", range=[0, 11], showgrid=False),
        yaxis=dict(title="Expected impact (1-10)", range=[5, 11], showgrid=False),
        margin=dict(l=10, r=10, t=10, b=10),
        showlegend=False,
    )
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.markdown("### Cumulative safeguard coverage")
    phase_names = ["Baseline\n(no safeguards)", "After Phase A", "After Phase B", "After Phase C"]
    coverage = [15, 55, 80, 95]
    df_line = pd.DataFrame({"Phase": phase_names, "Coverage (%)": coverage})
    fig2 = px.line(
        df_line, x="Phase", y="Coverage (%)",
        markers=True,
        line_shape="spline",
        color_discrete_sequence=["#22c55e"],
    )
    fig2.add_hline(y=80, line_dash="dash", line_color="#f59e0b",
                   annotation_text="Target minimum", annotation_font_color="#f59e0b")
    fig2.update_traces(marker=dict(size=12, color="#22c55e"), line=dict(width=3))
    fig2.update_layout(
        paper_bgcolor="#ffffff",
        plot_bgcolor="#ffffff",
        font=dict(color="#334155"),
        yaxis=dict(range=[0, 100], showgrid=False, title="Safeguard coverage (%)"),
        xaxis=dict(showgrid=False, title=""),
        margin=dict(l=10, r=10, t=10, b=10),
    )
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# ── One-slide summary ──────────────────────────────────────────────────────
st.markdown("### \U0001f4cc One-slide summary (what to say in a meeting)")
st.markdown(
    """
    <div style='background:#eff6ff; border:1px solid #2563eb; border-radius:12px;
                padding:24px 28px; text-align:center;'>
      <p style='color:#1e40af; font-size:1.3rem; font-weight:700; margin:0 0 12px;'>
        We don't need perfect AI.
      </p>
      <div style='display:flex; justify-content:center; gap:16px; flex-wrap:wrap;'>
        <span style='background:#f0fdf4; border:1px solid #22c55e; border-radius:20px;
                     padding:6px 16px; color:#16a34a; font-weight:600;'>✅ Fails safely</span>
        <span style='background:#eff6ff; border:1px solid #3b82f6; border-radius:20px;
                     padding:6px 16px; color:#1e40af; font-weight:600;'>🔍 Is reviewable</span>
        <span style='background:#fffbeb; border:1px solid #f59e0b; border-radius:20px;
                     padding:6px 16px; color:#92400e; font-weight:600;'>🏛️ Is governed</span>
        <span style='background:#faf5ff; border:1px solid #a855f7; border-radius:20px;
                     padding:6px 16px; color:#7c3aed; font-weight:600;'>🤝 Earns public trust</span>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)
