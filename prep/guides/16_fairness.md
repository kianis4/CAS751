# Algorithmic Fairness — Study Guide

Covers: Fairness criteria, trade‑offs, auditing, mitigation at post‑processing/in‑processing levels.

## 1) Core concepts
- Group metrics: demographic parity (DP), equalized odds (EO), equal opportunity (EOp)
- Individual fairness; counterfactual fairness (at a glance)
- Trade‑offs: calibration vs equalized odds; impossibility results

## 2) Auditing
- Compute per‑group metrics: TPR/FPR/PPV; calibration by group
- Visualization: disparity bars; ROC/PR by group; calibration curves

## 3) Mitigation
- Post‑processing: thresholding per group to meet EO/EOp
- Pre‑processing: reweighting, representation learning
- In‑processing: regularizers/constraints; reductions framework

## 4) Practice questions
1) Define EO and why it conflicts with calibration when base rates differ
2) When is demographic parity appropriate or harmful?
3) How would you pick a fairness constraint for a hiring model?

## 5) Applied tasks
- Compute group metrics on a dataset; report disparities
- Apply a post‑processing threshold adjustment to approximate EO; evaluate utility/fairness trade‑off
- Train with a fairness regularizer; compare outcomes

## 6) Pitfalls and checks
- Simpson’s paradox: subgroup analyses
- Data drift: fairness today != fairness tomorrow
- Metric gaming: document chosen metrics and reasons

## 7) Mini checklist
- [ ] Can audit group disparities
- [ ] Can implement one mitigation method
- [ ] Can articulate trade‑offs and limitations

---

# Practice Preparation Kit (focused for CAS 751)

## A) Equalized odds vs calibration
Example
- Base rates differ across groups; can you have both EO and perfect calibration? Explain.

How to think
- Impossibility results: with unequal base rates and non‑trivial models, can’t satisfy both.

Why it matters
- Choose a defensible fairness target and document trade‑offs.

Steps
1) Define EO and calibration
2) State conflict under differing base rates

Try similar
- Consider equal opportunity instead of EO.

## B) Post‑processing thresholds
Example
- Adjust thresholds per group to approximate EO; evaluate utility and fairness.

How to think
- Tune thresholds to match TPR/FPR; measure impact on accuracy/PPV.

Why it matters
- Simple, deployment‑friendly mitigation.

Steps
1) Fit base model
2) Optimize thresholds per group; re‑evaluate
