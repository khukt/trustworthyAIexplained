import streamlit as st
import plotly.express as px
import pandas as pd

st.title("4\ufe0f\u20e3 Common AI Failure Stories")
st.markdown(
    "<p style='color:#94a3b8; font-size:1.05rem;'>"
    "Most AI incidents are <strong>not</strong> caused by 'evil AI'. "
    "They are caused by <strong>missing safeguards</strong>."
    "</p>",
    unsafe_allow_html=True,
)

st.divider()

stories = [
    {
        "icon": "\u2696\ufe0f",
        "title": "Bias in data \u2192 unfair decisions",
        "color": "#f59e0b",
        "what_went_wrong": "Historical data reflected unequal treatment; the AI learned and repeated it.",
        "what_prevents": "Fairness checks, representative data, and regular audits.",
        "risk": 85,
        "prevention": 90,
    },
    {
        "icon": "\U0001f4c5",
        "title": "Out-of-date data \u2192 wrong recommendations",
        "color": "#ef4444",
        "what_went_wrong": "Reality changed, but the model still used older patterns and assumptions.",
        "what_prevents": "Data freshness checks + monitoring + scheduled re-evaluation.",
        "risk": 75,
        "prevention": 85,
    },
    {
        "icon": "\U0001f310",
        "title": "Used outside intended context \u2192 unpredictable behavior",
        "color": "#a855f7",
        "what_went_wrong": "AI trained for one setting was deployed in another (new region, new population, new conditions).",
        "what_prevents": "Clear scope documentation + out-of-context detection + human review.",
        "risk": 80,
        "prevention": 80,
    },
    {
        "icon": "\U0001f6a8",
        "title": "No monitoring after deployment \u2192 problems discovered too late",
        "color": "#3b82f6",
        "what_went_wrong": "Performance drifted silently; errors accumulated before anyone noticed.",
        "what_prevents": "Monitoring, alerts, incident response, and logging/audit trails.",
        "risk": 90,
        "prevention": 92,
    },
]

# ── Story cards ────────────────────────────────────────────────────────────
for s in stories:
    with st.expander(f"{s['icon']}  {s['title']}", expanded=True):
        col_text, col_bar = st.columns([2, 1], gap="large")
        with col_text:
            st.markdown(
                f"<div style='background:#2d1515; border-left:4px solid #ef4444; "
                f"border-radius:6px; padding:12px 16px; margin-bottom:10px;'>"
                f"<strong style='color:#fca5a5;'>\u26a0\ufe0f What went wrong:</strong><br>"
                f"<span style='color:#fecaca;'>{s['what_went_wrong']}</span>"
                f"</div>",
                unsafe_allow_html=True,
            )
            st.markdown(
                f"<div style='background:#14291e; border-left:4px solid #22c55e; "
                f"border-radius:6px; padding:12px 16px;'>"
                f"<strong style='color:#86efac;'>\u2705 What prevents it:</strong><br>"
                f"<span style='color:#bbf7d0;'>{s['what_prevents']}</span>"
                f"</div>",
                unsafe_allow_html=True,
            )
        with col_bar:
            df_bar = pd.DataFrame({
                "": ["Risk level", "Prevention effectiveness"],
                "Score": [s["risk"], s["prevention"]],
                "Color": ["#ef4444", "#22c55e"],
            })
            fig = px.bar(
                df_bar, x="Score", y="", orientation="h",
                color="",
                color_discrete_map={"Risk level": "#ef4444", "Prevention effectiveness": "#22c55e"},
                text="Score",
            )
            fig.update_traces(texttemplate="%{text}%", textposition="inside")
            fig.update_layout(
                paper_bgcolor="#1e293b",
                plot_bgcolor="#1e293b",
                font=dict(color="#cbd5e1"),
                showlegend=False,
                xaxis=dict(range=[0, 100], showgrid=False, title=""),
                yaxis=dict(title=""),
                margin=dict(l=0, r=10, t=10, b=10),
                height=100,
            )
            st.plotly_chart(fig, use_container_width=True)

st.divider()

# ── Summary chart ──────────────────────────────────────────────────────────
st.markdown("### \U0001f4ca Risk vs Prevention effectiveness across all stories")
df_summary = pd.DataFrame({
    "Story": [s["title"][:35] + "..." if len(s["title"]) > 35 else s["title"] for s in stories],
    "Risk level": [s["risk"] for s in stories],
    "Prevention effectiveness": [s["prevention"] for s in stories],
})
fig_sum = px.scatter(
    df_summary,
    x="Risk level",
    y="Prevention effectiveness",
    text="Story",
    size=[20, 20, 20, 20],
    color="Risk level",
    color_continuous_scale=["#22c55e", "#f59e0b", "#ef4444"],
    range_color=[60, 100],
)
fig_sum.update_traces(textposition="top center", marker_sizemin=15)
fig_sum.update_layout(
    paper_bgcolor="#1e293b",
    plot_bgcolor="#1e293b",
    font=dict(color="#cbd5e1"),
    coloraxis_showscale=False,
    xaxis=dict(range=[60, 100], title="Risk level (%)", showgrid=False),
    yaxis=dict(range=[70, 100], title="Prevention effectiveness (%)", showgrid=False),
    margin=dict(l=10, r=10, t=20, b=10),
    height=300,
)
st.plotly_chart(fig_sum, use_container_width=True)

st.markdown(
    "<div style='background:#1e3a5f; border:1px solid #2563eb; border-radius:10px; "
    "padding:16px 20px; color:#93c5fd; font-size:1rem;'>"
    "\U0001f4a1 <strong>Key takeaway:</strong> Every failure story on this page has a known, "
    "practical prevention. The question is whether organisations invest in safeguards <em>before</em> "
    "incidents occur."
    "</div>",
    unsafe_allow_html=True,
)
