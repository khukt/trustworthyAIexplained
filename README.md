# Trustworthy AI — Streamlit Overview Demo (for politicians & management)

This Streamlit app is an **overview demo** that explains:
- What Trustworthy AI is
- Why it matters (public safety, economic, trust/legitimacy)
- A simple interactive mini-demo showing how **safeguards** change risk
- Short failure stories + a practical roadmap

## Quick start

### 1) Create a virtualenv (recommended)
```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows
# .venv\Scripts\activate
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Run the app
```bash
streamlit run app.py
```

## Notes
- The interactive demo uses a **small example dataset** and a **lightweight simulated scoring model** (no heavy ML dependencies) to keep the demo easy to run and easy to understand.
- You can replace `data/sample_cases.csv` with your own domain examples later.

## Structure
- `app.py` — Home / navigation
- `pages/` — Streamlit multipage content
- `trust_utils.py` — shared scoring + helper functions
- `data/sample_cases.csv` — small example dataset

## License
MIT




## Story mode
Open **Interactive mini-demo (story mode)** and click through: Reliable → Safe → Fair → Transparent → Accountable.
