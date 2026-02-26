import streamlit as st

# -------------------------------------------------------
# Modern + clean + formal (Style B) — high readability
# -------------------------------------------------------
st.set_page_config(page_title="What is Trustworthy AI?", page_icon="🛡️", layout="wide")

# Global styling (light, high contrast, modern)
st.markdown(
    """
    <style>
      .stApp { background: #ffffff; }
      h1, h2, h3 { color: #0f172a; }
      p, li, div { color: #111827; font-size: 1.02rem; }
      .muted { color: #475569; font-size: 1.0rem; line-height: 1.55; }
      .chip {
        display:inline-block; padding:6px 10px; border-radius:999px;
        background:#eef2ff; border:1px solid #c7d2fe; color:#1e3a8a;
        font-size:0.92rem; margin-right:8px;
      }
      .hero {
        border: 1px solid #e5e7eb; border-radius: 14px; padding: 18px 18px;
        background: linear-gradient(180deg, #ffffff, #f8fafc);
      }
      .callout {
        border-left: 4px solid #1d4ed8;
        background: #eff6ff;
        padding: 12px 14px; border-radius: 10px;
        color: #0f172a;
      }
      .card {
        border: 1px solid #e5e7eb; border-radius: 12px; padding: 12px 14px;
        background: #ffffff;
      }
      .card-title { font-weight: 750; color: #0f172a; margin-bottom: 4px; }
      .card-desc { color: #475569; line-height: 1.5; }
      .section-title { margin-top: 10px; }
      .mini { color:#64748b; font-size:0.95rem; }
      hr { border: none; height: 1px; background: #e5e7eb; margin: 18px 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------------------------------------
# Header / Hero
# -------------------------------------------------------
st.markdown(
    """
    <div class="hero">
      <div style="display:flex; align-items:center; gap:10px;">
        <div style="font-size:1.8rem;">🛡️</div>
        <div>
          <h1 style="margin:0;">What is Trustworthy AI?</h1>
          <div class="muted">
            An academically grounded and EU-aligned overview for decision makers.
          </div>
        </div>
      </div>

      <div style="margin-top:14px;" class="callout">
        <div style="font-size:1.05rem;">
          <strong>Definition:</strong> Trustworthy AI refers to AI systems developed and governed to be
          <strong>lawful</strong>, <strong>ethical</strong>, and <strong>technically robust</strong>,
          so they can be used responsibly in real-world contexts under appropriate oversight.
        </div>
      </div>

      <div style="margin-top:12px;">
        <span class="chip">Policy-aligned</span>
        <span class="chip">Risk-based</span>
        <span class="chip">Governance-aware</span>
        <span class="chip">Not only accuracy</span>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
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
          <div class="card-title">✅ What it is</div>
          <div class="card-desc">
            A <strong>risk and governance</strong> approach for AI-assisted decisions.
          </div>
        </div>
        <div style="height:10px;"></div>
        <div class="card">
          <div class="card-title">❌ What it isn’t</div>
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
st.markdown("## Core dimensions that appear across major frameworks")
st.markdown(
    """
    <div class="muted">
      Different organizations structure Trustworthy AI differently (e.g., EU, OECD, NIST, ISO/IEC, sector frameworks),
      but the following <strong>recurring dimensions</strong> consistently appear.
    </div>
    """,
    unsafe_allow_html=True,
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
st.markdown("## EU perspective: 7 key requirements (Ethics Guidelines for Trustworthy AI, 2019)")
st.markdown(
    """
    <div class="muted">
      The EU High-Level Expert Group describes seven requirements for Trustworthy AI.
      These are widely cited in European policy discussions.
    </div>
    """,
    unsafe_allow_html=True,
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
st.markdown("## How different organizations structure Trustworthy AI (interactive)")
st.markdown(
    """
    <div class="muted">
      There is <strong>no single universal pillar set</strong>. Organizations group the same core dimensions differently
      depending on whether they focus on policy, engineering risk, or auditable management systems.
    </div>
    """,
    unsafe_allow_html=True,
)

framework = st.selectbox(
    "Select a framework to see its focus (brief, decision-maker friendly):",
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

st.caption("Use the Interactive mini-demo to show concrete examples of risk, bias, transparency, and governance in action.")
