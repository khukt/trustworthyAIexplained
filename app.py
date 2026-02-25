import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="Trustworthy AI Explained",
    page_icon="🤖",
    layout="wide",
)

# ── Global custom CSS ────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    /* Page background */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    }
    [data-testid="stSidebar"] {
        background: #1e293b;
    }
    /* Metric cards */
    [data-testid="metric-container"] {
        background: #1e3a5f;
        border: 1px solid #2563eb;
        border-radius: 10px;
        padding: 12px;
    }
    /* Expanders */
    details summary {
        font-size: 1.05rem;
        font-weight: 600;
    }
    /* Headings colour */
    h1, h2, h3 { color: #93c5fd !important; }
    /* Info / success / warning / error boxes */
    .stAlert { border-radius: 10px; }
    /* Divider */
    hr { border-color: #334155; }
    /* Pillar cards */
    .pillar-card {
        background: #1e3a5f;
        border: 1px solid #2563eb;
        border-radius: 12px;
        padding: 18px 16px;
        text-align: center;
        height: 100%;
    }
    .pillar-card h3 { color: #93c5fd !important; margin-bottom: 6px; }
    .pillar-card p { color: #cbd5e1; font-size: 0.9rem; margin: 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Hero ─────────────────────────────────────────────────────────────────────
col_hero, col_chart = st.columns([1.1, 1], gap="large")

with col_hero:
    st.markdown(
        """
        <h1 style='font-size:2.6rem; color:#93c5fd;'>🤖 Trustworthy AI — Explained</h1>
        <p style='font-size:1.2rem; color:#94a3b8;'>An interactive overview for decision-makers</p>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div style='background:#1e3a5f; border-left:4px solid #2563eb;
                    border-radius:8px; padding:16px 20px; margin:16px 0;'>
        <p style='color:#cbd5e1; font-size:1rem; margin:0;'>
        <em>"We don't need perfect AI.<br>
        We need AI that fails safely, is reviewable, is governed,
        and earns public trust."</em>
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 📌 Navigate the topics")
    nav_items = [
        ("1️⃣", "What is Trustworthy AI?", "The five key qualities"),
        ("2️⃣", "Why should we care?", "Public safety, economics and trust"),
        ("3️⃣", "Interactive mini-demo", "See how safeguards change risk"),
        ("4️⃣", "Failure stories", "Real examples of what goes wrong"),
        ("5️⃣", "Roadmap", "Practical steps to get started"),
    ]
    for icon, title, desc in nav_items:
        st.markdown(
            f"<div style='display:flex; align-items:center; gap:10px; "
            f"margin:6px 0; padding:8px 12px; background:#1e293b; "
            f"border-radius:8px; border:1px solid #334155;'>"
            f"<span style='font-size:1.3rem;'>{icon}</span>"
            f"<div><strong style='color:#e2e8f0;'>{title}</strong> "
            f"<span style='color:#64748b; font-size:0.85rem;'>— {desc}</span></div>"
            f"</div>",
            unsafe_allow_html=True,
        )

with col_chart:
    # Radar chart of the 5 Trustworthy AI pillars
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
    fig.add_trace(go.Scatterpolar(
        r=[0.45, 0.30, 0.35, 0.40, 0.28],
        theta=categories,
        fill="toself",
        name="Without safeguards",
        line_color="#ef4444",
        fillcolor="rgba(239,68,68,0.15)",
    ))
    fig.update_layout(
        polar=dict(
            bgcolor="#0f172a",
            radialaxis=dict(visible=True, range=[0, 1], color="#64748b"),
            angularaxis=dict(color="#94a3b8"),
        ),
        paper_bgcolor="#1e293b",
        plot_bgcolor="#1e293b",
        legend=dict(font=dict(color="#cbd5e1"), bgcolor="#1e293b"),
        margin=dict(l=40, r=40, t=40, b=40),
        title=dict(text="Trustworthy AI: Five Pillars", font=dict(color="#93c5fd", size=16)),
    )
    st.plotly_chart(fig, use_container_width=True)
