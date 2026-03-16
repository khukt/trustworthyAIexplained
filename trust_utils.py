from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Any, Optional, Sequence
import numpy as np
import pandas as pd
import streamlit as st


PAGE_ICONS = {
    "home": ":material/robot_2:",
    "what_is": ":material/verified_user:",
    "why": ":material/warning:",
    "risk": ":material/policy:",
    "demo": ":material/tune:",
    "stories": ":material/auto_stories:",
    "roadmap": ":material/route:",
}


NAV_ITEMS = [
    ("home", "app.py", "Home"),
    ("what_is", "pages/1_What_is_Trustworthy_AI.py", "1) What is Trustworthy AI?"),
    ("why", "pages/2_Why_should_we_care.py", "2) Why it matters"),
    ("risk", "pages/3_EU_AI_Act_Risk_Categories.py", "3) EU AI Act risk categories"),
    ("demo", "pages/3_Interactive_mini_demo.py", "4) Interactive mini-demo"),
    ("stories", "pages/4_Failure_stories.py", "5) Failure stories"),
    ("roadmap", "pages/5_Roadmap.py", "6) Roadmap"),
]


NAV_GROUPS = [
    ("Overview", ["home"]),
    ("Core brief", ["what_is", "why", "risk"]),
    ("From risk to action", ["demo", "stories", "roadmap"]),
]


NAV_DETAILS = {
    "home": {
        "summary": "Get the storyline, key themes, and how to use the app.",
        "accent": "#2563eb",
        "eyebrow": "Start",
    },
    "what_is": {
        "summary": "Define trustworthy AI in practical, governance-focused terms.",
        "accent": "#2563eb",
        "eyebrow": "Step 1",
    },
    "why": {
        "summary": "See why leadership, trust, and delivery risk are connected.",
        "accent": "#ea580c",
        "eyebrow": "Step 2",
    },
    "risk": {
        "summary": "Understand the EU AI Act's risk ladder and obligations.",
        "accent": "#7c3aed",
        "eyebrow": "Step 3",
    },
    "demo": {
        "summary": "Test how safeguards change outcomes in one live example.",
        "accent": "#0f766e",
        "eyebrow": "Step 4",
    },
    "stories": {
        "summary": "Review concrete failure patterns and what would have helped.",
        "accent": "#2563eb",
        "eyebrow": "Step 5",
    },
    "roadmap": {
        "summary": "End with a compact action plan for teams and decision-makers.",
        "accent": "#9333ea",
        "eyebrow": "Step 6",
    },
}


