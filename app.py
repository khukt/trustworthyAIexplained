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
        "title": "Stage 1 — Understand",
        "body": "Build shared language first so later risk and policy decisions are easier to frame.",
        "icon": "menu_book",
        "accent": "#2563eb",
        "items": ["what_is", "why"],
    },
    {
        "title": "Stage 2 — Assess",
        "body": "Move from abstract principles into risk classification and one concrete operational example.",
        "icon": "radar",
        "accent": "#0f766e",
        "items": ["risk", "demo"],
    },
    {
        "title": "Stage 3 — Decide",
        "body": "Close with failure patterns and a short action list leaders can immediately use.",
        "icon": "task_alt",
        "accent": "#9333ea",
        "items": ["stories", "roadmap"],
    },
]

TRUST_DIMENSIONS = [
    {
        "label": "Reliable",
        "score": 0.88,
        "accent": "#2563eb",
        "note": "Performs consistently enough to support real decisions.",
    },
    {
        "label": "Safe",
        "score": 0.84,
        "accent": "#0f766e",
        "note": "Controls reduce harm when the system is uncertain or wrong.",
    },
    {
        "label": "Fair",
        "score": 0.78,
        "accent": "#ea580c",
        "note": "Outcomes should avoid unjustified differences across people or groups.",
    },
    {
        "label": "Transparent",
        "score": 0.86,
        "accent": "#7c3aed",
        "note": "People should know when AI is used and how decisions can be traced.",
    },
    {
        "label": "Accountable",
        "score": 0.81,
        "accent": "#9333ea",
        "note": "Clear ownership, oversight, and review stay with people and institutions.",
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


def trust_status(score: float) -> tuple[str, str]:
    if score >= 0.84:
        return ("Strong", "trust-status-strong")
    if score >= 0.78:
        return ("Moderate", "trust-status-moderate")
    return ("Needs attention", "trust-status-attention")


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
          <div class='home-side-title'>Read the first stage, then test the demo, then finish on the roadmap.</div>
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
        title="Read it in three stages",
        body="The home page now works like a table of contents: each stage groups two pages with a clear purpose.",
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

    average_score = sum(item["score"] for item in TRUST_DIMENSIONS) / len(TRUST_DIMENSIONS)
    average_label, average_class = trust_status(average_score)
    strongest_dimension = max(TRUST_DIMENSIONS, key=lambda item: item["score"])
    weakest_dimension = min(TRUST_DIMENSIONS, key=lambda item: item["score"])
    bars_html = "".join(
        f"""
        <div class='trust-row'>
          <div class='trust-row-top'>
            <div class='trust-row-label'>
              <span class='trust-row-dot' style='background:{item["accent"]};'></span>
              {item["label"]}
            </div>
            <div class='trust-status {trust_status(item["score"])[1]}'>{trust_status(item["score"])[0]}</div>
          </div>
          <div class='trust-row-bar'>
            <span style='width:{item["score"] * 100:.0f}%; background:{item["accent"]};'></span>
          </div>
          <div class='trust-row-note'>{item["note"]}</div>
        </div>
        """
        for item in TRUST_DIMENSIONS
    )
    st.markdown(
        f"""
        <div class='trust-compass-panel'>
          <div class='trust-compass-hero'>
            <div>
              <div class='trust-compass-kicker'>Briefing view</div>
              <div class='trust-compass-score'>{average_label}</div>
              <div class='trust-compass-copy'>Overall signal across the five trust dimensions emphasized throughout this walkthrough.</div>
            </div>
            <div class='trust-compass-side'>
              <div class='trust-compass-side-label'>Strongest signal</div>
              <div class='trust-compass-side-value'>{strongest_dimension["label"]}</div>
              <div class='trust-compass-side-label' style='margin-top:0.75rem;'>Needs more scrutiny</div>
              <div class='trust-compass-side-value'>{weakest_dimension["label"]}</div>
            </div>
          </div>
          <div class='trust-compass-bars'>
            {bars_html}
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class='card'>
          <div class='card-title'>Questions to ask before adoption</div>
          <ul class='home-bullet-list'>
            <li>Where could this AI system create meaningful harm if it fails?</li>
            <li>What human oversight exists when confidence is low or context changes?</li>
            <li>What evidence would prove the system is reliable, fair, and accountable enough to use?</li>
          </ul>
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
