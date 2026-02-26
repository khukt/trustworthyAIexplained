import streamlit as st
import plotly.graph_objects as go
from trust_utils import apply_dark_theme

st.set_page_config(
    page_title="Trustworthy AI Explained",
    page_icon="🤖",
    layout="wide",
)


# -----------------------------------------------------------------------------
# SIDEBAR NAV (story-first)
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("## 🧭 Start here (recommended order)")
    st.caption("A short flow built for decision-makers.")

    st.page_link("app.py", label="Home", icon="🏠")

    st.page_link("pages/1_What_is_Trustworthy_AI.py", label="1) What is Trustworthy AI?", icon="🛡️")
    st.page_link("pages/2_Why_should_we_care.py", label="2) Why it matters", icon="⚠️")

    # Add this page when you create it (recommended)
    st.page_link("pages/3_EU_AI_Act_Risk_Categories.py", label="3) EU AI Act: Risk categories", icon="🇪🇺")

    # Shift numbering of existing pages OR keep file names and just link them in this order
    st.page_link("pages/3_Interactive_mini_demo.py", label="4) Interactive mini-demo", icon="🎛️")
    st.page_link("pages/4_Failure_stories.py", label="5) Failure stories", icon="📖")
    st.page_link("pages/5_Roadmap.py", label="6) Roadmap", icon="🧩")

    st.divider()
    st.markdown("### Quick jump")
    st.page_link("pages/3_Interactive_mini_demo.py", label="Show the demo now", icon="▶️")


# -----------------------------------------------------------------------------
# HOME HERO
# -----------------------------------------------------------------------------
col_hero, col_chart = st.columns([1.1, 1], gap="large")

with col_hero:
    st.markdown(
        """
        <h1 style='font-size:2.6rem; color:#0f172a;'>🤖 Trustworthy AI — Explained</h1>
        <p style='font-size:1.1rem; color:#475569;'>
          An interactive overview for decision-makers: risks → regulation → safeguards → action
        </p>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style='background:#f8fafc; border:1px solid #e5e7eb; border-radius:12px;
                    padding:14px 16px; margin:14px 0;'>
          <div style='color:#0f172a; font-weight:750; margin-bottom:6px;'>How to use this demo</div>
          <div style='color:#475569; line-height:1.55;'>
            Start with <strong>What it is</strong>, then <strong>Why it matters</strong>.
            If you need one powerful moment, open the <strong>Interactive mini-demo</strong>.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 📌 Recommended flow (click to open)")
    cards = [
        ("🛡️", "What is Trustworthy AI?", "Definition + how major frameworks describe it", "pages/1_What_is_Trustworthy_AI.py"),
        ("⚠️", "Why it matters", "Harm, trust, budgets + EU AI Act fines (Article 99)", "pages/2_Why_should_we_care.py"),
        ("🇪🇺", "EU AI Act risk categories", "How the EU classifies AI risk (Unacceptable → Minimal)", "pages/3_EU_AI_Act_Risk_Categories.py"),
        ("🎛️", "Interactive mini-demo", "See how safeguards change outcomes", "pages/3_Interactive_mini_demo.py"),
        ("📖", "Failure stories", "Concrete examples of what goes wrong without safeguards", "pages/4_Failure_stories.py"),
        ("🧩", "Roadmap", "What leaders can require (minimum)", "pages/5_Roadmap.py"),
    ]

    for icon, title, desc, path in cards:
        st.markdown(
            f"""
            <div style="border:1px solid #e5e7eb; border-radius:12px; padding:12px 14px;
                        background:#ffffff; margin:8px 0;">
              <div style="display:flex; align-items:center; justify-content:space-between;">
                <div style="display:flex; gap:10px; align-items:flex-start;">
                  <div style="font-size:1.4rem;">{icon}</div>
                  <div>
                    <div style="font-weight:750; color:#0f172a;">{title}</div>
                    <div style="color:#475569; font-size:0.95rem;">{desc}</div>
                  </div>
                </div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.page_link(path, label=f"Open: {title}", icon="➡️")

with col_chart:
    # Keep your radar chart if you still want it on Home (optional)
    categories = ["Reliable", "Safe", "Fair", "Transparent", "Accountable"]
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=[0.9, 0.85, 0.8, 0.88, 0.82],
        theta=categories,
        fill="toself",
        name="Trustworthy AI",
        line_color="#2563eb",
        fillcolor="rgba(37,99,235,0.25)",
    ))
    fig.update_layout(
        polar=dict(bgcolor="#f8fafc", radialaxis=dict(visible=True, range=[0, 1])),
        paper_bgcolor="#ffffff",
        margin=dict(l=40, r=40, t=40, b=40),
        title=dict(text="Trustworthy AI (quick view)", font=dict(color="#0f172a", size=16)),
    )
    st.plotly_chart(fig, use_container_width=True)
