import streamlit as st
from trust_utils import render_callout, render_page_header, render_section_intro, setup_page

setup_page("risk", "EU AI Act – Risk Categories")

render_page_header(
    title="EU AI Act – Risk-Based Approach",
  subtitle="The AI Act applies stricter rules as the potential harm rises.",
    icon_name="policy",
    accent="#7c3aed",
    chips=["Unacceptable", "High risk", "Limited risk", "Minimal risk"],
    eyebrow="Regulatory lens",
)

render_callout(
    title="Key idea",
  body="More risk means more legal obligations.",
    icon_name="scale",
    accent="#7c3aed",
)

st.markdown("<hr>", unsafe_allow_html=True)

render_section_intro(
  title="The four risk categories",
  body="The AI Act groups AI systems by the level of harm they could cause.",
  icon_name="category",
)

# -----------------------------------------------------------------------------
# Risk Category Cards
# -----------------------------------------------------------------------------

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown(
        """
        <div class="card">
          <div class="risk-badge red">Unacceptable Risk</div>
          <div class="card-title">Prohibited AI Practices (Article 5)</div>
          <p>
            These uses are banned because they pose a clear threat to safety, rights, or democratic values.
          </p>
          <ul>
            <li>Social scoring by public authorities</li>
            <li>Certain manipulative or exploitative systems</li>
            <li>Real-time remote biometric identification (with narrow exceptions)</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="card">
          <div class="risk-badge yellow">Limited Risk</div>
          <div class="card-title">Transparency Obligations</div>
          <p>
            These systems must tell people when AI is involved.
          </p>
          <ul>
            <li>Users must be informed they are interacting with AI</li>
            <li>AI-generated content must be identifiable</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="card">
          <div class="risk-badge orange">High Risk</div>
          <div class="card-title">High-Risk AI Systems (Title III)</div>
          <p>
            These systems can materially affect safety or rights, so they face strict requirements.
          </p>
          <ul>
            <li>Risk management systems</li>
            <li>Data governance and quality</li>
            <li>Technical documentation</li>
            <li>Human oversight</li>
            <li>Post-market monitoring</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="card">
          <div class="risk-badge green">Minimal Risk</div>
          <div class="card-title">Minimal or No Regulatory Burden</div>
          <p>
            These systems face little or no extra regulatory burden.
          </p>
          <ul>
            <li>Recommender systems (e.g., entertainment)</li>
            <li>Spam filters</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<hr>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Key Message
# -----------------------------------------------------------------------------
st.markdown(
    """
    <div class="card">
      <div class="card-title">Key Regulatory Principle</div>
      <p>
        Higher impact means stricter obligations.
      </p>
      <p class="muted">
        Compliance effort rises with societal impact.
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption(
    "Official source: Regulation (EU) 2024/1689 (AI Act), EUR-Lex: "
    "https://eur-lex.europa.eu/eli/reg/2024/1689/oj"
)
