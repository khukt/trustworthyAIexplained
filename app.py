import plotly.graph_objects as go
import streamlit as st

from trust_utils import NAV_ITEMS, PAGE_ICONS, material_icon, render_callout, render_page_header, render_section_intro, setup_page


setup_page("home", "Trustworthy AI Explained")

render_page_header(
    title="Trustworthy AI — Explained",
    subtitle="A fast walkthrough for leaders: what trustworthy AI means, why it matters, where risk sits, and what to do next.",
    icon_name="robot_2",
    accent="#2563eb",
    chips=["Board-ready", "Interactive", "EU-aligned", "Action-focused"],
    eyebrow="Decision-maker briefing",
)

render_callout(
    title="Best way to use this app",
    body="Read the first three pages, open the mini-demo for one concrete example, then finish with the failure stories and roadmap.",
    icon_name="map",
    accent="#1d4ed8",
)

descriptions = {
    "what_is": "Define the core idea and the dimensions leaders should expect any serious AI program to address.",
    "why": "Connect trustworthiness to public trust, delivery risk, cost, and leadership accountability.",
    "risk": "See the EU AI Act risk ladder and where obligations become stricter.",
    "demo": "Walk through a concrete example and watch safeguards change the outcome.",
    "stories": "Review common failure patterns and the controls that could have prevented them.",
    "roadmap": "Leave with a practical checklist for policy, governance, and rollout.",
}
accents = {
    "what_is": "#2563eb",
    "why": "#ea580c",
    "risk": "#7c3aed",
    "demo": "#0f766e",
    "stories": "#2563eb",
    "roadmap": "#9333ea",
}
icons = {
    "what_is": "verified_user",
    "why": "warning",
    "risk": "policy",
    "demo": "tune",
    "stories": "auto_stories",
    "roadmap": "route",
}
story_items = [item for item in NAV_ITEMS if item[0] != "home"]


def story_title(label: str) -> str:
    return label.split(") ", 1)[1] if ") " in label else label


briefing_stats = [
    ("6", "Short sections to move from basics to action."),
    ("1", "Live mini-demo to make the safeguards discussion concrete."),
    ("10 min", "Approximate read-through for a leadership briefing."),
]

summary_left, summary_right = st.columns([1.25, 0.9], gap="large")

with summary_left:
    render_section_intro(
        title="Follow the story",
        body="The sequence is designed like a briefing: concept first, then risk, then action.",
        icon_name="route",
    )

    left_column, right_column = st.columns(2, gap="large")
    for index, (key, path, label) in enumerate(story_items):
        accent = accents[key]
        target = left_column if index % 2 == 0 else right_column
        with target:
            st.markdown(
                f"""
                <div class='story-card'>
                  <div class='story-step'>Step {index + 1}</div>
                  <div class='story-card-head'>
                    <div class='story-card-icon' style='background:{accent}14;'>
                      {material_icon(icons[key], 22, accent)}
                    </div>
                    <div>
                      <div class='story-card-title'>{story_title(label)}</div>
                      <div class='story-card-desc'>{descriptions[key]}</div>
                    </div>
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.page_link(path, label="Open section", icon=PAGE_ICONS[key])

with summary_right:
    render_section_intro(
        title="Briefing snapshot",
        body="A quick summary of scope, pace, and the trust dimensions emphasized throughout the walkthrough.",
        icon_name="dashboard",
        accent="#0f766e",
    )

    stats_html = "".join(
        f"""
        <div class='home-stat'>
          <div class='home-stat-value'>{value}</div>
          <div class='home-stat-label'>{label}</div>
        </div>
        """
        for value, label in briefing_stats
    )
    st.markdown(f"<div class='home-stat-grid'>{stats_html}</div>", unsafe_allow_html=True)

    categories = ["Reliable", "Safe", "Fair", "Transparent", "Accountable"]
    fig = go.Figure()
    fig.add_trace(
        go.Scatterpolar(
            r=[0.88, 0.84, 0.78, 0.86, 0.81],
            theta=categories,
            fill="toself",
            line_color="#2563eb",
            fillcolor="rgba(37,99,235,0.18)",
            name="Trustworthy AI",
        )
    )
    fig.update_layout(
        height=340,
        polar=dict(
            bgcolor="rgba(255,255,255,0)",
            radialaxis=dict(visible=True, range=[0, 1], gridcolor="#dbe5f1"),
        ),
        paper_bgcolor="rgba(255,255,255,0)",
        margin=dict(l=20, r=20, t=20, b=10),
        showlegend=False,
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
        """
        <div class='card'>
          <div class='card-title'>What leaders should take away</div>
          <ul class='home-bullet-list'>
            <li>Trustworthy AI is about governance and operational discipline, not just model accuracy.</li>
            <li>The regulatory question is risk-based: the higher the impact, the tighter the controls.</li>
            <li>Human oversight, documentation, and monitoring are recurring themes across frameworks.</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.divider()

render_section_intro(
    title="What this briefing gives you",
    body="Three outcomes the rest of the walkthrough reinforces.",
    icon_name="checklist",
)

insight_a, insight_b, insight_c = st.columns(3, gap="large")
for column, title, desc, accent, icon in [
    (insight_a, "Shared vocabulary", "A clearer way to explain trustworthy AI beyond generic ethics language.", "#2563eb", "forum"),
    (insight_b, "Risk lens", "A practical view of where regulation and operational obligations become stronger.", "#0f766e", "shield"),
    (insight_c, "Action checklist", "A compact roadmap for what leaders can require from teams and vendors.", "#9333ea", "task_alt"),
]:
    with column:
        st.markdown(
            f"""
            <div class='card' style='height:100%;'>
              <div class='card-title'>{material_icon(icon, 18, accent)} {title}</div>
              <div class='card-desc'>{desc}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
