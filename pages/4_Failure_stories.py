import streamlit as st

from trust_utils import material_icon, render_callout, render_page_header, render_section_intro, setup_page


setup_page("stories", "Failure stories")

render_page_header(
    title="Common AI Failure Stories",
    subtitle="Most AI incidents do not come from science fiction scenarios. They usually come from ordinary governance gaps.",
    icon_name="auto_stories",
    accent="#2563eb",
    chips=["Bias", "Stale data", "Wrong context", "No monitoring"],
    eyebrow="Failure patterns",
)

render_callout(
    title="How to read this page",
    body="Each story follows the same pattern: what happened, what failed, and what practical control would have reduced the risk.",
    icon_name="search_insights",
    accent="#1d4ed8",
)

st.markdown("<hr>", unsafe_allow_html=True)

render_section_intro(
    title="A simple pattern appears again and again",
    body="The failure is rarely 'AI became evil'. The pattern is usually a system used with weak controls, weak oversight, or the wrong assumptions.",
    icon_name="pattern",
)

intro_a, intro_b = st.columns(2, gap="large")
with intro_a:
    st.markdown(
        """
        <div class="card">
          <div class="card-title">What failure stories are really about</div>
          <div class="card-desc">
            They show where organizations rely on AI <strong>without enough checks, review, or monitoring</strong>.
            The point is not to memorize incidents. It is to recognize recurring failure patterns before they happen again.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with intro_b:
    st.markdown(
        """
        <div class="card">
          <div class="card-title">What to look for in every case</div>
          <ul>
            <li>Was the system used outside its safe limits?</li>
            <li>Did people understand what the AI was doing?</li>
            <li>Were monitoring and escalation paths already in place?</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<hr>", unsafe_allow_html=True)

stories = [
    {
        "kicker": "Bias pattern",
        "title": "Historical bias is repeated as if it were objective truth",
        "icon": "balance",
        "accent": "#f59e0b",
        "what_happened": "An AI system learned from past decisions that already reflected unequal treatment. It then repeated those patterns at scale.",
        "what_failed": "Past outcomes were treated as if they were neutral ground truth, and outcome gaps were not checked seriously enough.",
        "what_helps": "Representative data, outcome monitoring across groups, and a clear fairness review process before and after deployment.",
        "lesson": "If historical decisions were unequal, an AI system can make that inequality faster and harder to notice.",
        "tags": ["Fairness", "Data", "Audits"],
    },
    {
        "kicker": "Data pattern",
        "title": "Stale data makes the system confident about the wrong world",
        "icon": "calendar_month",
        "accent": "#ef4444",
        "what_happened": "Conditions changed, but the model still relied on older patterns and assumptions. Outputs looked plausible while becoming less relevant.",
        "what_failed": "Data freshness was not treated as a live governance issue, and the organization had weak monitoring after deployment.",
        "what_helps": "Data freshness checks, scheduled re-evaluation, trigger points for retraining, and visible ownership for monitoring performance drift.",
        "lesson": "A model can fail quietly when the world changes faster than the governance around it.",
        "tags": ["Monitoring", "Data age", "Drift"],
    },
    {
        "kicker": "Scope pattern",
        "title": "A system built for one setting is used in another",
        "icon": "public",
        "accent": "#a855f7",
        "what_happened": "An AI system trained for one population, region, or workflow was used in a different context where its assumptions no longer held.",
        "what_failed": "The deployment team treated the model as general-purpose and did not manage out-of-context risk explicitly.",
        "what_helps": "Clear scope documentation, validation for the new context, out-of-context detection, and human review when cases look unusual.",
        "lesson": "A system that works well somewhere can still become unreliable when the context changes.",
        "tags": ["Scope", "Validation", "Human review"],
    },
    {
        "kicker": "Operations pattern",
        "title": "No monitoring means problems are discovered after damage accumulates",
        "icon": "siren",
        "accent": "#3b82f6",
        "what_happened": "Performance drifted or error patterns grew over time, but no one had a clear signal, alert, or review process to spot it early.",
        "what_failed": "Deployment was treated as the finish line. Logging, incident handling, and post-market-style monitoring were too weak or absent.",
        "what_helps": "Monitoring dashboards, alerts, audit trails, incident response, and a named team responsible for acting on warning signs.",
        "lesson": "If no one is watching the system after launch, small issues can become institutional failures.",
        "tags": ["Monitoring", "Audit trail", "Ownership"],
    },
]

render_section_intro(
    title="Four recurring failure patterns",
    body="These examples are generalized patterns, but they reflect the kinds of problems organizations repeatedly encounter.",
    icon_name="warning",
)

for story in stories:
    tags_html = "".join(f'<span class="failure-tag">{tag}</span>' for tag in story["tags"])
    st.markdown(
        (
            '<div class="failure-story-card">'
            f'<div class="failure-story-kicker">{story["kicker"]}</div>'
            f'<div class="failure-story-title">{material_icon(story["icon"], 20, story["accent"])} {story["title"]}</div>'
            f"{tags_html}"
            f'<div class="failure-story-copy">{story["what_happened"]}</div>'
            '<div class="failure-panel failure-panel-bad">'
            '<div class="failure-panel-title">What failed</div>'
            f'<div class="failure-panel-copy">{story["what_failed"]}</div>'
            "</div>"
            '<div class="failure-panel failure-panel-good">'
            '<div class="failure-panel-title">What would have helped</div>'
            f'<div class="failure-panel-copy">{story["what_helps"]}</div>'
            "</div>"
            f'<div class="failure-lesson"><strong>Lesson:</strong> {story["lesson"]}</div>'
            "</div>"
        ),
        unsafe_allow_html=True,
    )
    st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

render_section_intro(
    title="What these stories have in common",
    body="The same lesson appears across all four examples: the failure usually comes from governance gaps, not from the mere fact that AI exists.",
    icon_name="insights",
)

common_a, common_b, common_c = st.columns(3, gap="large")
for column, title, desc, accent, icon in [
    (
        common_a,
        "Weak assumptions",
        "The organization assumes the training data, context, or old performance still holds.",
        "#f59e0b",
        "rule",
    ),
    (
        common_b,
        "Weak controls",
        "Thresholds, review rules, documentation, or monitoring are missing or too weak.",
        "#0f766e",
        "tune",
    ),
    (
        common_c,
        "Weak ownership",
        "No one is clearly responsible for checking the system, responding to issues, and stopping harmful use.",
        "#2563eb",
        "person_alert",
    ),
]:
    with column:
        st.markdown(
            f"""
            <div class="card">
              <div class="card-title">{material_icon(icon, 18, accent)} {title}</div>
              <div class="card-desc">{desc}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(
    (
        '<div class="section-note">'
        "<strong>Key takeaway:</strong> Every story on this page has a practical prevention. "
        "The real question is whether the organization adds safeguards before something goes wrong rather than after."
        "</div>"
    ),
    unsafe_allow_html=True,
)
