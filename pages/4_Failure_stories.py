import streamlit as st
import plotly.express as px
import pandas as pd

from trust_utils import material_icon, render_callout, render_page_header, render_section_intro, setup_page


setup_page("stories", "Failure stories")

render_page_header(
    title="Common AI Failure Stories",
    subtitle="Most AI incidents are not caused by 'evil AI'. They are usually caused by missing safeguards.",
    icon_name="auto_stories",
    accent="#2563eb",
    chips=["Bias", "Stale data", "Wrong context", "No monitoring"],
    eyebrow="Failure patterns",
)

render_callout(
    title="What to look for",
    body="Each example pairs a common failure pattern with the practical control that prevents it.",
    icon_name="search_insights",
    accent="#1d4ed8",
)

st.divider()

stories = [
    {
        "icon": material_icon("balance", 22, "#f59e0b"),
        "title": "Bias in data → unfair decisions",
        "color": "#f59e0b",
        "what_went_wrong": "Historical data reflected unequal treatment; the AI learned and repeated it.",
        "what_prevents": "Fairness checks, representative data, and regular audits.",
        "risk": 85,
        "prevention": 90,
    },
    {
        "icon": material_icon("calendar_month", 22, "#ef4444"),
        "title": "Out-of-date data → wrong recommendations",
        "color": "#ef4444",
        "what_went_wrong": "Reality changed, but the model still used older patterns and assumptions.",
        "what_prevents": "Data freshness checks + monitoring + scheduled re-evaluation.",
        "risk": 75,
        "prevention": 85,
    },
    {
        "icon": material_icon("public", 22, "#a855f7"),
        "title": "Used outside intended context → unpredictable behavior",
        "color": "#a855f7",
        "what_went_wrong": "AI trained for one setting was deployed in another (new region, new population, new conditions).",
        "what_prevents": "Clear scope documentation + out-of-context detection + human review.",
        "risk": 80,
        "prevention": 80,
    },
    {
        "icon": material_icon("siren", 22, "#3b82f6"),
        "title": "No monitoring after deployment → problems discovered too late",
        "color": "#3b82f6",
        "what_went_wrong": "Performance drifted silently; errors accumulated before anyone noticed.",
        "what_prevents": "Monitoring, alerts, incident response, and logging/audit trails.",
        "risk": 90,
        "prevention": 92,
    },
]

for story in stories:
    with st.expander(f"{story['icon']}  {story['title']}", expanded=True):
        col_text, col_bar = st.columns([2, 1], gap="large")
        with col_text:
            st.markdown(
                f"<div style='background:#fef2f2; border-left:4px solid #ef4444; border-radius:6px; padding:12px 16px; margin-bottom:10px;'>"
                f"<strong style='color:#dc2626;'>{material_icon('warning', 18, '#dc2626')} What went wrong:</strong><br>"
                f"<span style='color:#991b1b;'>{story['what_went_wrong']}</span>"
                f"</div>",
                unsafe_allow_html=True,
            )
            st.markdown(
                f"<div style='background:#f0fdf4; border-left:4px solid #22c55e; border-radius:6px; padding:12px 16px;'>"
                f"<strong style='color:#16a34a;'>{material_icon('verified', 18, '#16a34a')} What prevents it:</strong><br>"
                f"<span style='color:#166534;'>{story['what_prevents']}</span>"
                f"</div>",
                unsafe_allow_html=True,
            )
        with col_bar:
            df_bar = pd.DataFrame(
                {
                    "": ["Risk level", "Prevention effectiveness"],
                    "Score": [story["risk"], story["prevention"]],
                }
            )
            fig = px.bar(
                df_bar,
                x="Score",
                y="",
                orientation="h",
                color="",
                color_discrete_map={"Risk level": "#ef4444", "Prevention effectiveness": "#22c55e"},
                text="Score",
            )
            fig.update_traces(texttemplate="%{text}%", textposition="inside")
            fig.update_layout(
                paper_bgcolor="#ffffff",
                plot_bgcolor="#ffffff",
                font=dict(color="#334155"),
                showlegend=False,
                xaxis=dict(range=[0, 100], showgrid=False, title=""),
                yaxis=dict(title=""),
                margin=dict(l=0, r=10, t=10, b=10),
                height=100,
            )
            st.plotly_chart(fig, use_container_width=True)

st.divider()

render_section_intro(
    title="Risk vs prevention effectiveness across all stories",
    body="The chart below compares how risky each failure pattern is against how effective known safeguards can be.",
    icon_name="monitoring",
)
df_summary = pd.DataFrame(
    {
        "Story": [story["title"][:35] + "..." if len(story["title"]) > 35 else story["title"] for story in stories],
        "Risk level": [story["risk"] for story in stories],
        "Prevention effectiveness": [story["prevention"] for story in stories],
    }
)
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
    paper_bgcolor="#ffffff",
    plot_bgcolor="#ffffff",
    font=dict(color="#334155"),
    coloraxis_showscale=False,
    xaxis=dict(range=[60, 100], title="Risk level (%)", showgrid=False),
    yaxis=dict(range=[70, 100], title="Prevention effectiveness (%)", showgrid=False),
    margin=dict(l=10, r=10, t=20, b=10),
    height=300,
)
st.plotly_chart(fig_sum, use_container_width=True)

st.markdown(
    f"<div style='background:#eff6ff; border:1px solid #2563eb; border-radius:10px; padding:16px 20px; color:#1e40af; font-size:1rem;'>"
    f"{material_icon('lightbulb', 18, '#1d4ed8')} <strong>Key takeaway:</strong> Every failure story on this page has a known, practical prevention. "
    f"The question is whether organisations invest in safeguards <em>before</em> incidents occur."
    f"</div>",
    unsafe_allow_html=True,
)
