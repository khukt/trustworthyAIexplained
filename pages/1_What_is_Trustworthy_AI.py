import streamlit as st

from trust_utils import material_icon, render_callout, render_page_header, render_section_intro, setup_page


setup_page("what_is", "What is Trustworthy AI?")

render_page_header(
    title="What is Trustworthy AI?",
    subtitle="A plain-language explanation of what the term covers, what it does not, and how major frameworks describe it.",
    icon_name="verified_user",
    accent="#2563eb",
    chips=["Plain language", "EU-aligned", "Governance first", "Framework-aware"],
    eyebrow="Foundations",
)

render_callout(
    title="In one sentence",
    body="Trustworthy AI is AI that can be used responsibly because it is lawful, well-governed, technically robust, and subject to meaningful human oversight.",
    icon_name="menu_book",
    accent="#1d4ed8",
)

st.markdown("<hr>", unsafe_allow_html=True)

render_section_intro(
    title="Start with the basic idea",
    body="The term is not mainly about whether a model is impressive. It is about whether an organization can justify using AI in real decisions.",
    icon_name="lightbulb",
)

intro_left, intro_right = st.columns([1.1, 0.9], gap="large")

with intro_left:
    st.markdown(
        """
        <div class="card">
          <div class="card-title">Plain-language definition</div>
          <div class="card-desc">
            Trustworthy AI means the system is designed and governed so people can rely on it <strong>without losing oversight, accountability, or basic protections</strong>.
            The question is not only “Does it work?” but also:
          </div>
          <ul>
            <li>Is it safe enough for the context?</li>
            <li>Can people understand and challenge its use?</li>
            <li>Is someone clearly responsible for outcomes?</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with intro_right:
    st.markdown(
        """
        <div class="card">
          <div class="card-title">""" + material_icon("check_circle", 18, "#16a34a") + """ What it is</div>
          <div class="card-desc">
            A <strong>governance and risk</strong> approach for using AI in ways that people and institutions can defend.
          </div>
        </div>
        <div style="height:10px;"></div>
        <div class="card">
          <div class="card-title">""" + material_icon("cancel", 18, "#dc2626") + """ What it is not</div>
          <div class="card-desc">
            Not just “high accuracy”, not branding language, and not a claim that automation should replace human judgment.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<hr>", unsafe_allow_html=True)

render_section_intro(
    title="How to recognize it in practice",
    body="Different frameworks use different wording, but they usually point to the same practical checks.",
    icon_name="fact_check",
)

dimensions = [
    (
        "Reliable and robust",
        "The system performs consistently enough for the context and has known limits, monitoring, and fallback plans.",
    ),
    (
        "Safe and controllable",
        "Failures are less likely to cause harm, and humans can intervene when uncertainty or risk increases.",
    ),
    (
        "Fair",
        "The system avoids unjustified differences in treatment or outcomes across people or groups.",
    ),
    (
        "Transparent",
        "People know when AI is being used, what role it plays, and how decisions can be traced or explained.",
    ),
    (
        "Accountable",
        "There is clear ownership for design, deployment, review, and what happens when things go wrong.",
    ),
    (
        "Well-governed data",
        "Data quality, privacy, access, and lifecycle controls are treated as part of trustworthiness, not as an afterthought.",
    ),
]

dim_col_a, dim_col_b = st.columns(2, gap="large")
for index, (title, desc) in enumerate(dimensions):
    target = dim_col_a if index % 2 == 0 else dim_col_b
    with target:
        st.markdown(
            f"""
            <div class="card">
              <div class="card-title">{title}</div>
              <div class="card-desc">{desc}</div>
            </div>
            <div style="height:10px;"></div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("<hr>", unsafe_allow_html=True)

render_section_intro(
    title="What the EU framing adds",
    body="The European discussion uses the same core ideas, but it puts particular weight on oversight, data governance, and broader societal impact.",
    icon_name="policy",
    accent="#7c3aed",
)

eu_left, eu_right = st.columns([1, 1], gap="large")

with eu_left:
    st.markdown(
        """
        <div class="compare-card">
          <div class="compare-kicker">Shared core</div>
          <div class="compare-title">What most frameworks already agree on</div>
          <div class="compare-list">
            <div class="compare-item">
              <span class="compare-dot"></span>
              <div class="compare-copy">AI should be reliable and safe enough for the context in which it is used.</div>
            </div>
            <div class="compare-item">
              <span class="compare-dot"></span>
              <div class="compare-copy">People should be treated fairly and be able to understand the role AI plays.</div>
            </div>
            <div class="compare-item">
              <span class="compare-dot"></span>
              <div class="compare-copy">Organizations should keep clear oversight, accountability, and documentation.</div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with eu_right:
    st.markdown(
        """
        <div class="compare-card compare-card-eu">
          <div class="compare-kicker">EU emphasis</div>
          <div class="compare-title">What the European framing makes more explicit</div>
          <div class="compare-list">
            <div class="compare-item">
              <span class="compare-dot"></span>
              <div class="compare-copy"><strong>Human agency and oversight</strong> are named directly, not treated as background assumptions.</div>
            </div>
            <div class="compare-item">
              <span class="compare-dot"></span>
              <div class="compare-copy"><strong>Privacy and data governance</strong> are central trust questions, not separate compliance topics.</div>
            </div>
            <div class="compare-item">
              <span class="compare-dot"></span>
              <div class="compare-copy"><strong>Societal and environmental impact</strong> matters alongside technical performance.</div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

render_section_intro(
    title="EU High-Level Expert Group: 7 requirements",
    body="These seven requirements make the European framing easier to scan than a long paragraph.",
    icon_name="format_list_bulleted",
    accent="#7c3aed",
)

eu_requirements = [
    ("1", "Human agency and oversight", "AI should support human decision-making and leave room for intervention."),
    ("2", "Technical robustness and safety", "Systems should be resilient, secure, and safe under expected and unexpected conditions."),
    ("3", "Privacy and data governance", "Data protection, quality, integrity, and access control are part of trustworthiness."),
    ("4", "Transparency", "People should know when AI is used and decisions should be traceable and explainable."),
    ("5", "Diversity, non-discrimination and fairness", "Systems should avoid unfair bias and remain accessible and equitable."),
    ("6", "Societal and environmental well-being", "Wider effects on society, institutions, democracy, and sustainability matter."),
    ("7", "Accountability", "There should be clear responsibility, auditability, and routes for review or redress."),
]

for start in range(0, len(eu_requirements), 3):
    row = eu_requirements[start:start + 3]
    columns = st.columns(3, gap="large")
    for column, (number, title, desc) in zip(columns, row):
        with column:
            st.markdown(
                f"""
                <div class="requirement-card">
                  <div class="requirement-number">{number}</div>
                  <div class="requirement-title">{title}</div>
                  <div class="requirement-copy">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

st.markdown(
    """
    <div class="section-note">
      The labels vary across frameworks, but the underlying message is consistent: trustworthy AI is <strong>not only a technical question</strong>.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<hr>", unsafe_allow_html=True)

render_section_intro(
    title="How major organizations group the same idea",
    body="The frameworks below are broadly aligned. What changes is the angle: policy, rights, engineering risk, or management systems.",
    icon_name="hub",
)

framework_options = [
    "EU (HLEG 2019) — 7 requirements",
    "OECD — AI Principles",
    "NIST — AI Risk Management Framework",
    "ISO/IEC — standards (management system + risk)",
]

framework = st.selectbox(
    "Choose a framework:",
    framework_options,
)

if framework.startswith("EU"):
    framework_title = "EU (HLEG 2019)"
    framework_kicker = "Policy-oriented"
    framework_summary = (
        "The EU framing makes oversight, data governance, and societal impact especially visible alongside "
        "robustness, fairness, transparency, and accountability."
    )
    framework_meta = [
        ("Best for", "Public policy and governance discussions"),
        ("Main lens", "Rights, oversight, and public-interest safeguards"),
        ("Style", "Normative and policy-facing"),
    ]
    framework_focus = [
        "Human agency and oversight are explicitly named.",
        "Privacy and data governance are central, not peripheral.",
        "Societal and environmental well-being sits alongside technical performance.",
    ]
elif framework.startswith("OECD"):
    framework_title = "OECD AI Principles"
    framework_kicker = "International policy baseline"
    framework_summary = (
        "The OECD principles give governments and organizations a broad policy vocabulary focused on values, transparency, robustness, and accountability."
    )
    framework_meta = [
        ("Best for", "Cross-country or cross-sector policy framing"),
        ("Main lens", "Human rights, democratic values, and inclusive growth"),
        ("Style", "High-level principles"),
    ]
    framework_focus = [
        "Strong emphasis on human rights and democratic values.",
        "Useful as a common policy baseline across jurisdictions.",
        "Less operational detail than engineering or standards-based frameworks.",
    ]
elif framework.startswith("NIST"):
    framework_title = "NIST AI RMF"
    framework_kicker = "Engineering and risk management"
    framework_summary = (
        "NIST translates trustworthiness into operational characteristics and risk-management activities that teams can build into development and deployment."
    )
    framework_meta = [
        ("Best for", "Operational governance and technical risk management"),
        ("Main lens", "Measurable trust characteristics and lifecycle controls"),
        ("Style", "Practical and implementation-oriented"),
    ]
    framework_focus = [
        "Frames trustworthiness in operational terms such as valid, safe, explainable, and resilient.",
        "Useful for teams that need a working risk-management process.",
        "Feels closer to engineering practice than broad policy language.",
    ]
else:
    framework_title = "ISO/IEC standards"
    framework_kicker = "Management system and auditability"
    framework_summary = (
        "ISO/IEC standards focus on making trustworthiness systematic, auditable, and repeatable through governance processes, controls, and documentation."
    )
    framework_meta = [
        ("Best for", "Organizations building formal management systems"),
        ("Main lens", "Governance, process, and audit readiness"),
        ("Style", "Standards-based and repeatable"),
    ]
    framework_focus = [
        "Useful when the goal is structured governance rather than principles alone.",
        "Emphasizes documentation, monitoring, and management-system discipline.",
        "Helps organizations turn trust goals into auditable processes.",
    ]

focus_html = "".join(
    f"""
    <div class="framework-focus-item">
      <span class="framework-focus-dot"></span>
      <div class="framework-focus-copy">{item}</div>
    </div>
    """
    for item in framework_focus
)
meta_html = "".join(
    f"""
    <div class="framework-meta">
      <div class="framework-meta-label">{label}</div>
      <div class="framework-meta-value">{value}</div>
    </div>
    """
    for label, value in framework_meta
)

st.markdown(
    f"""
    <div class="framework-panel">
      <div class="framework-kicker">{framework_kicker}</div>
      <div class="framework-title">{framework_title}</div>
      <div class="framework-summary">{framework_summary}</div>
      <div class="framework-meta-grid">{meta_html}</div>
      <div class="framework-focus-grid">{focus_html}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

framework_note_left, framework_note_right = st.columns([1, 1], gap="large")
with framework_note_left:
    st.markdown(
        """
        <div class="card">
          <div class="card-title">What stays the same across all of them</div>
          <div class="card-desc">
            None of these frameworks reduce trustworthiness to model accuracy. They all point back to a mix of
            <strong>technical performance</strong>, <strong>human oversight</strong>, <strong>fairness</strong>,
            <strong>transparency</strong>, and <strong>accountability</strong>.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with framework_note_right:
    st.markdown(
        """
        <div class="card">
          <div class="card-title">How to read the differences</div>
          <div class="card-desc">
            Treat the differences as differences in <strong>emphasis and use case</strong>:
            policy frameworks guide principles, risk frameworks guide operations, and standards guide management systems.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<hr>", unsafe_allow_html=True)

render_section_intro(
    title="References",
    body="Official starting points if you want to see how the major frameworks define the area.",
    icon_name="link",
)

st.markdown(
    """
    <div class="card">
      <ul>
        <li><a href="https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai" target="_blank">EU HLEG (2019) Ethics Guidelines for Trustworthy AI</a></li>
        <li><a href="https://www.oecd.org/en/topics/ai-principles.html" target="_blank">OECD AI Principles</a></li>
        <li><a href="https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/" target="_blank">NIST AI RMF trustworthy characteristics</a></li>
        <li><a href="https://www.iso.org/standard/81230.html" target="_blank">ISO/IEC 42001 AI management system standard</a></li>
      </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("Next step: open the EU AI Act risk categories page or the mini-demo if you want to see the concept applied.")
