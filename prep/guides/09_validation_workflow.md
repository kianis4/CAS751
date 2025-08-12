# Validation, Data Hygiene, and Workflow — Study Guide

## 1) Core concepts (quick hits)
- Proper splits: train/val/test; stratification; temporal splits
- Cross‑validation (k‑fold, stratified, nested)
- Leakage examples: scaling/selection before CV; target leakage
- Calibration: reliability curves; Platt/Isotonic
- Experiment tracking and reproducibility

## 2) Applied checklist
- Always use Pipeline for preprocessing + model
- Use StratifiedKFold for classification; GroupKFold if groups exist
- Log random_state, metrics, and CV std; keep an experiments CSV

## 3) Practice questions
1) Give two concrete leakage examples and how to fix them
2) When use nested CV?
3) How to evaluate under class imbalance?

## 4) Tasks
- Build a wrong pipeline (leakage) vs correct Pipeline; show score drop on held‑out
- Plot calibration curve; compute Brier score

## 5) Pitfalls and checks
- Don’t optimize hyperparams on test set
- Be explicit about data time order
- Keep seeds and versions; save artifacts

## 6) Mini checklist
- [ ] Use correct split strategy for the problem
- [ ] Prevent leakage with Pipelines
- [ ] Track experiments reproducibly

---

# Practice Preparation Kit (focused for CAS 751)

## A) Leakage case study
Example
- You see a 5–10% drop when moving scaling/selection into the Pipeline. Explain and fix.

How to think
- Any transform using full data before split leaks target info.

Why it matters
- Invalid evaluations undermine privacy/fairness claims.

Steps
1) Move all preprocessing into Pipeline
2) Re‑run CV; keep held‑out test sealed until final

Analogy
- Practicing with the exam solutions.

Try similar
- Demonstrate temporal split for time‑ordered data.

## B) Calibration and reporting
Example
- Model is miscalibrated; produce reliability curve and Brier score.

How to think
- Compare predicted probs to empirical frequencies; fix with isotonic/Platt.

Why it matters
- Thresholding and fairness both depend on calibrated scores.

Steps
1) Plot calibration curve
2) Apply calibration and re‑evaluate

Analogy
- A biased thermometer; recalibrate.

Try similar
- Group‑wise calibration curves.
