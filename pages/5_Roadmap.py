from html import escape

import streamlit as st

from trust_utils import material_icon, render_callout, render_page_header, render_section_intro, setup_page


setup_page("roadmap", "Roadmap")

render_page_header(
    title="Roadmap: from pilot to governed use",
    subtitle="A practical sequence for teams that want AI to be useful, reviewable, and safe enough for the context.",
    icon_name="route",
    accent="#9333ea",
    chips=["Immediate safeguards", "Governance setup", "Operating model"],
    eyebrow="Action plan",
)

render_callout(
    title="How to use this roadmap",
    body="Use it as a sequencing guide. Put guardrails in place first, formalize ownership and evidence next, then monitor and improve continuously. This is a governance roadmap, not a substitute for legal review.",
    icon_name="conversion_path",
    accent="#9333ea",
)

render_section_intro(
    title="Three stages of adoption",
    body="The order matters. Constrain the task first, then make the system governable, then run it like a live service that can drift, fail, and need intervention.",
    icon_name="route",
    accent="#9333ea",
)

stages = [
    {
        "stage": "Stage 1",
        "window": "Immediate safeguards",
        "name": "Constrain the use case",
        "subtitle": "Stop avoidable harm before the system becomes routine.",
        "color": "#22c55e",
        "soft": "rgba(34,197,94,0.10)",
        "icon": material_icon("shield", 28, "#16a34a"),
        "icon_bg": "rgba(220,252,231,0.95)",
        "owner": "Service or product lead",
        "items": [
            "Define what the AI is for, where it helps, and where it should not be used.",
            "Add confidence thresholds, refusal rules, and a clear fallback path.",
            "Require human review for risky, unusual, or low-confidence cases.",
            "Check that critical data is recent enough and fit for the task.",
        ],
        "gate": "Do not widen use until people can intervene and the service can fail safely.",
    },
    {
        "stage": "Stage 2",
        "window": "Governance setup",
        "name": "Make it governable",
        "subtitle": "Turn ad hoc safeguards into repeatable operating rules.",
        "color": "#3b82f6",
        "soft": "rgba(59,130,246,0.10)",
        "icon": material_icon("account_balance", 28, "#2563eb"),
        "icon_bg": "rgba(219,234,254,0.95)",
        "owner": "Business owner with risk and legal support",
        "items": [
            "Name an accountable owner and define an escalation path when something goes wrong.",
            "Keep records of model versions, key decisions, approvals, and exceptions.",
            "Run repeatable fairness, reliability, and documentation checks.",
            "Document who can approve changes, pauses, or temporary overrides.",
        ],
        "gate": "Scaling should require evidence and named accountability, not optimism.",
    },
    {
        "stage": "Stage 3",
        "window": "Operating model",
        "name": "Operate and improve",
        "subtitle": "Treat AI as a managed capability, not a one-time launch.",
        "color": "#a855f7",
        "soft": "rgba(168,85,247,0.10)",
        "icon": material_icon("autorenew", 28, "#9333ea"),
        "icon_bg": "rgba(243,232,255,0.95)",
        "owner": "Service owner with technical and operational leads",
        "items": [
            "Monitor drift, complaints, overrides, incidents, and changes in the operating context.",
            "Re-review the system when data, users, workflows, or legal obligations change.",
            "Use independent challenge for high-impact or high-sensitivity use cases.",
            "Feed lessons from failures, near misses, and audits back into the controls.",
        ],
        "gate": "If conditions change, the system should be adjusted, paused, or withdrawn.",
    },
]

stage_columns = st.columns(3, gap="large")
for col, stage in zip(stage_columns, stages):
    with col:
        items_html = "".join(f"<li>{escape(item)}</li>" for item in stage["items"])
        st.markdown(
            (
                f"<div class='roadmap-stage-card' style='--roadmap-accent:{stage['color']}; --roadmap-soft:{stage['soft']};'>"
                "<div class='roadmap-stage-top'>"
                f"<span class='roadmap-stage-step'>{escape(stage['stage'])}</span>"
                f"<span class='roadmap-stage-window'>{escape(stage['window'])}</span>"
                "</div>"
                "<div class='roadmap-stage-head'>"
                f"<div class='roadmap-stage-icon' style='background:{stage['icon_bg']};'>{stage['icon']}</div>"
                "<div>"
                f"<div class='roadmap-stage-title'>{escape(stage['name'])}</div>"
                f"<div class='roadmap-stage-copy'>{escape(stage['subtitle'])}</div>"
                "</div>"
                "</div>"
                "<div class='roadmap-stage-meta'>"
                "<span class='roadmap-stage-meta-label'>Primary owner</span>"
                f"<span class='roadmap-stage-meta-value'>{escape(stage['owner'])}</span>"
                "</div>"
                "<div class='roadmap-stage-list-label'>What should exist by the end of this stage</div>"
                f"<ul class='roadmap-stage-list'>{items_html}</ul>"
                f"<div class='roadmap-stage-gate'><strong>Decision gate:</strong> {escape(stage['gate'])}</div>"
                "</div>"
            ),
            unsafe_allow_html=True,
        )

