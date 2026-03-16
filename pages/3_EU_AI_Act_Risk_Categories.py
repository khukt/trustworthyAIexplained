import streamlit as st

from trust_utils import render_callout, render_page_header, render_section_intro, setup_page


setup_page("risk", "EU AI Act – Risk Categories")

render_page_header(
    title="EU AI Act – Risk-Based Approach",
    subtitle="The EU AI Act does not treat all AI systems the same. Obligations become stricter as the potential harm rises.",
    icon_name="policy",
    accent="#7c3aed",
    chips=["Unacceptable", "High risk", "Limited risk", "Minimal risk"],
    eyebrow="Regulatory lens",
)

render_callout(
    title="Core idea",
    body="The AI Act is built around one principle: higher potential harm means stronger restrictions, obligations, and scrutiny.",
    icon_name="scale",
    accent="#7c3aed",
)

st.markdown("<hr>", unsafe_allow_html=True)

render_section_intro(
    title="Read the regulation as a risk ladder",
    body="The key question is not simply whether a system uses AI. It is how much harm it could create for safety, rights, or public interests.",
    icon_name="stairs",
)

ladder_left, ladder_right = st.columns([0.95, 1.05], gap="large")

with ladder_left:
    st.markdown(
        """
        <div class="card">
          <div class="card-title">How the logic works</div>
          <div class="risk-ladder">
            <div class="risk-ladder-item">
              <div class="risk-ladder-number">1</div>
              <div>
                <div class="risk-ladder-title">If the use is unacceptable, it is prohibited</div>
                <div class="risk-ladder-copy">Some practices are considered too harmful to allow, subject to limited exceptions set out in the Act.</div>
              </div>
            </div>
            <div class="risk-ladder-item">
              <div class="risk-ladder-number">2</div>
              <div>
                <div class="risk-ladder-title">If the use is high-risk, strong obligations apply</div>
                <div class="risk-ladder-copy">Systems affecting safety or fundamental rights face detailed requirements before and after deployment.</div>
              </div>
            </div>
            <div class="risk-ladder-item">
              <div class="risk-ladder-number">3</div>
              <div>
                <div class="risk-ladder-title">If the use is lower risk, transparency may be enough</div>
                <div class="risk-ladder-copy">Some systems mainly trigger duties to inform users that AI is involved or that content is AI-generated.</div>
              </div>
            </div>
            <div class="risk-ladder-item">
              <div class="risk-ladder-number">4</div>
              <div>
                <div class="risk-ladder-title">If the use is minimal risk, there is little extra burden</div>
                <div class="risk-ladder-copy">Many ordinary AI uses face no major new AI Act obligations beyond other applicable law.</div>
              </div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with ladder_right:
    st.markdown(
        """
        <div class="card">
          <div class="card-title">What changes as risk rises</div>
          <ul>
            <li><strong>More documentation</strong> about how the system works and how it is governed.</li>
            <li><strong>More oversight</strong> over how people use, review, and intervene in AI-supported decisions.</li>
            <li><strong>More monitoring</strong> before and after deployment, especially for safety and rights impacts.</li>
            <li><strong>Stronger accountability</strong> for providers, deployers, and others in the lifecycle.</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<hr>", unsafe_allow_html=True)

render_section_intro(
    title="The four risk categories",
    body="This is the practical summary most readers need: what category means what, and what it changes in practice.",
    icon_name="category",
)

tier_a, tier_b = st.columns(2, gap="large")

with tier_a:
    st.markdown(
        """
        <div class="risk-tier">
          <div class="risk-tier-badge risk-tier-red">Unacceptable risk</div>
          <div class="risk-tier-title">Prohibited AI practices</div>
          <div class="risk-tier-copy">
            These uses are considered too harmful to safety, rights, or democratic values and are banned, subject to specific exceptions in the Act.
          </div>
          <ul>
            <li>Social scoring by public authorities</li>
            <li>Certain manipulative or exploitative practices</li>
            <li>Certain uses of real-time remote biometric identification, with narrow exceptions</li>
          </ul>
        </div>
        <div style="height:12px;"></div>
        <div class="risk-tier">
          <div class="risk-tier-badge risk-tier-yellow">Limited risk</div>
          <div class="risk-tier-title">Transparency duties</div>
          <div class="risk-tier-copy">
            The main obligation is to make the AI involvement visible enough for people to understand what they are interacting with.
          </div>
          <ul>
            <li>People may need to be informed that they are interacting with AI</li>
            <li>Some AI-generated or AI-manipulated content must be identifiable</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with tier_b:
    st.markdown(
        """
        <div class="risk-tier">
          <div class="risk-tier-badge risk-tier-orange">High risk</div>
          <div class="risk-tier-title">Strict obligations before and after deployment</div>
          <div class="risk-tier-copy">
            High-risk systems can materially affect safety or fundamental rights, so they face the strongest ongoing compliance duties short of prohibition.
          </div>
          <ul>
            <li>Risk management and governance controls</li>
            <li>Data governance and technical documentation</li>
            <li>Human oversight, logging, and post-market monitoring</li>
          </ul>
        </div>
        <div style="height:12px;"></div>
        <div class="risk-tier">
          <div class="risk-tier-badge risk-tier-green">Minimal risk</div>
          <div class="risk-tier-title">Little or no extra AI Act burden</div>
          <div class="risk-tier-copy">
            Many everyday AI uses fall here. They may still be affected by other law, but the AI Act itself adds little extra burden.
          </div>
          <ul>
            <li>Common low-stakes recommender systems</li>
            <li>Spam filters and similar background tools</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<hr>", unsafe_allow_html=True)

render_section_intro(
    title="What high-risk status usually means in practice",
    body="For most organizations, this is the category that changes day-to-day work the most.",
    icon_name="shield",
    accent="#ea580c",
)

obligation_1, obligation_2, obligation_3 = st.columns(3, gap="large")
for column, title, copy in [
    (
        obligation_1,
        "Before deployment",
        "You need clearer documentation, governance, testing, and defined responsibilities before the system goes live.",
    ),
    (
        obligation_2,
        "During use",
        "Human oversight, logging, and instructions for use matter because the system cannot be treated like a black box.",
    ),
    (
        obligation_3,
        "After deployment",
        "Monitoring, incident handling, and updates remain part of compliance after launch, not only before it.",
    ),
]:
    with column:
        st.markdown(
            f"""
            <div class="obligation-card">
              <div class="obligation-title">{title}</div>
              <div class="obligation-copy">{copy}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(
    """
    <div class="section-note">
      This page is a practical overview, not a substitute for the legal text. Exact obligations depend on the specific system, role, and AI Act provisions involved.
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption(
    "Official source: Regulation (EU) 2024/1689 (AI Act), EUR-Lex: "
    "https://eur-lex.europa.eu/eli/reg/2024/1689/oj"
)
