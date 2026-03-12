import streamlit as st

from trust_utils import material_icon, render_callout, render_page_header, render_section_intro, setup_page

setup_page("what_is", "What is Trustworthy AI?")

render_page_header(
    title="What is Trustworthy AI?",
  subtitle="A practical, EU-aligned overview for decision makers.",
    icon_name="verified_user",
    accent="#2563eb",
    chips=["Policy-aligned", "Risk-based", "Governance-aware", "Not only accuracy"],
    eyebrow="Foundations",
)

render_callout(
    title="Definition",
  body="Trustworthy AI means AI that is lawful, ethical, and robust enough to use responsibly under real oversight.",
    icon_name="menu_book",
    accent="#1d4ed8",
)

st.markdown("<hr>", unsafe_allow_html=True)

# -------------------------------------------------------
# Why it matters (short, readable)
# -------------------------------------------------------
left, right = st.columns([1.1, 0.9], gap="large")

with left:
    st.markdown("## Why it matters")
    st.markdown(
        """
        <div class="muted">
          AI systems increasingly influence decisions in public services, industry, healthcare, and security.
          Without safeguards, AI can introduce <strong>harm</strong>, <strong>bias</strong>, <strong>opacity</strong>,
          and unclear <strong>responsibility</strong> — which can damage public trust and create legal and reputational risk.
        </div>
        """,
        unsafe_allow_html=True,
    )

with right:
    st.markdown("## What it is (and isn’t)")
    st.markdown(
        """
        <div class="card">
          <div class="card-title">""" + material_icon("check_circle", 18, "#16a34a") + """ What it is</div>
          <div class="card-desc">
            A <strong>risk and governance</strong> approach for AI-assisted decisions.
          </div>
        </div>
        <div style="height:10px;"></div>
        <div class="card">
          <div class="card-title">""" + material_icon("cancel", 18, "#dc2626") + """ What it isn’t</div>
          <div class="card-desc">
            Not just “high accuracy”, and not “automation that replaces humans”.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<hr>", unsafe_allow_html=True)

# -------------------------------------------------------
# Core recurring dimensions (7 themes)
# -------------------------------------------------------
render_section_intro(
    title="Core dimensions that appear across major frameworks",
  body="Different frameworks use different labels, but they point to the same core ideas.",
    icon_name="view_carousel",
)

dims = [
    ("Technical robustness & reliability", "Consistent performance; resilience to errors and changing conditions."),
    ("Safety & risk mitigation", "Failures do not create harm; uncertain cases are controlled and reviewed."),
    ("Fairness & non-discrimination", "Avoids unjustified disparities across individuals or groups."),
    ("Transparency & explainability", "Practical explanations and traceability of outcomes and processes."),
    ("Accountability & governance", "Clear responsibility, oversight, auditability, and decision ownership."),
    ("Privacy & data governance", "Responsible data handling, protection, quality, and lifecycle governance."),
    ("Societal & environmental impact", "Consider broader impacts on society, institutions, and sustainability."),
]

c1, c2 = st.columns(2, gap="large")
for i, (title, desc) in enumerate(dims):
    target = c1 if i < 4 else c2
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

# -------------------------------------------------------
# EU 7 requirements (explicit, readable list)
# -------------------------------------------------------
render_section_intro(
    title="EU perspective: 7 key requirements",
  body="The EU High-Level Expert Group set out seven requirements that still shape European policy discussions.",
    icon_name="fact_check",
)

eu7 = [
    ("1) Human agency & oversight", "AI should support human decision-making with appropriate oversight and ability to intervene."),
    ("2) Technical robustness & safety", "Systems should be resilient, reliable, secure, and safe across expected and unexpected conditions."),
    ("3) Privacy & data governance", "Strong data protection, quality, integrity, access control, and responsible data management."),
    ("4) Transparency", "Traceability and appropriate explainability; clarity about when AI is used."),
    ("5) Diversity, non-discrimination & fairness", "Avoid unfair bias; ensure accessibility and equitable outcomes."),
    ("6) Societal & environmental well-being", "Consider impacts on society, institutions, democracy, and sustainability."),
    ("7) Accountability", "Clear responsibility, auditability, governance, and mechanisms for redress."),
]

for title, desc in eu7:
    st.markdown(
        f"""
        <div class="card">
          <div class="card-title">{title}</div>
          <div class="card-desc">{desc}</div>
        </div>
        <div style="height:8px;"></div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<hr>", unsafe_allow_html=True)

# -------------------------------------------------------
# Interactive: “Different organizations group it differently”
# -------------------------------------------------------
render_section_intro(
    title="How different organizations structure Trustworthy AI",
  body="There is no single pillar set. Organizations group the same ideas differently depending on their focus.",
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
            Policy-oriented structure that explicitly includes <strong>human oversight</strong>,
            <strong>privacy/data governance</strong>, and <strong>societal well-being</strong> alongside
            robustness, fairness, transparency, and accountability.
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
            Intergovernmental principles emphasizing <strong>human rights and democratic values</strong>,
            <strong>transparency</strong>, <strong>robustness/safety</strong>, and <strong>accountability</strong>.
            Often used as a policy baseline across countries.
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
            Engineering and risk-management oriented. Focuses on measurable characteristics such as
            <strong>valid/reliable</strong>, <strong>safe/secure/resilient</strong>,
            <strong>explainable</strong>, <strong>fair</strong>, <strong>privacy-enhanced</strong>,
            and <strong>accountable/transparent</strong>.
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
            Standards focus on making trustworthiness <strong>operational and auditable</strong>:
            management systems, governance, documentation, monitoring, and risk processes.
            They help organizations implement Trustworthy AI practices systematically.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<hr>", unsafe_allow_html=True)

# -------------------------------------------------------
# References (clean)
# -------------------------------------------------------
st.markdown("## References (official sources)")
st.markdown(
    """
    <div class="mini">
      EU HLEG (2019): https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai<br>
      OECD AI Principles: https://www.oecd.org/en/topics/ai-principles.html<br>
      NIST AI RMF (trustworthy characteristics): https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/<br>
      ISO/IEC 42001 (AI management system): https://www.iso.org/standard/81230.html
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("Next step: open the Interactive mini-demo for a concrete example.")