st.divider()

left, right = st.columns([1.15, 0.85], gap="large")

with left:
    render_section_intro(
        title="Minimum before wider rollout",
        body="If these elements are missing, the system is not ready to scale or to sit in an important workflow.",
        icon_name="fact_check",
        accent="#2563eb",
    )
    readiness_checks = [
        (
            "Clear scope",
            "The task, boundaries, fallback path, and non-approved uses are documented in plain language.",
        ),
        (
            "Named accountability",
            "One owner is answerable for the use case, even though several teams contribute controls.",
        ),
        (
            "Human intervention",
            "People can review, override, or stop the system when confidence is weak or context changes.",
        ),
        (
            "Evidence pack",
            "There is current evidence for reliability, fairness, data quality, and the conditions under which the system was tested.",
        ),
        (
            "Monitoring and response",
            "Logs, alerts, complaint handling, and incident escalation exist after launch, not only before it.",
        ),
    ]
    checklist_html = "".join(
        (
            "<div class='roadmap-check-item'>"
            f"<div class='roadmap-check-number'>{index}</div>"
            "<div>"
            f"<div class='roadmap-check-title'>{escape(title)}</div>"
            f"<div class='roadmap-check-copy'>{escape(copy)}</div>"
            "</div>"
            "</div>"
        )
        for index, (title, copy) in enumerate(readiness_checks, start=1)
    )
    st.markdown(f"<div class='roadmap-checklist'>{checklist_html}</div>", unsafe_allow_html=True)

with right:
    render_section_intro(
        title="Who should own what",
        body="Trustworthy AI is cross-functional, but accountability should be clear enough that issues never fall between teams.",
        icon_name="groups",
        accent="#0f766e",
    )
    owners = [
        (
            "Business or service owner",
            "Decides whether the use case is worth the risk and what level of error or harm is acceptable.",
        ),
        (
            "Product or operations lead",
            "Designs the workflow, escalation path, and fallback when the system should not decide alone.",
        ),
        (
            "Technical lead",
            "Maintains models, data pipelines, versioning, monitoring, and change control.",
        ),
        (
            "Risk, legal, or compliance",
            "Checks that governance, records, and regulatory obligations match the context and risk level.",
        ),
    ]
    for title, copy in owners:
        st.markdown(
            (
                "<div class='roadmap-owner-card'>"
                f"<div class='roadmap-owner-title'>{escape(title)}</div>"
                f"<div class='roadmap-owner-copy'>{escape(copy)}</div>"
                "</div>"
            ),
            unsafe_allow_html=True,
        )
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

st.divider()

render_section_intro(
    title="If you only do three things this quarter",
    body="This is the shortest credible version of the roadmap for teams that are early in adoption.",
    icon_name="keep",
    accent="#9333ea",
)

priority_cols = st.columns(3, gap="large")
priorities = [
    (
        "Priority 1",
        "Narrow the task",
        "Use AI for a defined job with clear limits instead of letting it quietly become general-purpose.",
    ),
    (
        "Priority 2",
        "Name one accountable owner",
        "Cross-functional support matters, but one person or function still has to own the decision to deploy.",
    ),
    (
        "Priority 3",
        "Instrument the service",
        "If you cannot see drift, complaints, overrides, and failures after launch, you are not governing the system yet.",
    ),
]
for col, (kicker, title, copy) in zip(priority_cols, priorities):
    with col:
        st.markdown(
            (
                "<div class='roadmap-priority-card'>"
                f"<div class='roadmap-priority-kicker'>{escape(kicker)}</div>"
                f"<div class='roadmap-priority-title'>{escape(title)}</div>"
                f"<div class='roadmap-priority-copy'>{escape(copy)}</div>"
                "</div>"
            ),
            unsafe_allow_html=True,
        )

st.markdown("<div style='height:14px;'></div>", unsafe_allow_html=True)

st.markdown(
    (
        "<div class='roadmap-summary'>"
        "<div class='roadmap-summary-kicker'>Decision standard</div>"
        "<div class='roadmap-summary-title'>Do not ask whether the AI is perfect. Ask whether the organization can rely on it responsibly.</div>"
        "<div class='roadmap-summary-copy'>"
        "Proceed when the task is narrow, the evidence is current, a human can intervene, and someone remains accountable after launch. "
        "That is the difference between an interesting pilot and a governable service."
        "</div>"
        "<div class='roadmap-summary-chip-row'>"
        f"<span class='roadmap-summary-chip'>{material_icon('shield', 16, '#5b21b6')} Scoped use</span>"
        f"<span class='roadmap-summary-chip'>{material_icon('manage_search', 16, '#5b21b6')} Reviewable evidence</span>"
        f"<span class='roadmap-summary-chip'>{material_icon('person_alert', 16, '#5b21b6')} Human intervention</span>"
        f"<span class='roadmap-summary-chip'>{material_icon('monitoring', 16, '#5b21b6')} Ongoing monitoring</span>"
        "</div>"
        "</div>"
    ),
    unsafe_allow_html=True,
)
