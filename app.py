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
        "title": "Stage 1 — Definition & stakes",
        "body": "Start with what trustworthy AI means, then connect it to leadership risk, trust, and public impact.",
        "icon": "menu_book",
        "accent": "#2563eb",
        "items": ["what_is", "why"],
    },
    {
        "title": "Stage 2 — Risk & safeguards",
        "body": "See how the EU risk lens works and how safeguards change decisions in a live example.",
        "icon": "radar",
        "accent": "#0f766e",
        "items": ["risk", "demo"],
    },
    {
        "title": "Stage 3 — Failures & action",
        "body": "Finish with common failure patterns and a practical roadmap for governance and rollout.",
        "icon": "task_alt",
        "accent": "#9333ea",
        "items": ["stories", "roadmap"],
    },
]

TRUST_DIMENSIONS = [
    {
        "label": "Reliable",
        "direction": "north",
        "accent": "#2563eb",
        "question": "Will it work consistently in the situations we expect?",
        "note": "Ask for evidence of stable performance, known limits, and monitoring after launch.",
    },
    {
        "label": "Safe",
        "direction": "east",
        "accent": "#0f766e",
        "question": "What stops harm when the system is uncertain or wrong?",
        "note": "Look for thresholds, fallback paths, escalation rules, and human intervention points.",
    },
    {
        "label": "Fair",
        "direction": "south_east",
        "accent": "#ea580c",
        "question": "Could it produce unfair outcomes for some people or groups?",
        "note": "Check who may be affected, how bias is tested, and what happens if a problem is found.",
    },
    {
        "label": "Transparent",
        "direction": "south_west",
        "accent": "#7c3aed",
        "question": "Will people know when AI is used and how a decision can be traced?",
        "note": "Expect documentation, traceability, and explanations that non-experts can follow.",
    },
    {
        "label": "Accountable",
        "direction": "west",
        "accent": "#9333ea",
        "question": "Who is responsible when something goes wrong?",
        "note": "Clarify ownership, governance roles, review rights, and escalation authority.",
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
          <div class='home-side-label'>{material_icon('groups', 18, '#1d4ed8')} Who this is for</div>
          <div class='home-side-title'>Built for leaders, policy teams, and anyone who needs a practical overview without deep technical detail.</div>
          <div class='home-side-copy'>
            Use it to build shared language, understand risk, and decide what safeguards and governance you should expect before adoption.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    action_a, action_b = st.columns(2, gap="small")
    with action_a:
        st.page_link(PAGES["what_is"]["path"], label="Start with basics", icon=PAGE_ICONS["what_is"])
    with action_b:
        st.page_link(PAGES["demo"]["path"], label="See the demo", icon=PAGE_ICONS["demo"])

    st.markdown(
        """
        <div class='home-kpi-grid'>
          <div class='home-kpi'>
            <div class='home-kpi-value'>3</div>
            <div class='home-kpi-label'>Stages in the story</div>
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
            <div class='home-kpi-value'>2</div>
            <div class='home-kpi-label'>Lenses: policy and practice</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

main_left, main_right = st.columns([1.12, 0.88], gap="large")

with main_left:
    render_section_intro(
        title="Read it in three stages",
        body="Move from basics to risk to action. Each stage groups two pages around one concrete question.",
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
        body="Use these five checks before you rely on an AI system in policy, operations, or service delivery.",
        icon_name="dashboard",
        accent="#0f766e",
    )

    compass_points_html = "".join(
        f"""
        <div class='trust-compass-point trust-compass-point-{item["direction"]}'>
          <span class='trust-compass-point-dot' style='background:{item["accent"]};'></span>
          <span>{item["label"]}</span>
        </div>
        """
        for item in TRUST_DIMENSIONS
    )
    trust_checks_html = "".join(
        f"""
        <div class='trust-check-card'>
          <div class='trust-check-title'>
            <span class='trust-row-dot' style='background:{item["accent"]};'></span>
            {item["label"]}
          </div>
          <div class='trust-check-question'>{item["question"]}</div>
          <div class='trust-check-note'>{item["note"]}</div>
        </div>
        """
        for item in TRUST_DIMENSIONS
    )
    st.markdown(
        f"""
        <div class='trust-compass-panel'>
          <div class='trust-compass-visual'>
            <div class='trust-compass-ring'></div>
            <div class='trust-compass-axis trust-compass-axis-vertical'></div>
            <div class='trust-compass-axis trust-compass-axis-horizontal'></div>
            {compass_points_html}
            <div class='trust-compass-center'>
              <div class='trust-compass-kicker'>Start here</div>
              <div class='trust-compass-center-title'>Ask these five questions before you trust the system.</div>
              <div class='trust-compass-center-copy'>If one answer is weak or unclear, adoption should slow down until safeguards are stronger.</div>
            </div>
          </div>
          <div class='trust-compass-legend'>
            {trust_checks_html}
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.divider()

render_section_intro(
    title="What you should leave with",
    body="The home page should set up three practical outcomes for the rest of the walkthrough.",
    icon_name="checklist",
)

outcome_a, outcome_b, outcome_c = st.columns(3, gap="large")
for column, title, desc, accent, icon in [
    (outcome_a, "Shared language", "A plain-language way to explain trustworthy AI beyond vague ethics terminology.", "#2563eb", "forum"),
    (outcome_b, "Clearer risk judgment", "A better sense of when AI use becomes high-stakes and needs stronger safeguards.", "#0f766e", "shield"),
    (outcome_c, "Practical next steps", "A short roadmap for governance, oversight, and safer deployment decisions.", "#9333ea", "task_alt"),
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
