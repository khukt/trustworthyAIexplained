import streamlit as st

st.set_page_config(page_title="EU AI Act – Risk Categories", page_icon="🇪🇺", layout="wide")

# --- Clean, readable styling ---
st.markdown(
    """
    <style>
      .stApp { background:#ffffff; }
      h1, h2, h3 { color:#0f172a; }
      p, li { color:#111827; font-size:1.02rem; line-height:1.6; }
      .muted { color:#475569; }
      .hero {
        border:1px solid #e5e7eb; border-radius:14px;
        padding:18px; background:linear-gradient(180deg,#ffffff,#f8fafc);
      }
      .card {
        border:1px solid #e5e7eb;
        border-radius:12px;
        padding:14px;
        background:#ffffff;
        margin-bottom:12px;
      }
      .card-title {
        font-weight:750;
        font-size:1.1rem;
        margin-bottom:6px;
      }
      .risk-badge {
        display:inline-block;
        padding:5px 10px;
        border-radius:999px;
        font-size:0.85rem;
        margin-bottom:8px;
      }
      .red { background:#fee2e2; color:#991b1b; border:1px solid #fecaca; }
      .orange { background:#ffedd5; color:#9a3412; border:1px solid #fed7aa; }
      .yellow { background:#fef9c3; color:#854d0e; border:1px solid #fde68a; }
      .green { background:#dcfce7; color:#166534; border:1px solid #bbf7d0; }
      hr { border:none; height:1px; background:#e5e7eb; margin:18px 0; }
      a { color:#1d4ed8; text-decoration:none; }
      a:hover { text-decoration:underline; }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# Header
# -----------------------------------------------------------------------------
st.markdown(
    """
    <div class="hero">
      <h1>🇪🇺 EU AI Act – Risk-Based Approach</h1>
      <p class="muted">
        Regulation (EU) 2024/1689 establishes a <strong>risk-based regulatory framework</strong>
        for AI systems within the European Union.
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("## The Four Risk Categories")

st.markdown(
    '<p class="muted">The AI Act classifies AI systems according to the level of risk they pose to safety, fundamental rights, and EU values.</p>',
    unsafe_allow_html=True,
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
            AI systems that pose a clear threat to safety, fundamental rights,
            or democratic values are prohibited within the EU.
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
            AI systems that interact with humans must meet specific transparency requirements.
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
            AI systems that may significantly affect safety or fundamental rights
            are subject to strict regulatory requirements.
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
            AI systems with minimal impact remain largely unregulated.
            The Act encourages innovation in this category.
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
        The higher the potential impact on safety or fundamental rights,
        the stricter the regulatory obligations.
      </p>
      <p class="muted">
        This risk-based structure aligns compliance effort with societal impact.
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption(
    "Official source: Regulation (EU) 2024/1689 (AI Act), EUR-Lex: "
    "https://eur-lex.europa.eu/eli/reg/2024/1689/oj"
)
