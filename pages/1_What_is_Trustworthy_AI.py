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
        <div style="height:10px;"></div>
        <div class="card">
          <div class="card-title">""" + material_icon("person_search", 18, "#2563eb") + """ Why the term exists</div>
          <div class="card-desc">
            It gives leaders a way to talk about <strong>safety, fairness, transparency, oversight, and responsibility</strong> in one frame.
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
        <div class="card">
          <div class="card-title">Common pattern across frameworks</div>
          <ul>
            <li>Systems should be reliable and safe enough for their context.</li>
            <li>People should be treated fairly and be able to understand the role of AI.</li>
            <li>Organizations should keep clear oversight, accountability, and documentation.</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with eu_right:
    st.markdown(
        """
        <div class="card">
          <div class="card-title">EU emphasis</div>
          <ul>
            <li><strong>Human agency and oversight</strong> are explicit, not assumed.</li>
            <li><strong>Privacy and data governance</strong> are treated as core trust issues.</li>
            <li><strong>Societal impact</strong> matters alongside technical performance.</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div class="card">
      <div class="card-title">EU High-Level Expert Group: 7 requirements</div>
      <div class="card-desc">
        The HLEG framework names seven requirements: human agency and oversight; technical robustness and safety; privacy and data governance;
        transparency; diversity, non-discrimination and fairness; societal and environmental well-being; and accountability.
        The exact labels vary across frameworks, but the underlying message is consistent: trustworthy AI is <strong>not only a technical question</strong>.
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<hr>", unsafe_allow_html=True)

render_section_intro(
    title="How major organizations group the same idea",
    body="There is no single official pillar set. The differences are usually about emphasis, not about a completely different definition.",
    icon_name="hub",
)

framework = st.selectbox(
    "Choose a framework:",
    [
        "EU (HLEG 2019) — 7 requirements",
        "OECD — AI Principles",
        "NIST — AI Risk Management Framework",
        "ISO/IEC — standards (management system + risk)",
    ],
)

if framework.startswith("EU"):
    st.markdown(
        """
        <div class="card">
          <div class="card-title">EU (HLEG 2019)</div>
          <div class="card-desc">
            A policy-oriented structure that explicitly combines <strong>human oversight</strong>, <strong>data governance</strong>,
            <strong>societal impact</strong>, and the more familiar themes of robustness, fairness, transparency, and accountability.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
elif framework.startswith("OECD"):
    st.markdown(
        """
        <div class="card">
          <div class="card-title">OECD AI Principles</div>
          <div class="card-desc">
            A high-level international policy frame centered on <strong>inclusive growth</strong>, <strong>human rights and democratic values</strong>,
            <strong>transparency</strong>, <strong>robustness</strong>, and <strong>accountability</strong>.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
elif framework.startswith("NIST"):
    st.markdown(
        """
        <div class="card">
          <div class="card-title">NIST AI RMF</div>
          <div class="card-desc">
            An engineering and risk-management frame that translates trustworthiness into operational characteristics such as
            <strong>valid and reliable</strong>, <strong>safe</strong>, <strong>secure and resilient</strong>, <strong>explainable</strong>,
            <strong>privacy-enhanced</strong>, <strong>fair</strong>, and <strong>accountable</strong>.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <div class="card">
          <div class="card-title">ISO/IEC standards</div>
          <div class="card-desc">
            A standards-based view focused on making trustworthiness <strong>auditable and repeatable</strong> through management systems,
            documentation, governance processes, monitoring, and risk controls.
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
