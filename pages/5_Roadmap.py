import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from trust_utils import material_icon, render_callout, render_page_header, render_section_intro, setup_page


setup_page("roadmap", "Roadmap")

render_page_header(
    title="What we recommend — a decision-ready roadmap",
    subtitle="A simple roadmap leaders can act on.",
    icon_name="route",
    accent="#9333ea",
    chips=["Quick wins", "Governance", "Continuous improvement"],
    eyebrow="Action plan",
)

render_callout(
    title="How to use this roadmap",
    body="Treat Phase A as the baseline, Phase B as the governance layer, and Phase C as the improvement loop.",
    icon_name="conversion_path",
    accent="#9333ea",
)

phases = [
    {
        "phase": "Phase A",
        "name": "Minimum Safety Baseline",
        "subtitle": "Quick wins",
        "color": "#22c55e",
        "bg": "#f0fdf4",
        "icon": material_icon("verified_user", 28, "#22c55e"),
        "effort": 2,
        "impact": 8,
        "items": [
            "Define what the AI is for — and not for",
            "Add confidence thresholds",
            "Add human review for risky cases",
            "Add basic data quality and freshness checks",
        ],
    },
    {
        "phase": "Phase B",
        "name": "Robust Governance",
        "subtitle": "Structural safeguards",
        "color": "#3b82f6",
        "bg": "#eff6ff",
        "icon": material_icon("account_balance", 28, "#3b82f6"),
        "effort": 5,
        "impact": 9,
        "items": [
            "Add monitoring and alerts",
            "Keep audit trails",
            "Set clear ownership",
            "Repeat documented fairness checks",
        ],
    },
    {
        "phase": "Phase C",
        "name": "Continuous Improvement",
        "subtitle": "Long-term excellence",
        "color": "#a855f7",
        "bg": "#faf5ff",
        "icon": material_icon("autorenew", 28, "#a855f7"),
        "effort": 8,
        "impact": 10,
        "items": [
            "Re-evaluate and update regularly",
            "Improve data coverage and reduce bias",
            "Use independent review for high-impact cases",
            "Learn from incidents",
        ],
    },
]

cols = st.columns(3, gap="large")
for col, phase in zip(cols, phases):
    with col:
        items_html = "".join(f"<li style='margin:4px 0; color:#334155;'>{item}</li>" for item in phase["items"])
        st.markdown(
            f"""
            <div style='background:{phase['bg']}; border:1px solid {phase['color']};
                        border-top:5px solid {phase['color']}; border-radius:12px;
                        padding:20px 16px; min-height:300px;'>
              <div style='font-size:2rem; margin-bottom:6px;'>{phase['icon']}</div>
              <div style='color:{phase['color']}; font-size:0.8rem; font-weight:600;
                          text-transform:uppercase; letter-spacing:1px;'>{phase['phase']}</div>
              <div style='color:#1e293b; font-weight:700; font-size:1.1rem;
                          margin:4px 0 2px;'>{phase['name']}</div>
              <div style='color:#64748b; font-size:0.85rem; margin-bottom:12px;'>{phase['subtitle']}</div>
              <ul style='padding-left:18px; margin:0;'>{items_html}</ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.divider()

left, right = st.columns([1, 1], gap="large")

with left:
    render_section_intro(
        title="Effort vs impact by phase",
        body="A simple view of effort versus expected value.",
        icon_name="scatter_plot",
    )
    df_bubble = pd.DataFrame(
        {
            "Phase": [phase["phase"] + ": " + phase["name"] for phase in phases],
            "Effort": [phase["effort"] for phase in phases],
            "Impact": [phase["impact"] for phase in phases],
            "Size": [30, 40, 50],
            "Color": [phase["color"] for phase in phases],
        }
    )
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
    render_section_intro(
        title="Cumulative safeguard coverage",
        body="Coverage rises as teams move from a baseline toward stronger governance and improvement.",
        icon_name="show_chart",
    )
    phase_names = ["Baseline\n(no safeguards)", "After Phase A", "After Phase B", "After Phase C"]
    coverage = [15, 55, 80, 95]
    df_line = pd.DataFrame({"Phase": phase_names, "Coverage (%)": coverage})
    fig2 = px.line(
        df_line,
        x="Phase",
        y="Coverage (%)",
        markers=True,
        line_shape="spline",
        color_discrete_sequence=["#22c55e"],
    )
    fig2.add_hline(y=80, line_dash="dash", line_color="#f59e0b", annotation_text="Target minimum", annotation_font_color="#f59e0b")
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

st.markdown(
    f"### {material_icon('keep', 20, '#1d4ed8')} One-slide summary (what to say in a meeting)",
    unsafe_allow_html=True,
)
st.markdown(
    "<div style='background:#eff6ff; border:1px solid #2563eb; border-radius:12px; padding:24px 28px; text-align:center;'>"
    "<p style='color:#1e40af; font-size:1.3rem; font-weight:700; margin:0 0 12px;'>We don't need perfect AI.</p>"
    "<div style='display:flex; justify-content:center; gap:16px; flex-wrap:wrap;'>"
    + f"<span style='background:#f0fdf4; border:1px solid #22c55e; border-radius:20px; padding:6px 16px; color:#16a34a; font-weight:600;'>{material_icon('health_and_safety', 18, '#16a34a')} Fails safely</span>"
    + f"<span style='background:#eff6ff; border:1px solid #3b82f6; border-radius:20px; padding:6px 16px; color:#1e40af; font-weight:600;'>{material_icon('manage_search', 18, '#1e40af')} Is reviewable</span>"
    + f"<span style='background:#fffbeb; border:1px solid #f59e0b; border-radius:20px; padding:6px 16px; color:#92400e; font-weight:600;'>{material_icon('gavel', 18, '#92400e')} Is governed</span>"
    + f"<span style='background:#faf5ff; border:1px solid #a855f7; border-radius:20px; padding:6px 16px; color:#7c3aed; font-weight:600;'>{material_icon('handshake', 18, '#7c3aed')} Earns public trust</span>"
    + "</div></div>",
    unsafe_allow_html=True,
)