def inject_icon_font() -> None:
    """Load Material Symbols for consistent icon rendering in custom HTML."""
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,400,0,0');

        .material-symbols-rounded {
            font-family: 'Material Symbols Rounded';
            font-weight: normal;
            font-style: normal;
            line-height: 1;
            letter-spacing: normal;
            text-transform: none;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            white-space: nowrap;
            word-wrap: normal;
            direction: ltr;
            -webkit-font-feature-settings: 'liga';
            -webkit-font-smoothing: antialiased;
            font-variation-settings: 'FILL' 0, 'wght' 500, 'GRAD' 0, 'opsz' 24;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def material_icon(name: str, size: int = 24, color: str = "currentColor") -> str:
    """Return a Material Symbols icon span for use in custom HTML blocks."""
    return (
        f"<span class='material-symbols-rounded' "
        f"style='font-size:{size}px; color:{color};' aria-hidden='true'>{name}</span>"
    )


def _join_chips(chips: Sequence[str]) -> str:
    return "".join(f"<span class='chip'>{chip}</span>" for chip in chips)


def render_sidebar(active_page: str) -> None:
    """Render the shared story-first sidebar navigation."""
    nav_lookup = {key: (path, label) for key, path, label in NAV_ITEMS}
    story_keys = [key for key, _, _ in NAV_ITEMS if key != "home"]
    total_steps = len(story_keys)
    current_step = story_keys.index(active_page) + 1 if active_page in story_keys else 0
    progress = current_step / total_steps if total_steps else 0
    _, current_label = nav_lookup.get(active_page, ("", "Current page"))
    current_details = NAV_DETAILS.get(active_page, {})
    next_item = None
    if active_page == "home" and story_keys:
        next_key = story_keys[0]
        next_path, next_label = nav_lookup[next_key]
        next_item = (next_key, next_path, next_label)
    elif 0 < current_step < total_steps:
        next_key = story_keys[current_step]
        next_path, next_label = nav_lookup[next_key]
        next_item = (next_key, next_path, next_label)

    with st.sidebar:
        st.markdown(
            f"<div class='sidebar-hero'>"
            f"<div class='sidebar-eyebrow'>Navigator</div>"
            f"<div class='sidebar-title'>{material_icon('explore', 20, '#1d4ed8')} Trustworthy AI Explained</div>"
            f"<div class='sidebar-copy'>Move from the core idea to the action plan in one guided pass.</div>"
            f"<div class='sidebar-progress-row'>"
            f"<span class='sidebar-pill'>{current_details.get('eyebrow', 'Overview')}</span>"
            f"<span class='sidebar-pill sidebar-pill-muted'>{current_step}/{total_steps} story steps</span>"
            f"</div>"
            f"<div class='sidebar-progress-track'><span style='width:{progress * 100:.0f}%;'></span></div>"
            f"</div>",
            unsafe_allow_html=True,
        )

        for group_title, group_keys in NAV_GROUPS:
            st.markdown(f"<div class='sidebar-group-label'>{group_title}</div>", unsafe_allow_html=True)
            for key in group_keys:
                path, label = nav_lookup[key]
                details = NAV_DETAILS.get(key, {})
                step_copy = details.get("eyebrow", "Overview")
                if key != "home":
                    step_copy = f"{step_copy} of {total_steps}"
                st.page_link(path, label=label, icon=PAGE_ICONS[key])
                st.markdown(
                    (
                        f"<div class='sidebar-link-meta{' sidebar-link-meta-active' if key == active_page else ''}'>"
                        f"<span class='sidebar-link-kicker'>{step_copy}</span>"
                        f"<span>{details.get('summary', '')}</span>"
                        f"</div>"
                    ),
                    unsafe_allow_html=True,
                )

        st.markdown(
            f"<div class='sidebar-note'>"
            f"<div class='sidebar-note-title'>{material_icon('flag', 16, current_details.get('accent', '#0f172a'))} Current focus</div>"
            f"<div class='sidebar-note-copy'>{current_label}</div>"
            f"<div class='sidebar-note-subcopy'>{current_details.get('summary', 'Use the menu to move through the story.')}</div>"
            f"</div>",
            unsafe_allow_html=True,
        )
        if next_item:
            next_key, next_path, next_label = next_item
            st.markdown("<div class='sidebar-group-label'>Recommended next</div>", unsafe_allow_html=True)
            st.markdown(
                (
                    "<div class='sidebar-link-meta sidebar-link-meta-next'>"
                    f"<span class='sidebar-link-kicker'>{next_label}</span>"
                    f"<span>{NAV_DETAILS[next_key]['eyebrow']}</span><br>"
                    f"<span>{NAV_DETAILS[next_key]['summary']}</span>"
                    "</div>"
                ),
                unsafe_allow_html=True,
            )


def inject_global_styles() -> None:
    """Inject the shared visual design system used across pages."""
    st.markdown(
        """
        <style>
        :root {
            --bg: #f6f8fc;
            --surface: rgba(255, 255, 255, 0.96);
            --surface-strong: #ffffff;
            --border: #d6deeb;
            --text: #0f172a;
            --muted: #475569;
            --accent: #2563eb;
            --shadow: 0 14px 34px rgba(15, 23, 42, 0.07);
        }
        .stApp {
            background:
                radial-gradient(circle at top left, rgba(37, 99, 235, 0.06), transparent 34%),
                linear-gradient(180deg, #f6f8fc 0%, #ffffff 42%, #f8fafc 100%);
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        }
        [data-testid="stAppViewContainer"] {
            background: transparent;
        }
        [data-testid="stSidebarNav"],
        section[data-testid="stSidebarNav"],
        nav[data-testid="stSidebarNav"],
        [data-testid="stSidebarNavItems"],
        [data-testid="stSidebarNavSeparator"] {
            display: none;
        }
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #f8fbff 0%, #f8fafc 100%);
            border-right: 1px solid var(--border);
        }
        .block-container {
            padding-top: 1.15rem;
            padding-bottom: 3rem;
            max-width: 1180px;
        }
        [data-testid="metric-container"] {
            background: rgba(255, 255, 255, 0.95);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 13px;
            box-shadow: 0 8px 20px rgba(15, 23, 42, 0.04);
        }
        h1, h2, h3 {
            color: var(--text) !important;
            letter-spacing: -0.02em;
        }
        p, li, div {
            color: #111827;
        }
        details summary {
            font-size: 1.02rem;
            font-weight: 600;
        }
        .stAlert {
            border-radius: 16px;
        }
        hr {
            border-color: #e2e8f0;
            margin: 1.15rem 0;
        }
        .hero-panel {
            background: linear-gradient(180deg, rgba(255,255,255,0.97), rgba(248,250,252,0.95));
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 20px 22px;
            box-shadow: var(--shadow);
            margin-bottom: 0.35rem;
        }
        .hero-row {
            display: flex;
            align-items: flex-start;
            gap: 14px;
        }
        .hero-icon {
            width: 52px;
            height: 52px;
            border-radius: 16px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background: rgba(37, 99, 235, 0.10);
            flex-shrink: 0;
        }
        .muted {
            color: var(--muted);
            font-size: 1rem;
            line-height: 1.6;
        }
        .hero-panel h1 {
            line-height: 1.08;
            margin-bottom: 0.35rem !important;
        }
        .hero-panel .muted {
            max-width: 60rem;
        }
        .hero-kicker {
            color: var(--muted);
            text-transform: uppercase;
            letter-spacing: 0.08em;
            font-size: 0.78rem;
            font-weight: 700;
            margin-bottom: 6px;
        }
        .chip {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 11px;
            border-radius: 999px;
            background: #eff6ff;
            border: 1px solid #bfdbfe;
            color: #1d4ed8;
            font-size: 0.92rem;
            margin: 7px 7px 0 0;
        }
        .callout {
            border-left: 4px solid var(--accent);
            background: #f1f5ff;
            padding: 12px 14px;
            border-radius: 12px;
            color: var(--text);
            margin: 12px 0 2px;
            box-shadow: 0 6px 16px rgba(37, 99, 235, 0.08);
        }
        .section-intro {
            margin: 0.25rem 0 0.85rem;
        }
        .section-intro h2 {
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 4px;
        }
        .card {
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 15px 16px;
            background: rgba(255,255,255,0.95);
            box-shadow: 0 8px 18px rgba(15, 23, 42, 0.04);
            height: 100%;
        }
        .card-title {
            font-weight: 750;
            color: var(--text);
            margin-bottom: 6px;
        }
        .card-desc {
            color: var(--muted);
            line-height: 1.6;
        }
        .card p:last-child,
        .card ul:last-child {
            margin-bottom: 0;
        }
        .card ul {
            padding-left: 1.1rem;
        }
        .card li + li {
            margin-top: 0.28rem;
        }
        .compare-card {
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 18px 18px;
            background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(248,250,252,0.96));
            box-shadow: 0 10px 22px rgba(15, 23, 42, 0.05);
            height: 100%;
        }
        .compare-card-eu {
            border-color: rgba(196, 181, 253, 0.95);
            background:
                radial-gradient(circle at top right, rgba(124,58,237,0.10), transparent 36%),
                linear-gradient(180deg, rgba(255,255,255,0.98), rgba(250,245,255,0.96));
        }
        .compare-kicker {
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            font-size: 0.72rem;
            font-weight: 800;
            margin-bottom: 0.45rem;
        }
        .compare-card-eu .compare-kicker {
            color: #7c3aed;
        }
        .compare-title {
            color: var(--text);
            font-size: 1.08rem;
            font-weight: 800;
            line-height: 1.35;
            margin-bottom: 0.75rem;
        }
        .compare-list {
            display: grid;
            gap: 0.7rem;
        }
        .compare-item {
            display: flex;
            align-items: flex-start;
            gap: 0.7rem;
        }
        .compare-dot {
            width: 10px;
            height: 10px;
            border-radius: 999px;
            flex-shrink: 0;
            margin-top: 0.38rem;
            background: #2563eb;
        }
        .compare-card-eu .compare-dot {
            background: #7c3aed;
        }
        .compare-copy {
            color: #475569;
            line-height: 1.65;
        }
        .requirement-card {
            border: 1px solid rgba(226, 232, 240, 0.95);
            border-radius: 18px;
            padding: 14px 14px;
            background: rgba(255,255,255,0.96);
            box-shadow: 0 8px 18px rgba(15, 23, 42, 0.04);
            height: 100%;
        }
        .requirement-number {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-width: 30px;
            height: 30px;
            padding: 0 0.45rem;
            border-radius: 999px;
            background: rgba(124, 58, 237, 0.10);
            color: #7c3aed;
            font-size: 0.78rem;
            font-weight: 800;
            margin-bottom: 0.65rem;
        }
        .requirement-title {
            color: var(--text);
            font-size: 1rem;
            font-weight: 800;
            line-height: 1.35;
            margin-bottom: 0.4rem;
        }
        .requirement-copy {
            color: #64748b;
            line-height: 1.6;
            font-size: 0.93rem;
        }
        .section-note {
            border-left: 3px solid #c4b5fd;
            padding: 0.1rem 0 0.1rem 0.9rem;
            color: #475569;
            line-height: 1.65;
            margin-top: 0.8rem;
        }
        .impact-card {
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 18px 18px;
            background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(248,250,252,0.96));
            box-shadow: 0 10px 22px rgba(15, 23, 42, 0.05);
            height: 100%;
        }
        .impact-card-kicker {
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            font-size: 0.72rem;
            font-weight: 800;
            margin-bottom: 0.45rem;
        }
        .impact-card-title {
            color: var(--text);
            font-size: 1.1rem;
            font-weight: 800;
            line-height: 1.35;
            margin-bottom: 0.55rem;
        }
        .impact-card-copy {
            color: #475569;
            line-height: 1.7;
        }
        .risk-chain {
            display: grid;
            gap: 0.75rem;
        }
        .risk-chain-item {
            display: grid;
            grid-template-columns: 34px 1fr;
            gap: 0.8rem;
            align-items: start;
            padding: 0.8rem 0.9rem;
            border-radius: 18px;
            border: 1px solid rgba(226, 232, 240, 0.95);
            background: rgba(255,255,255,0.94);
        }
        .risk-chain-number {
            width: 34px;
            height: 34px;
            border-radius: 999px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background: rgba(234, 88, 12, 0.12);
            color: #c2410c;
            font-size: 0.82rem;
            font-weight: 800;
        }
        .risk-chain-title {
            color: var(--text);
            font-size: 0.98rem;
            font-weight: 800;
            line-height: 1.35;
            margin-bottom: 0.24rem;
        }
        .risk-chain-copy {
            color: #64748b;
            line-height: 1.6;
            font-size: 0.94rem;
        }
        .fine-tier-grid {
            display: grid;
            gap: 0.8rem;
        }
        .fine-tier {
            border: 1px solid rgba(226, 232, 240, 0.95);
            border-radius: 18px;
            padding: 13px 14px;
            background: rgba(255,255,255,0.95);
            box-shadow: 0 8px 18px rgba(15, 23, 42, 0.04);
        }
        .fine-tier-top {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 10px;
            margin-bottom: 0.45rem;
        }
        .fine-tier-title {
            color: var(--text);
            font-size: 0.98rem;
            font-weight: 800;
            line-height: 1.35;
        }
        .fine-tier-value {
            display: inline-flex;
            align-items: center;
            border-radius: 999px;
            padding: 0.24rem 0.62rem;
            background: rgba(254, 226, 226, 0.92);
            border: 1px solid rgba(252, 165, 165, 0.9);
            color: #991b1b;
            font-size: 0.76rem;
            font-weight: 800;
            white-space: nowrap;
        }
        .fine-tier-copy {
            color: #64748b;
            line-height: 1.6;
            font-size: 0.93rem;
        }
        .fine-note {
            border-left: 3px solid #f59e0b;
            padding: 0.1rem 0 0.1rem 0.9rem;
            color: #475569;
            line-height: 1.65;
            margin-top: 0.8rem;
        }
        .checklist-grid {
            display: grid;
            gap: 0.8rem;
        }
        .checklist-item {
            display: grid;
            grid-template-columns: 36px 1fr;
            gap: 0.85rem;
            align-items: start;
            border: 1px solid rgba(226, 232, 240, 0.95);
            border-radius: 18px;
            padding: 0.9rem 1rem;
            background: rgba(255,255,255,0.95);
            box-shadow: 0 8px 18px rgba(15, 23, 42, 0.04);
        }
        .checklist-number {
            width: 36px;
            height: 36px;
            border-radius: 999px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background: rgba(37, 99, 235, 0.1);
            color: #1d4ed8;
            font-size: 0.84rem;
            font-weight: 800;
        }
        .checklist-title {
            color: var(--text);
            font-size: 0.98rem;
            font-weight: 800;
            line-height: 1.35;
            margin-bottom: 0.24rem;
        }
        .checklist-copy {
            color: #64748b;
            line-height: 1.6;
            font-size: 0.94rem;
        }
        .risk-tier {
            border: 1px solid rgba(226, 232, 240, 0.95);
            border-radius: 20px;
            padding: 16px 16px;
            background: rgba(255,255,255,0.96);
            box-shadow: 0 10px 22px rgba(15, 23, 42, 0.05);
            height: 100%;
        }
        .risk-tier-badge {
            display: inline-flex;
            align-items: center;
            border-radius: 999px;
            padding: 0.28rem 0.72rem;
            font-size: 0.76rem;
            font-weight: 800;
            letter-spacing: 0.04em;
            margin-bottom: 0.7rem;
        }
        .risk-tier-red {
            background: rgba(254, 226, 226, 0.96);
            color: #991b1b;
            border: 1px solid rgba(252, 165, 165, 0.9);
        }
        .risk-tier-orange {
            background: rgba(255, 237, 213, 0.96);
            color: #9a3412;
            border: 1px solid rgba(253, 186, 116, 0.92);
        }
        .risk-tier-yellow {
            background: rgba(254, 249, 195, 0.96);
            color: #854d0e;
            border: 1px solid rgba(253, 224, 71, 0.9);
        }
        .risk-tier-green {
            background: rgba(220, 252, 231, 0.96);
            color: #166534;
            border: 1px solid rgba(134, 239, 172, 0.9);
        }
        .risk-tier-title {
            color: var(--text);
            font-size: 1.05rem;
            font-weight: 800;
            line-height: 1.35;
            margin-bottom: 0.45rem;
        }
        .risk-tier-copy {
            color: #475569;
            line-height: 1.65;
            margin-bottom: 0.7rem;
        }
        .risk-tier ul {
            margin: 0;
            padding-left: 1.1rem;
            color: #64748b;
            line-height: 1.65;
        }
        .risk-ladder {
            display: grid;
            gap: 0.8rem;
        }
        .risk-ladder-item {
            display: grid;
            grid-template-columns: 40px 1fr;
            gap: 0.9rem;
            align-items: start;
            border: 1px solid rgba(226, 232, 240, 0.95);
            border-radius: 18px;
            padding: 0.9rem 1rem;
            background: rgba(255,255,255,0.95);
        }
        .risk-ladder-number {
            width: 40px;
            height: 40px;
            border-radius: 999px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background: rgba(124, 58, 237, 0.10);
            color: #7c3aed;
            font-size: 0.86rem;
            font-weight: 800;
        }
        .risk-ladder-title {
            color: var(--text);
            font-size: 1rem;
            font-weight: 800;
            line-height: 1.35;
            margin-bottom: 0.24rem;
        }
        .risk-ladder-copy {
            color: #64748b;
            line-height: 1.6;
            font-size: 0.94rem;
        }
        .obligation-card {
            border: 1px solid rgba(226, 232, 240, 0.95);
            border-radius: 18px;
            padding: 14px 14px;
            background: rgba(255,255,255,0.96);
            box-shadow: 0 8px 18px rgba(15, 23, 42, 0.04);
            height: 100%;
        }
        .obligation-title {
            color: var(--text);
            font-size: 1rem;
            font-weight: 800;
            line-height: 1.35;
            margin-bottom: 0.35rem;
        }
        .obligation-copy {
            color: #64748b;
            line-height: 1.6;
            font-size: 0.94rem;
        }
        .failure-story-card {
            border: 1px solid rgba(203, 213, 225, 0.95);
            border-radius: 22px;
            padding: 18px 18px;
            background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(248,250,252,0.96));
            box-shadow: 0 12px 24px rgba(15, 23, 42, 0.05);
            height: 100%;
        }
        .failure-story-kicker {
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            font-size: 0.72rem;
            font-weight: 800;
            margin-bottom: 0.45rem;
        }
        .failure-story-title {
            color: var(--text);
            font-size: 1.08rem;
            font-weight: 800;
            line-height: 1.35;
            margin-bottom: 0.65rem;
        }
        .failure-story-copy {
            color: #475569;
            line-height: 1.65;
        }
        .failure-panel {
            border-radius: 18px;
            padding: 12px 14px;
            margin-top: 0.75rem;
        }
        .failure-panel-bad {
            background: rgba(254, 242, 242, 0.96);
            border: 1px solid rgba(252, 165, 165, 0.95);
        }
        .failure-panel-good {
            background: rgba(240, 253, 244, 0.96);
            border: 1px solid rgba(134, 239, 172, 0.95);
        }
        .failure-panel-title {
            font-size: 0.94rem;
            font-weight: 800;
            line-height: 1.35;
            margin-bottom: 0.3rem;
        }
        .failure-panel-bad .failure-panel-title {
            color: #b91c1c;
        }
        .failure-panel-good .failure-panel-title {
            color: #166534;
        }
        .failure-panel-copy {
            color: #475569;
            line-height: 1.6;
            font-size: 0.94rem;
        }
        .failure-tag {
            display: inline-flex;
            align-items: center;
            border-radius: 999px;
            padding: 0.24rem 0.62rem;
            font-size: 0.76rem;
            font-weight: 800;
            margin-right: 0.45rem;
            margin-bottom: 0.45rem;
            border: 1px solid rgba(203, 213, 225, 0.95);
            background: rgba(255,255,255,0.92);
            color: #334155;
        }
        .failure-lesson {
            border-left: 3px solid #2563eb;
            padding: 0.1rem 0 0.1rem 0.9rem;
            color: #475569;
            line-height: 1.65;
            margin-top: 0.8rem;
        }
        .demo-case-card {
            border: 1px solid rgba(203, 213, 225, 0.95);
            border-radius: 22px;
            padding: 18px 18px;
            background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(248,250,252,0.96));
            box-shadow: 0 12px 24px rgba(15, 23, 42, 0.05);
            height: 100%;
        }
        .demo-case-kicker {
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            font-size: 0.72rem;
            font-weight: 800;
            margin-bottom: 0.45rem;
        }
        .demo-case-title {
            color: var(--text);
            font-size: 1.1rem;
            font-weight: 800;
            line-height: 1.35;
            margin-bottom: 0.45rem;
        }
        .demo-case-copy {
            color: #475569;
            line-height: 1.65;
        }
        .demo-signal-list {
            display: grid;
            gap: 0.65rem;
        }
        .demo-signal {
            display: flex;
            align-items: flex-start;
            gap: 0.7rem;
            padding: 0.7rem 0.8rem;
            border-radius: 16px;
            border: 1px solid rgba(226, 232, 240, 0.95);
            background: rgba(255,255,255,0.94);
        }
        .demo-signal-dot {
            width: 10px;
            height: 10px;
            border-radius: 999px;
            flex-shrink: 0;
            margin-top: 0.38rem;
            background: #2563eb;
        }
        .demo-signal-copy {
            color: #475569;
            line-height: 1.6;
            font-size: 0.94rem;
        }
        .demo-outcome-card {
            border: 1px solid rgba(203, 213, 225, 0.95);
            border-radius: 22px;
            padding: 18px 18px;
            background: rgba(255,255,255,0.96);
            box-shadow: 0 12px 26px rgba(15, 23, 42, 0.05);
            height: 100%;
        }
        .demo-outcome-card-good {
            border-color: rgba(134, 239, 172, 0.95);
            background:
                radial-gradient(circle at top right, rgba(34,197,94,0.10), transparent 34%),
                linear-gradient(180deg, rgba(255,255,255,0.98), rgba(240,253,244,0.95));
        }
        .demo-outcome-card-risky {
            border-color: rgba(253, 186, 116, 0.95);
            background:
                radial-gradient(circle at top right, rgba(245,158,11,0.10), transparent 34%),
                linear-gradient(180deg, rgba(255,255,255,0.98), rgba(255,247,237,0.95));
        }
        .demo-outcome-kicker {
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            font-size: 0.72rem;
            font-weight: 800;
            margin-bottom: 0.45rem;
        }
        .demo-outcome-title {
            color: var(--text);
            font-size: 1.15rem;
            font-weight: 800;
            line-height: 1.35;
            margin-bottom: 0.55rem;
        }
        .demo-pill {
            display: inline-flex;
            align-items: center;
            border-radius: 999px;
            padding: 0.24rem 0.62rem;
            font-size: 0.76rem;
            font-weight: 800;
            margin-bottom: 0.7rem;
        }
        .demo-pill-green {
            background: rgba(220, 252, 231, 0.95);
            color: #166534;
            border: 1px solid rgba(134, 239, 172, 0.9);
        }
        .demo-pill-yellow {
            background: rgba(254, 249, 195, 0.95);
            color: #854d0e;
            border: 1px solid rgba(253, 224, 71, 0.9);
        }
        .demo-pill-red {
            background: rgba(254, 226, 226, 0.95);
            color: #991b1b;
            border: 1px solid rgba(252, 165, 165, 0.9);
        }
        .demo-outcome-copy {
            color: #475569;
            line-height: 1.65;
            margin-bottom: 0.7rem;
        }
        .demo-reason-list {
            display: grid;
            gap: 0.5rem;
        }
        .demo-reason {
            border-radius: 14px;
            padding: 0.65rem 0.75rem;
            background: rgba(255,255,255,0.9);
            border: 1px solid rgba(226, 232, 240, 0.95);
            color: #475569;
            line-height: 1.55;
            font-size: 0.93rem;
        }
        .demo-note {
            border-left: 3px solid #0f766e;
            padding: 0.1rem 0 0.1rem 0.9rem;
            color: #475569;
            line-height: 1.65;
        }
        .framework-panel {
            border: 1px solid rgba(203, 213, 225, 0.95);
            border-radius: 22px;
            padding: 18px 18px;
            background:
                radial-gradient(circle at top right, rgba(37,99,235,0.08), transparent 34%),
                linear-gradient(180deg, rgba(255,255,255,0.98), rgba(248,250,252,0.96));
            box-shadow: 0 12px 26px rgba(15, 23, 42, 0.05);
        }
        .framework-kicker {
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            font-size: 0.72rem;
            font-weight: 800;
            margin-bottom: 0.45rem;
        }
        .framework-title {
            color: var(--text);
            font-size: 1.18rem;
            font-weight: 800;
            line-height: 1.35;
            margin-bottom: 0.45rem;
        }
        .framework-summary {
            color: #475569;
            line-height: 1.7;
            margin-bottom: 1rem;
        }
        .framework-meta-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 10px;
            margin-bottom: 1rem;
        }
        .framework-meta {
            border: 1px solid rgba(226, 232, 240, 0.95);
            border-radius: 16px;
            padding: 11px 12px;
            background: rgba(255,255,255,0.92);
        }
        .framework-meta-label {
            color: #64748b;
            font-size: 0.72rem;
            text-transform: uppercase;
            letter-spacing: 0.07em;
            font-weight: 800;
            margin-bottom: 0.28rem;
        }
        .framework-meta-value {
            color: var(--text);
            font-size: 0.92rem;
            font-weight: 700;
            line-height: 1.45;
        }
        .framework-focus-grid {
            display: grid;
            gap: 0.65rem;
        }
        .framework-focus-item {
            display: flex;
            align-items: flex-start;
            gap: 0.7rem;
            padding: 0.7rem 0.8rem;
            border-radius: 16px;
            background: rgba(255,255,255,0.9);
            border: 1px solid rgba(226, 232, 240, 0.95);
        }
        .framework-focus-dot {
            width: 10px;
            height: 10px;
            border-radius: 999px;
            flex-shrink: 0;
            margin-top: 0.38rem;
            background: #2563eb;
        }
        .framework-focus-copy {
            color: #475569;
            line-height: 1.6;
            font-size: 0.94rem;
        }
        .home-hero-card {
            border: 1px solid rgba(191, 219, 254, 0.9);
            border-radius: 24px;
            padding: 22px 24px;
            background:
                radial-gradient(circle at top right, rgba(37,99,235,0.12), transparent 34%),
                linear-gradient(180deg, rgba(255,255,255,0.98), rgba(248,250,252,0.96));
            box-shadow: 0 18px 38px rgba(15, 23, 42, 0.08);
        }
        .home-hero-kicker {
            color: #1d4ed8;
            text-transform: uppercase;
            letter-spacing: 0.11em;
            font-size: 0.74rem;
            font-weight: 800;
            margin-bottom: 0.9rem;
        }
        .home-hero-title-row {
            display: flex;
            align-items: flex-start;
            gap: 16px;
        }
        .home-hero-mark {
            width: 58px;
            height: 58px;
            border-radius: 18px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background: rgba(37, 99, 235, 0.10);
            flex-shrink: 0;
        }
        .home-hero-title {
            color: var(--text);
            font-size: clamp(2.5rem, 4vw, 4.2rem);
            font-weight: 850;
            line-height: 0.98;
            letter-spacing: -0.04em;
            margin-bottom: 0.9rem;
        }
        .home-hero-copy {
            color: #475569;
            font-size: 1.08rem;
            line-height: 1.7;
            max-width: 46rem;
        }
        .home-chip-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.55rem;
            margin-top: 1.2rem;
        }
        .home-side-card {
            border: 1px solid rgba(191, 219, 254, 0.9);
            border-radius: 22px;
            padding: 18px 18px;
            background: rgba(255,255,255,0.96);
            box-shadow: 0 14px 28px rgba(15, 23, 42, 0.05);
            margin-bottom: 0.8rem;
        }
        .home-side-label {
            display: flex;
            align-items: center;
            gap: 0.45rem;
            color: #1d4ed8;
            font-size: 0.82rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 0.55rem;
        }
        .home-side-title {
            color: var(--text);
            font-size: 1.2rem;
            font-weight: 800;
            line-height: 1.35;
            margin-bottom: 0.55rem;
        }
        .home-side-copy {
            color: #64748b;
            line-height: 1.65;
        }
        .home-kpi-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 10px;
            margin-top: 0.9rem;
        }
        .home-kpi {
            border: 1px solid var(--border);
            border-radius: 18px;
            padding: 13px 13px;
            background: rgba(255,255,255,0.96);
            box-shadow: 0 10px 20px rgba(15, 23, 42, 0.04);
        }
        .home-kpi-value {
            color: var(--text);
            font-size: 1.55rem;
            font-weight: 850;
            line-height: 1;
            margin-bottom: 0.35rem;
        }
        .home-kpi-label {
            color: #64748b;
            font-size: 0.86rem;
            line-height: 1.45;
        }
        .home-act-card {
            border: 1px solid var(--border);
            border-radius: 22px;
            padding: 16px 16px;
            background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(248,250,252,0.95));
            box-shadow: 0 12px 24px rgba(15, 23, 42, 0.05);
            margin-bottom: 0.75rem;
        }
        .home-act-header {
            display: flex;
            align-items: flex-start;
            gap: 14px;
        }
        .home-act-icon {
            width: 48px;
            height: 48px;
            border-radius: 15px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }
        .home-act-title {
            color: var(--text);
            font-size: 1.18rem;
            font-weight: 800;
            line-height: 1.3;
            margin-bottom: 0.35rem;
        }
        .home-act-copy {
            color: #64748b;
            line-height: 1.65;
        }
        .home-page-summary {
            position: relative;
            margin: 0 0 0.8rem 0.35rem;
            padding: 0.1rem 0 0.1rem 1rem;
        }
        .home-page-summary::before {
            content: "";
            position: absolute;
            left: 0;
            top: 0.1rem;
            bottom: 0.1rem;
            width: 2px;
            border-radius: 999px;
            background: linear-gradient(180deg, #dbeafe 0%, #e2e8f0 100%);
        }
        .home-page-title {
            display: flex;
            align-items: center;
            gap: 0.55rem;
            color: var(--text);
            font-size: 1rem;
            font-weight: 750;
            margin-bottom: 0.3rem;
        }
        .home-page-dot {
            width: 9px;
            height: 9px;
            border-radius: 999px;
            flex-shrink: 0;
        }
        .home-page-copy {
            color: #64748b;
            line-height: 1.6;
            font-size: 0.95rem;
        }
        .trust-compass-panel {
            border: 1px solid rgba(191, 219, 254, 0.95);
            border-radius: 24px;
            padding: 18px 18px;
            background:
                radial-gradient(circle at top right, rgba(15,118,110,0.10), transparent 32%),
                linear-gradient(180deg, rgba(255,255,255,0.98), rgba(248,250,252,0.96));
            box-shadow: 0 16px 32px rgba(15, 23, 42, 0.06);
            margin-bottom: 1rem;
        }
        .trust-compass-visual {
            position: relative;
            min-height: 360px;
            border: 1px solid rgba(203, 213, 225, 0.9);
            border-radius: 24px;
            background: rgba(255,255,255,0.92);
            overflow: hidden;
            margin-bottom: 1rem;
        }
        .trust-compass-ring {
            position: absolute;
            inset: 50% auto auto 50%;
            width: 250px;
            height: 250px;
            transform: translate(-50%, -50%);
            border: 1.5px solid rgba(148, 163, 184, 0.35);
            border-radius: 999px;
            background: radial-gradient(circle, rgba(219, 234, 254, 0.26) 0%, rgba(219, 234, 254, 0.08) 54%, transparent 55%);
        }
        .trust-compass-ring-inner {
            width: 150px;
            height: 150px;
            border-color: rgba(148, 163, 184, 0.22);
            background: none;
        }
        .trust-compass-axis {
            position: absolute;
            left: 50%;
            top: 50%;
            background: rgba(148, 163, 184, 0.35);
            transform: translate(-50%, -50%);
        }
        .trust-compass-axis-vertical {
            width: 1px;
            height: 238px;
        }
        .trust-compass-axis-horizontal {
            width: 238px;
            height: 1px;
        }
        .trust-compass-axis-diagonal-a {
            width: 210px;
            height: 1px;
            transform: translate(-50%, -50%) rotate(45deg);
        }
        .trust-compass-axis-diagonal-b {
            width: 210px;
            height: 1px;
            transform: translate(-50%, -50%) rotate(-45deg);
        }
        .trust-compass-cardinal {
            position: absolute;
            color: #64748b;
            font-size: 0.76rem;
            font-weight: 800;
            letter-spacing: 0.12em;
            text-transform: uppercase;
        }
        .trust-compass-cardinal-n {
            top: 16px;
            left: 50%;
            transform: translateX(-50%);
        }
        .trust-compass-cardinal-e {
            right: 18px;
            top: 50%;
            transform: translateY(-50%);
        }
        .trust-compass-cardinal-s {
            bottom: 16px;
            left: 50%;
            transform: translateX(-50%);
        }
        .trust-compass-cardinal-w {
            left: 18px;
            top: 50%;
            transform: translateY(-50%);
        }
        .trust-compass-needle {
            position: absolute;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
            width: 0;
            height: 0;
        }
        .trust-compass-needle-main {
            border-left: 12px solid transparent;
            border-right: 12px solid transparent;
            border-bottom: 88px solid #2563eb;
            transform: translate(-50%, -92%);
            filter: drop-shadow(0 10px 12px rgba(37, 99, 235, 0.18));
        }
        .trust-compass-needle-tail {
            border-left: 9px solid transparent;
            border-right: 9px solid transparent;
            border-top: 62px solid rgba(148, 163, 184, 0.72);
            transform: translate(-50%, -2%);
        }
        .trust-compass-hub {
            position: absolute;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
            width: 74px;
            height: 74px;
            border-radius: 999px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: rgba(255,255,255,0.98);
            border: 1px solid rgba(191, 219, 254, 0.95);
            box-shadow: 0 12px 24px rgba(15, 23, 42, 0.08);
            color: var(--text);
            font-size: 0.88rem;
            font-weight: 800;
        }
        .trust-compass-point {
            position: absolute;
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            padding: 0.38rem 0.72rem;
            border-radius: 999px;
            background: rgba(255,255,255,0.96);
            border: 1px solid rgba(203, 213, 225, 0.95);
            color: var(--text);
            font-size: 0.82rem;
            font-weight: 750;
            box-shadow: 0 10px 20px rgba(15, 23, 42, 0.05);
        }
        .trust-compass-point-north {
            top: 46px;
            left: 50%;
            transform: translateX(-50%);
        }
        .trust-compass-point-east {
            top: 50%;
            right: 28px;
            transform: translateY(-50%);
        }
        .trust-compass-point-south_east {
            right: 64px;
            bottom: 46px;
        }
        .trust-compass-point-south_west {
            left: 64px;
            bottom: 46px;
        }
        .trust-compass-point-west {
            top: 50%;
            left: 28px;
            transform: translateY(-50%);
        }
        .trust-compass-point-dot {
            width: 10px;
            height: 10px;
            border-radius: 999px;
            flex-shrink: 0;
        }
        .trust-compass-caption {
            margin-bottom: 1rem;
            color: #475569;
            line-height: 1.65;
            font-size: 0.94rem;
        }
        .trust-compass-caption strong {
            color: var(--text);
        }
        .trust-compass-legend {
            display: grid;
            gap: 0.8rem;
        }
        .trust-check-card {
            border: 1px solid rgba(226, 232, 240, 0.95);
            border-radius: 18px;
            padding: 12px 13px;
            background: rgba(255,255,255,0.92);
        }
        .trust-check-title {
            display: flex;
            align-items: center;
            gap: 0.55rem;
            color: var(--text);
            font-weight: 750;
            margin-bottom: 0.45rem;
        }
        .trust-row-dot {
            width: 10px;
            height: 10px;
            border-radius: 999px;
            flex-shrink: 0;
        }
        .trust-check-question {
            color: var(--text);
            font-size: 0.96rem;
            font-weight: 650;
            line-height: 1.55;
            margin-bottom: 0.35rem;
        }
        .trust-check-note {
            color: #64748b;
            font-size: 0.9rem;
            line-height: 1.55;
        }
        .roadmap-stage-card {
            border: 1px solid rgba(203, 213, 225, 0.95);
            border-top: 4px solid var(--roadmap-accent);
            border-radius: 24px;
            padding: 18px 18px;
            background:
                radial-gradient(circle at top right, var(--roadmap-soft), transparent 36%),
                linear-gradient(180deg, rgba(255,255,255,0.98), rgba(248,250,252,0.96));
            box-shadow: 0 14px 28px rgba(15, 23, 42, 0.06);
            height: 100%;
        }
        .roadmap-stage-top {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 0.65rem;
            margin-bottom: 0.85rem;
        }
        .roadmap-stage-step,
        .roadmap-stage-window {
            display: inline-flex;
            align-items: center;
            border-radius: 999px;
            padding: 0.28rem 0.7rem;
            font-size: 0.74rem;
            font-weight: 800;
            letter-spacing: 0.06em;
            text-transform: uppercase;
        }
        .roadmap-stage-step {
            background: rgba(15, 23, 42, 0.06);
            color: var(--text);
        }
        .roadmap-stage-window {
            background: rgba(255,255,255,0.92);
            border: 1px solid rgba(203, 213, 225, 0.95);
            color: #475569;
        }
        .roadmap-stage-head {
            display: flex;
            align-items: flex-start;
            gap: 0.9rem;
            margin-bottom: 0.95rem;
        }
        .roadmap-stage-icon {
            width: 50px;
            height: 50px;
            border-radius: 16px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }
        .roadmap-stage-title {
            color: var(--text);
            font-size: 1.16rem;
            font-weight: 800;
            line-height: 1.3;
            margin-bottom: 0.35rem;
        }
        .roadmap-stage-copy {
            color: #64748b;
            line-height: 1.65;
        }
        .roadmap-stage-meta {
            display: flex;
            justify-content: space-between;
            gap: 0.8rem;
            border-radius: 16px;
            padding: 0.75rem 0.85rem;
            background: rgba(255,255,255,0.82);
            border: 1px solid rgba(226, 232, 240, 0.95);
            margin-bottom: 0.9rem;
        }
        .roadmap-stage-meta-label {
            color: #64748b;
            font-size: 0.76rem;
            font-weight: 800;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }
        .roadmap-stage-meta-value {
            color: var(--text);
            font-size: 0.92rem;
            font-weight: 700;
            text-align: right;
        }
        .roadmap-stage-list-label {
            color: #475569;
            font-size: 0.78rem;
            font-weight: 800;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            margin-bottom: 0.55rem;
        }
        .roadmap-stage-list {
            margin: 0;
            padding-left: 1.1rem;
            color: #475569;
            line-height: 1.7;
        }
        .roadmap-stage-list li + li {
            margin-top: 0.32rem;
        }
        .roadmap-stage-gate {
            margin-top: 0.95rem;
            border-left: 3px solid var(--roadmap-accent);
            padding: 0.1rem 0 0.1rem 0.85rem;
            color: #475569;
            line-height: 1.62;
        }
        .roadmap-checklist {
            display: grid;
            gap: 0.8rem;
        }
        .roadmap-check-item {
            display: grid;
            grid-template-columns: 38px 1fr;
            gap: 0.9rem;
            align-items: start;
            border: 1px solid rgba(226, 232, 240, 0.95);
            border-radius: 18px;
            padding: 0.95rem 1rem;
            background: rgba(255,255,255,0.95);
            box-shadow: 0 10px 20px rgba(15, 23, 42, 0.04);
        }
        .roadmap-check-number {
            width: 38px;
            height: 38px;
            border-radius: 999px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background: rgba(37, 99, 235, 0.10);
            color: #1d4ed8;
            font-size: 0.84rem;
            font-weight: 800;
        }
        .roadmap-check-title {
            color: var(--text);
            font-size: 0.98rem;
            font-weight: 800;
            line-height: 1.35;
            margin-bottom: 0.24rem;
        }
        .roadmap-check-copy {
            color: #64748b;
            line-height: 1.6;
            font-size: 0.94rem;
        }
        .roadmap-owner-card {
            border: 1px solid rgba(226, 232, 240, 0.95);
            border-radius: 20px;
            padding: 16px 16px;
            background:
                radial-gradient(circle at top right, rgba(15,118,110,0.08), transparent 32%),
                linear-gradient(180deg, rgba(255,255,255,0.98), rgba(248,250,252,0.96));
            box-shadow: 0 12px 24px rgba(15, 23, 42, 0.05);
            height: 100%;
        }
        .roadmap-owner-title {
            color: var(--text);
            font-size: 1rem;
            font-weight: 800;
            line-height: 1.35;
            margin-bottom: 0.4rem;
        }
        .roadmap-owner-copy {
            color: #475569;
            line-height: 1.65;
            font-size: 0.94rem;
        }
        .roadmap-priority-card {
            border: 1px solid rgba(203, 213, 225, 0.95);
            border-radius: 20px;
            padding: 16px 16px;
            background: rgba(255,255,255,0.96);
            box-shadow: 0 12px 24px rgba(15, 23, 42, 0.05);
            height: 100%;
        }
        .roadmap-priority-kicker {
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            font-size: 0.72rem;
            font-weight: 800;
            margin-bottom: 0.45rem;
        }
        .roadmap-priority-title {
            color: var(--text);
            font-size: 1.04rem;
            font-weight: 800;
            line-height: 1.35;
            margin-bottom: 0.45rem;
        }
        .roadmap-priority-copy {
            color: #475569;
            line-height: 1.65;
        }
        .roadmap-summary {
            border: 1px solid rgba(196, 181, 253, 0.95);
            border-radius: 24px;
            padding: 22px 22px;
            background:
                radial-gradient(circle at top right, rgba(147,51,234,0.12), transparent 34%),
                linear-gradient(180deg, rgba(255,255,255,0.98), rgba(250,245,255,0.96));
            box-shadow: 0 16px 32px rgba(15, 23, 42, 0.06);
        }
        .roadmap-summary-kicker {
            color: #7c3aed;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            font-size: 0.74rem;
            font-weight: 800;
            margin-bottom: 0.55rem;
        }
        .roadmap-summary-title {
            color: var(--text);
            font-size: 1.45rem;
            font-weight: 850;
            line-height: 1.2;
            margin-bottom: 0.7rem;
        }
        .roadmap-summary-copy {
            color: #475569;
            line-height: 1.7;
            font-size: 1rem;
            margin-bottom: 1rem;
        }
        .roadmap-summary-chip-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.55rem;
        }
        .roadmap-summary-chip {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            border-radius: 999px;
            padding: 0.38rem 0.78rem;
            background: rgba(255,255,255,0.92);
            border: 1px solid rgba(196, 181, 253, 0.95);
            color: #5b21b6;
            font-size: 0.82rem;
            font-weight: 700;
        }
        .story-card {
            border: 1px solid var(--border);
            border-radius: 18px;
            padding: 16px 16px 14px;
            background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(248,250,252,0.96));
            box-shadow: 0 10px 22px rgba(15, 23, 42, 0.05);
            min-height: 190px;
        }
        .story-step {
            display: inline-flex;
            align-items: center;
            border-radius: 999px;
            padding: 0.25rem 0.65rem;
            background: rgba(226, 232, 240, 0.85);
            color: #334155;
            font-size: 0.72rem;
            font-weight: 800;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            margin-bottom: 0.85rem;
        }
        .story-card-head {
            display: flex;
            align-items: flex-start;
            gap: 12px;
        }
        .story-card-icon {
            width: 46px;
            height: 46px;
            border-radius: 14px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }
        .story-card-title {
            color: var(--text);
            font-size: 1.22rem;
            font-weight: 800;
            line-height: 1.3;
            margin-bottom: 0.45rem;
        }
        .story-card-desc {
            color: var(--muted);
            line-height: 1.65;
        }
        .home-stat-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 10px;
            margin-bottom: 1rem;
        }
        .home-stat {
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 12px 12px;
            background: rgba(255,255,255,0.96);
            box-shadow: 0 8px 18px rgba(15, 23, 42, 0.04);
        }
        .home-stat-value {
            color: var(--text);
            font-size: 1.5rem;
            font-weight: 800;
            line-height: 1;
            margin-bottom: 0.3rem;
        }
        .home-stat-label {
            color: var(--muted);
            font-size: 0.84rem;
            line-height: 1.45;
        }
        .home-bullet-list {
            margin: 0;
            padding-left: 1.1rem;
            color: var(--muted);
            line-height: 1.7;
        }
        .sidebar-hero,
        .sidebar-note {
            background: rgba(255,255,255,0.92);
            border: 1px solid rgba(191, 219, 254, 0.9);
            border-radius: 18px;
            padding: 14px 14px;
            margin-bottom: 12px;
            box-shadow: 0 14px 30px rgba(37, 99, 235, 0.08);
        }
        .sidebar-hero {
            background:
                linear-gradient(180deg, rgba(255,255,255,0.98), rgba(239,246,255,0.96)),
                radial-gradient(circle at top right, rgba(37,99,235,0.16), transparent 36%);
        }
        .sidebar-eyebrow {
            color: #1d4ed8;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            font-size: 0.72rem;
            font-weight: 800;
            margin-bottom: 0.35rem;
        }
        .sidebar-title {
            display: flex;
            align-items: center;
            gap: 8px;
            font-weight: 750;
            color: var(--text);
            margin-bottom: 6px;
        }
        .sidebar-copy {
            color: var(--muted);
            font-size: 0.92rem;
            line-height: 1.5;
        }
        .sidebar-progress-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.45rem;
            margin-top: 0.85rem;
        }
        .sidebar-pill {
            display: inline-flex;
            align-items: center;
            border-radius: 999px;
            padding: 0.24rem 0.62rem;
            background: rgba(219, 234, 254, 0.9);
            color: #1d4ed8;
            font-size: 0.74rem;
            font-weight: 700;
        }
        .sidebar-pill-muted {
            background: rgba(241, 245, 249, 0.95);
            color: #334155;
        }
        .sidebar-progress-track {
            width: 100%;
            height: 8px;
            border-radius: 999px;
            margin-top: 0.8rem;
            background: rgba(191, 219, 254, 0.45);
            overflow: hidden;
        }
        .sidebar-progress-track span {
            display: block;
            height: 100%;
            border-radius: inherit;
            background: linear-gradient(90deg, #2563eb 0%, #0f766e 100%);
        }
        .sidebar-group-label {
            color: #475569;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            font-size: 0.7rem;
            font-weight: 800;
            margin: 1rem 0 0.45rem;
        }
        .sidebar-link-meta {
            margin: -0.18rem 0 0.7rem 0;
            padding: 0 0.25rem 0 0.3rem;
            color: #64748b;
            font-size: 0.82rem;
            line-height: 1.45;
        }
        .sidebar-link-meta-active {
            color: #0f172a;
        }
        .sidebar-link-meta-next {
            color: #334155;
        }
        .sidebar-link-kicker {
            display: inline-block;
            font-weight: 700;
            color: #1d4ed8;
            margin-right: 0.35rem;
        }
        .sidebar-note {
            margin-top: 0.8rem;
            color: var(--muted);
        }
        .sidebar-note-title {
            display: flex;
            align-items: center;
            gap: 0.45rem;
            font-weight: 750;
            color: var(--text);
            margin-bottom: 0.35rem;
        }
        .sidebar-note-copy {
            font-weight: 700;
            color: var(--text);
        }
        .sidebar-note-subcopy {
            margin-top: 0.35rem;
            font-size: 0.86rem;
            line-height: 1.5;
            color: #64748b;
        }
        .surface-strip {
            border: 1px solid var(--border);
            background: rgba(255,255,255,0.92);
            border-radius: 14px;
            padding: 14px 18px;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.04);
        }
        [data-testid="stMain"] [data-testid="stPageLink"] {
            margin-top: 0.5rem;
            margin-bottom: 0.75rem;
        }
        [data-testid="stMain"] [data-testid="stPageLink"] a {
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            width: 100%;
            min-height: 2rem;
            justify-content: center;
            padding: 0.5rem 0.8rem;
            border: 1px solid var(--border);
            border-radius: 10px;
            background: #eef2ff;
            color: #1d4ed8;
            font-weight: 600;
            box-shadow: none;
        }
        [data-testid="stMain"] [data-testid="stPageLink"] a:hover {
            border-color: #bfdbfe;
            background: #e0e7ff;
            color: #1d4ed8;
        }
        [data-testid="stSidebar"] [data-testid="stPageLink"] {
            margin-top: 0;
            margin-bottom: 0.2rem;
        }
        [data-testid="stSidebar"] [data-testid="stPageLink"] a {
            border-radius: 14px;
            background: rgba(255,255,255,0.95);
            border: 1px solid rgba(203, 213, 225, 0.95);
            padding: 0.75rem 0.78rem;
            width: 100%;
            justify-content: flex-start;
            font-weight: 650;
            color: #0f172a;
            box-shadow: 0 8px 18px rgba(15, 23, 42, 0.04);
            transition: transform 140ms ease, border-color 140ms ease, box-shadow 140ms ease, background 140ms ease;
        }
        [data-testid="stSidebar"] [data-testid="stPageLink"] a:hover {
            transform: translateY(-1px);
            border-color: #93c5fd;
            background: linear-gradient(180deg, #ffffff 0%, #eff6ff 100%);
            box-shadow: 0 12px 22px rgba(37, 99, 235, 0.08);
        }
        [data-testid="stSidebar"] [data-testid="stPageLink"] a[aria-current="page"] {
            border-color: #60a5fa;
            background: linear-gradient(180deg, #eff6ff 0%, #dbeafe 100%);
            color: #1d4ed8;
            box-shadow: 0 12px 24px rgba(37, 99, 235, 0.14);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def setup_page(page_key: str, page_title: str, layout: str = "wide") -> None:
    """Configure a page and apply the shared chrome."""
    st.set_page_config(page_title=page_title, page_icon=PAGE_ICONS[page_key], layout=layout)
    inject_icon_font()
    inject_global_styles()
    render_sidebar(page_key)


def render_page_header(
    title: str,
    subtitle: str,
    icon_name: str,
    accent: str = "#2563eb",
    chips: Optional[Sequence[str]] = None,
    eyebrow: Optional[str] = None,
) -> None:
    """Render the shared page hero section."""
    chips_html = _join_chips(chips or [])
    eyebrow_html = f"<div class='hero-kicker'>{eyebrow}</div>" if eyebrow else ""
    st.markdown(
        f"""
        <div class='hero-panel' style='--accent:{accent};'>
          <div class='hero-row'>
            <div class='hero-icon' style='background:{accent}12;'>
              {material_icon(icon_name, 30, accent)}
            </div>
            <div>
              {eyebrow_html}
              <h1 style='margin:0;'>{title}</h1>
              <div class='muted'>{subtitle}</div>
            </div>
          </div>
          {f"<div style='margin-top:10px;'>{chips_html}</div>" if chips_html else ""}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_callout(title: str, body: str, icon_name: str = "info", accent: str = "#2563eb") -> None:
    """Render a consistent callout panel."""
    st.markdown(
        f"""
        <div class='callout' style='--accent:{accent};'>
          <strong>{material_icon(icon_name, 18, accent)} {title}</strong><br>
          <span>{body}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_section_intro(title: str, body: str, icon_name: Optional[str] = None, accent: str = "#2563eb") -> None:
    """Render a section heading with optional icon and short explanation."""
    title_html = (
        f"<h2>{material_icon(icon_name, 20, accent)}<span>{title}</span></h2>"
        if icon_name
        else f"<h2>{title}</h2>"
    )
    st.markdown(
        f"<div class='section-intro'>{title_html}<div class='muted'>{body}</div></div>",
        unsafe_allow_html=True,
    )


def apply_dark_theme() -> None:
    """Inject the global CSS used across all pages."""
    inject_icon_font()
    inject_global_styles()


@dataclass
class Safeguards:
    """
    Safeguards are the *policy knobs* that make AI safer for real-world use.
    """
    data_quality_checks: bool = True
    bias_check: bool = True
    confidence_threshold_on: bool = True
    human_review_low_conf: bool = True

    # Policy thresholds (interactive)
    conf_threshold: float = 0.65            # below => low confidence
    missing_threshold: float = 0.10         # above => quality issue
    max_data_age_days: int = 60             # above => stale data
    ood_threshold: float = 0.45             # above => out-of-context


def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-x))


def simulate_model_outputs(df: pd.DataFrame, seed: int = 7) -> pd.DataFrame:
    """
    Simulate a simple prediction + confidence based on case features.
    Intentionally lightweight and transparent for demo purposes.
    """
    rng = np.random.default_rng(seed)

    # Model score influenced by need (positive), data issues (negative), plus noise
    x = (
        2.4 * df["need_score"].to_numpy()
        - 1.3 * df["missing_rate"].to_numpy()
        - 1.0 * df["ood_score"].to_numpy()
        - 0.004 * df["data_age_days"].to_numpy()
        + rng.normal(0, 0.25, size=len(df))
    )
    prob = sigmoid(x)

    # Confidence is lower when the case is out-of-context or has missing values
    conf = np.clip(
        0.92
        - 0.55 * df["ood_score"].to_numpy()
        - 0.85 * df["missing_rate"].to_numpy()
        + rng.normal(0, 0.03, size=len(df)),
        0.05,
        0.99,
    )

    out = df.copy()
    out["pred_prob"] = np.round(prob, 3)
    out["pred_label"] = (prob >= 0.5).astype(int)
    out["confidence"] = np.round(conf, 3)
    return out


def compute_bias_gap(df: pd.DataFrame) -> float:
    """
    Fairness proxy: difference in positive prediction rate between groups.
    """
    rates = df.groupby("sensitive_group")["pred_label"].mean()
    if len(rates) < 2:
        return 0.0
    return float((rates.max() - rates.min()))


def case_risk(row: pd.Series, s: Safeguards) -> Dict[str, Any]:
    """
    Human-friendly risk flags for a single case.
    """
    reasons = []
    points = 0

    # Data quality
    if s.data_quality_checks:
        if row["missing_rate"] > s.missing_threshold:
            reasons.append("Data quality issue: too much missing information.")
            points += 2
        if row["data_age_days"] > s.max_data_age_days:
            reasons.append("Data is old; the situation may have changed.")
            points += 1
    else:
        reasons.append("No data quality checks enabled.")
        points += 2

    # Out-of-context (OOD)
    if row["ood_score"] > s.ood_threshold:
        reasons.append("Case looks unusual compared to training examples (out-of-context).")
        points += 2

    # Confidence threshold
    low_conf = row["confidence"] < s.conf_threshold
    if s.confidence_threshold_on:
        if low_conf:
            reasons.append("Low confidence prediction.")
            points += 2
    else:
        reasons.append("No confidence threshold — AI may be used even when uncertain.")
        points += 1

    # Human review for low confidence
    needs_review = False
    if s.human_review_low_conf and low_conf:
        needs_review = True
        reasons.append("Human review required for low-confidence cases.")
        # review reduces operational risk a bit
        points = max(0, points - 1)

    # Map points to traffic light
    if points >= 5:
        level = "RED"
    elif points >= 3:
        level = "YELLOW"
    else:
        level = "GREEN"

    return {
        "risk_level": level,
        "risk_points": int(points),
        "needs_review": bool(needs_review),
        "low_conf": bool(low_conf),
        "reasons": reasons if reasons else ["No major risk flags triggered."],
    }


def add_risk_columns(df: pd.DataFrame, s: Safeguards) -> pd.DataFrame:
    """
    Vector-friendly risk labels for dashboards.
    """
    out = df.copy()
    # Flags
    out["flag_quality"] = False
    out["flag_stale"] = False
    out["flag_ood"] = out["ood_score"] > s.ood_threshold
    out["flag_low_conf"] = out["confidence"] < s.conf_threshold

    if s.data_quality_checks:
        out["flag_quality"] = out["missing_rate"] > s.missing_threshold
        out["flag_stale"] = out["data_age_days"] > s.max_data_age_days
    else:
        # if checks are off, treat as "unknown/higher baseline"
        out["flag_quality"] = True

    # Risk points
    pts = np.zeros(len(out), dtype=int)
    pts += out["flag_quality"].astype(int) * 2
    pts += out["flag_stale"].astype(int) * 1
    pts += out["flag_ood"].astype(int) * 2

    if s.confidence_threshold_on:
        pts += out["flag_low_conf"].astype(int) * 2
    else:
        pts += 1  # baseline risk if threshold isn't used

    # Human review reduces a point for low-confidence cases (when enabled)
    out["needs_review"] = False
    if s.human_review_low_conf:
        out["needs_review"] = out["flag_low_conf"]
        pts = np.where(out["needs_review"], np.maximum(0, pts - 1), pts)

    out["risk_points"] = pts
    out["risk_level"] = np.where(pts >= 5, "RED", np.where(pts >= 3, "YELLOW", "GREEN"))
    return out


def overall_summary(df: pd.DataFrame, s: Safeguards) -> Dict[str, Any]:
    """
    Management-friendly KPIs.
    """
    low_conf_rate = float((df["confidence"] < s.conf_threshold).mean())
    ood_rate = float((df["ood_score"] > s.ood_threshold).mean())

    quality_incident_rate: Optional[float] = None
    if s.data_quality_checks:
        quality_incident_rate = float(((df["missing_rate"] > s.missing_threshold) | (df["data_age_days"] > s.max_data_age_days)).mean())

    bias_gap: Optional[float] = compute_bias_gap(df) if s.bias_check else None

    # Risk index (0..1) - intentionally simple and explainable
    risk_index = 0.0
    risk_index += 0.45 * low_conf_rate
    risk_index += 0.25 * ood_rate
    if quality_incident_rate is not None:
        risk_index += 0.20 * quality_incident_rate
    else:
        risk_index += 0.20 * 0.50  # assume higher baseline if not measured
    if bias_gap is not None:
        risk_index += 0.35 * bias_gap
    else:
        risk_index += 0.12

    risk_index = float(np.clip(risk_index, 0, 1))
    if risk_index >= 0.62:
        overall = "RED"
    elif risk_index >= 0.38:
        overall = "YELLOW"
    else:
        overall = "GREEN"

    return {
        "overall_risk": overall,
        "risk_index": round(risk_index, 3),
        "low_conf_rate": round(low_conf_rate, 3),
        "ood_rate": round(ood_rate, 3),
        "quality_incident_rate": None if quality_incident_rate is None else round(quality_incident_rate, 3),
        "bias_gap": None if bias_gap is None else round(float(bias_gap), 3),
    }
