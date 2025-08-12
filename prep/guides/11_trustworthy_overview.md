# Trustworthy ML Overview — Study Guide

Course fit: CAS 751 focuses on privacy (DP), fairness, and generalization using information-theoretic tools. This guide frames why accuracy alone fails and what trustworthy ML entails.

## 1) Core concepts
- Dimensions of trust: privacy, fairness, robustness, interpretability, accountability, generalization.
- Harms of optimizing only accuracy: distribution shift, feedback loops, disparate impact, privacy leakage, shortcut learning.
- Risk vs uncertainty; socio-technical framing: data lifecycle, stakeholders, deployment context.

## 2) Intuition
- Trustworthiness = constraints and guarantees layered onto predictive performance.
- Information theory helps quantify leakage (privacy), discrimination (through constraints), and generalization (information used from data).

## 3) Practice questions
1) Give two examples where higher accuracy worsens social outcomes. Propose a metric beyond accuracy to detect it.
2) Define a minimal “risk register” for an ML system (3 risks, detection, mitigation).
3) Contrast post-processing fairness fixes vs learning-time constraints. Pros/cons.

## 4) Applied tasks
- Dataset audit: identify sensitive attributes, imbalance, label noise; write 5 bullets on potential harms and stakeholders.
- Baseline diagnostic: compute per-group metrics (accuracy, TPR/FPR); visualize disparities.
- Add a constraint: pick a fairness metric to monitor; define a privacy budget placeholder for future DP training.

## 5) Pitfalls and checks
- Metric laundering: swapping to a convenient metric late in the project.
- Ignoring deployment distribution: fairness on train != fairness in production.
- Overpromising guarantees: be explicit about assumptions and budgets.

## 6) Mini checklist
- [ ] Can articulate why accuracy is insufficient
- [ ] Have a basic audit template and per-group metric script
- [ ] Know which trust axes the course will give formal tools for

---

# Practice Preparation Kit (focused for CAS 751)

## A) Metric beyond accuracy
Example
- A loan model is 95% accurate but rejects qualified applicants in a minority group. Pick two metrics to reveal harm.

How to think
- Use group TPR/FPR, PPV, and calibration gaps; plot disparities.

Why it matters
- Sets context for fairness modules; makes harms visible.

Steps
1) Compute per‑group metrics
2) Visualize differences; write a 3‑bullet risk note

Analogy
- Averages hide outliers; look per group.

Try similar
- Add cost‑sensitive utility to reflect real‑world stakes.

## B) Risk register
Example
- Draft 3 risks, detection signals, and mitigations for a hiring model.

How to think
- Think data, model, deployment risks; one signal and one mitigation each.

Why it matters
- Keeps scope grounded; informs later technical choices.

Steps
1) Fill a 3×3 table
2) Revisit after first baseline

Analogy
- Pre‑flight checklist.

Try similar
- Do the same for a healthcare triage model.
