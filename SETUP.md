# CAS 751 Prep — Setup and Roadmap

## Setup (5 minutes)
1) Open this folder in VS Code.
2) Use the pre-configured Python venv (3.13). If needed, run:
   - Install deps: see below.
3) Run a smoke test to check your Python environment.

Dependencies
- File: `prep/requirements.txt`

Optional: Install deps manually (already configured by Copilot agent)
- In a terminal, run: pip install -r prep/requirements.txt

## Roadmap (Day ↔ Guide ↔ Code)
- Day 1: Linear algebra refresher → `prep/guides/01_linear_algebra.md`
- Day 2: Calculus & probability → `prep/guides/02_calculus_probability.md`
- Day 3: Optimization → `prep/guides/03_optimization.md`
- Day 4: Python & sklearn → `prep/guides/04_python_sklearn.md`
- Day 5–6: Info theory (f‑div, DPI/SDPI) → `prep/guides/12_information_theory_basics.md` + `prep/code/01_divergences_mi.py`
- Day 7–8: Central DP + composition → `prep/guides/13_differential_privacy_central.md` + `prep/code/02_dp_mechanisms.py`
- Day 9: RDP + DP‑SGD → `prep/guides/14_renyi_dp_private_sgd.md` + `prep/code/03_rdp_accountant_dp_sgd.py`
- Day 10–11: Local DP + estimation → `prep/guides/15_local_dp.md` + `prep/code/04_ldp_randomized_response.py`
- Day 12–13: Fairness (audit/mitigation) → `prep/guides/16_fairness.md` + `prep/code/05_fairness_audit_thresholds.py`
- Day 14: Capstone & midterm pack → `CAS751/PREP_PLAN.md` + `prep/CHEAT_SHEETS.md`

## Study cadence (ADHD-friendly)
- Daily: 2–3 focus blocks (25/5). Start with the first checkbox. End by logging deliverables.
- Output-first: each day produces notes, code/plots, and a 3–5 bullet reflection.
- If stuck: do the tiniest next step (run one cell / one script), then resume.

## Where everything lives
- Plan: `CAS751/PREP_PLAN.md`
- Guides index: `prep/guides/INDEX.md`
- Code starters: `prep/code/README.md`
- Cheat sheets: `prep/CHEAT_SHEETS.md`
- Templates: `prep/report_template.md`
