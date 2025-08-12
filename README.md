# CAS 751 – Prep Kit (Information-Theoretic Methods in Trustworthy ML)

A focused, ADHD-friendly, two-week preparation kit aligned to the CAS 751 outline. Includes a daily plan, concise guides with practice kits, runnable code, and plotted notebooks for intuition.

## What’s inside
- PREP_PLAN.md – Two-week schedule mapped to course topics (f-divergences/DPI/SDPI, central DP, composition, RDP + DP‑SGD, local DP, fairness).
- SETUP.md – One‑page setup and roadmap.
- prep/guides/ – Complete study guides with “Practice Preparation Kits.” See `prep/guides/INDEX.md`.
- prep/notebooks/ – Visual demos:
  - 01_Information_Theory_Demos.ipynb
  - 02_DP_SGD_RDP_Demo.ipynb (DP‑SGD training curves + toy RDP→(ε, δ) plots)
- prep/code/ – Small runnable scripts mirroring the guides:
  - 01_divergences_mi.py, 02_dp_mechanisms.py, 03_rdp_accountant_dp_sgd.py,
    04_ldp_randomized_response.py, 05_fairness_audit_thresholds.py
- prep/CHEAT_SHEETS.md – Quick Cards.
- prep/report_template.md – Lightweight write‑up scaffold.
- outline2024.pdf – Course outline for reference.

## Quick start
- Prefer following `SETUP.md` for environment and roadmap.
- If needed, install Python deps in your environment: `pip install -r prep/requirements.txt`.
- Open and run the notebooks in `prep/notebooks/` (Run All).
- Or run scripts in `prep/code/` for quick CLI demos.

## Notes
- The RDP accountant in the notebook is didactic (toy bound) for intuition—use vetted accountants for formal reporting.
- Everything is minimal and self‑contained to keep you moving fast.

## Troubleshooting
- If a notebook complains about a missing package (e.g., matplotlib), ensure your env is active and reinstall requirements.

## Contributing
Small PRs welcome: typos, clearer wording, extra checks/plots, or small tests.
