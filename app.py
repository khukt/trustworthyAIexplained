import plotly.graph_objects as go
import streamlit as st

from trust_utils import PAGE_ICONS, material_icon, render_section_intro, setup_page


setup_page("home", "Trustworthy AI Explained")

PAGES = {
    "what_is": {
        "path": "pages/1_What_is_Trustworthy_AI.py",
        "label": "What is Trustworthy AI?",
        "summary": "Start with the shared definition, the recurring dimensions, and what trustworthy AI means in practice.",
        "icon": "verified_user",
        "accent": "#2563eb",
    },
    "why": {
        "path": "pages/2_Why_should_we_care.py",
        "label": "Why it matters",
        "summary": "Connect trustworthiness to legitimacy, operational risk, budgets, and leadership accountability.",
        "icon": "warning",
        "accent": "#ea580c",
    },
    "risk": {
        "path": "pages/3_EU_AI_Act_Risk_Categories.py",
        "label": "EU AI Act risk categories",
        "summary": "See how the EU frames AI risk and where obligations become significantly stricter.",
        "icon": "policy",
        "accent": "#7c3aed",
    },
    "demo": {
        "path": "pages/3_Interactive_mini_demo.py",
        "label": "Interactive mini-demo",
        "summary": "Use a live example to see how safeguards and human review change decisions.",
        "icon": "tune",
        "accent": "#0f766e",
    },
    "stories": {
        "path": "pages/4_Failure_stories.py",
        "label": "Failure stories",
        "summary": "Review common breakdowns and the controls that would have reduced harm.",
        "icon": "auto_stories",
        "accent": "#2563eb",
    },
    "roadmap": {
        "path": "pages/5_Roadmap.py",
        "label": "Roadmap",
        "summary": "Finish with a practical checklist for policy, governance, and rollout.",
        "icon": "route",
        "accent": "#9333ea",
    },
}

ACTS = [
    {
        "title": "Act I — Understand",
        "body": "Build shared language first so later risk and policy decisions are easier to frame.",
        "icon": "menu_book",
        "accent": "#2563eb",
        "items": ["what_is", "why"],
    },
    {
        "title": "Act II — Assess",
        "body": "Move from abstract principles into risk classification and one concrete operational example.",
        "icon": "radar",
        "accent": "#0f766e",
        "items": ["risk", "demo"],
    },
    {
        "title": "Act III — Decide",
        "body": "Close with failure patterns and a short action list leaders can immediately use.",
        "icon": "task_alt",
        "accent": "#9333ea",
        "items": ["stories", "roadmap"],
    },
]


def render_page_summary(page_key: str) -> None:
    page = PAGES[page_key]
    st.markdown(
        f"""
        <div class='home-page-summary'>
          <div class='home-page-title'>
            <span class='home-page-dot' style='background:{page["accent"]};'></span>
            {page["label"]}
          </div>
          <div class='home-page-copy'>{page["summary"]}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


hero_left, hero_right = st.columns([1.18, 0.82], gap="large")

with hero_left:
    st.markdown(
        f"""
        <div class='home-hero-card'>
          <div class='home-hero-kicker'>Decision-maker briefing</div>
          <div class='home-hero-title-row'>
            <div class='home-hero-mark'>{material_icon('robot_2', 30, '#2563eb')}</div>
            <div>
              <div class='home-hero-title'>Trustworthy AI — Explained</div>
              <div class='home-hero-copy'>
                A guided walkthrough for leaders who need a clear view of trust, risk, regulation, and what to require from teams.
              </div>
            </div>
          </div>
          <div class='home-chip-row'>
            <span class='chip'>Board-ready</span>
            <span class='chip'>EU-aligned</span>
            <span class='chip'>Interactive demo</span>
            <span class='chip'>Action-focused</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with hero_right:
    st.markdown(
        f"""
        <div class='home-side-card'>
          <div class='home-side-label'>{material_icon('explore', 18, '#1d4ed8')} Recommended route</div>
          <div class='home-side-title'>Read the first act, then test the demo, then finish on the roadmap.</div>
          <div class='home-side-copy'>
            The sequence is designed to move from understanding to assessment to action without forcing technical detail too early.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    action_a, action_b = st.columns(2, gap="small")
    with action_a:
        st.page_link(PAGES["what_is"]["path"], label="Start briefing", icon=PAGE_ICONS["what_is"])
    with action_b:
        st.page_link(PAGES["demo"]["path"], label="Open demo", icon=PAGE_ICONS["demo"])

    st.markdown(
        """
        <div class='home-kpi-grid'>
          <div class='home-kpi'>
            <div class='home-kpi-value'>3</div>
            <div class='home-kpi-label'>Acts in the story</div>
          </div>
          <div class='home-kpi'>
            <div class='home-kpi-value'>6</div>
            <div class='home-kpi-label'>Short sections</div>
          </div>
          <div class='home-kpi'>
            <div class='home-kpi-value'>1</div>
            <div class='home-kpi-label'>Live demo</div>
          </div>
          <div class='home-kpi'>
            <div class='home-kpi-value'>10 min</div>
            <div class='home-kpi-label'>Approximate briefing time</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

main_left, main_right = st.columns([1.12, 0.88], gap="large")

with main_left:
    render_section_intro(
        title="Read it in three acts",
        body="The home page now works like a table of contents: each act groups two pages with a clear purpose.",
        icon_name="route",
    )

    for act in ACTS:
        st.markdown(
            f"""
            <div class='home-act-card'>
              <div class='home-act-header'>
                <div class='home-act-icon' style='background:{act["accent"]}14;'>
                  {material_icon(act["icon"], 22, act["accent"])}
                </div>
                <div>
                  <div class='home-act-title'>{act["title"]}</div>
                  <div class='home-act-copy'>{act["body"]}</div>
                </div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        for page_key in act["items"]:
            render_page_summary(page_key)
        buttons = st.columns(2, gap="small")
        for column, page_key in zip(buttons, act["items"]):
            with column:
                st.page_link(PAGES[page_key]["path"], label=PAGES[page_key]["label"], icon=PAGE_ICONS[page_key])

with main_right:
    render_section_intro(
        title="Trust compass",
        body="A compact view of the five qualities that appear repeatedly across frameworks and governance discussions.",
        icon_name="dashboard",
        accent="#0f766e",
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
        height=360,
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
          <div class='card-title'>Questions to take into a meeting</div>
          <ul class='home-bullet-list'>
            <li>Where could this AI system create meaningful harm if it fails?</li>
            <li>What human oversight exists when confidence is low or context changes?</li>
            <li>What evidence would prove the system is reliable, fair, and accountable enough to use?</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class='surface-strip'>
          <div class='card-title'>Why this structure works</div>
          <div class='card-desc'>
            It starts with shared vocabulary, shifts into concrete risk, and ends with decision-ready actions.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.divider()

render_section_intro(
    title="What you leave with",
    body="The briefing is designed to produce three immediate outcomes.",
    icon_name="checklist",
)

outcome_a, outcome_b, outcome_c = st.columns(3, gap="large")
for column, title, desc, accent, icon in [
    (outcome_a, "Shared language", "A clearer explanation of trustworthy AI that goes beyond generic ethics slogans.", "#2563eb", "forum"),
    (outcome_b, "Risk awareness", "A better sense of when AI use becomes high-stakes and demands stronger controls.", "#0f766e", "shield"),
    (outcome_c, "Actionable next steps", "A compact roadmap for governance, oversight, and safer deployment decisions.", "#9333ea", "task_alt"),
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
