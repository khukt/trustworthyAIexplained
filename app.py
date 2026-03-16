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

summary_left, summary_right = st.columns([1.15, 0.85], gap="large")

with summary_left:
    render_section_intro(
        title="Follow the story",
        body="Each page uses the same layout and navigation, so the message is faster to scan.",
        icon_name="route",
    )

    descriptions = {
        "what_is": "See the core idea and key dimensions.",
        "why": "See the leadership, trust, and budget impact.",
        "risk": "See how the EU AI Act classifies risk.",
        "demo": "Walk through one live example.",
        "stories": "Review common failures and fixes.",
        "roadmap": "Leave with a practical action plan.",
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

    for start in range(0, len(story_items), 3):
        row_items = story_items[start:start + 3]
        row_columns = st.columns(3, gap="large")
        for column, (key, path, label) in zip(row_columns, row_items):
            accent = accents[key]
            with column:
                st.markdown(
                    f"""
                    <div class='card' style='margin-bottom:0;'>
                        <div style='display:flex; gap:12px; align-items:flex-start;'>
                            <div class='hero-icon' style='width:44px; height:44px; border-radius:14px; background:{accent}14;'>
                                {material_icon(icons[key], 22, accent)}
                            </div>
                            <div style='flex:1;'>
                                <div class='card-title'>{label}</div>
                                <div class='card-desc'>{descriptions[key]}</div>
                            </div>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.page_link(path, label="Open section", icon=PAGE_ICONS[key])

with summary_right:
    render_section_intro(
        title="Trust snapshot",
        body="A quick view of the five qualities emphasized throughout the app.",
        icon_name="radar",
    )

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
        polar=dict(
            bgcolor="rgba(255,255,255,0)",
            radialaxis=dict(visible=True, range=[0, 1], gridcolor="#dbe5f1"),
        ),
        paper_bgcolor="rgba(255,255,255,0)",
        margin=dict(l=10, r=10, t=20, b=20),
        showlegend=False,
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
        """
        <div class='surface-strip'>
          <div class='card-title'>What improved in the redesign</div>
          <div class='card-desc'>
            One visual system, one story-first sidebar, and more consistent page sections.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.divider()

insight_a, insight_b, insight_c = st.columns(3, gap="large")
for column, title, desc, accent, icon in [
    (insight_a, "Clearer navigation", "The same sidebar appears on every page.", "#2563eb", "explore"),
    (insight_b, "Less duplication", "Shared helpers now handle layout and styling.", "#0f766e", "layers"),
    (insight_c, "Faster scanning", "Headers, cards, and intros now follow one pattern.", "#9333ea", "bolt"),
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
