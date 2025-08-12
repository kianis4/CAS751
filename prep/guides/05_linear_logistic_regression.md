# Linear & Logistic Regression — Study Guide

## 1) Core concepts (quick hits)
- Linear regression: OLS, MSE, normal equation, assumptions
- Regularization: Ridge (L2) vs Lasso (L1); bias‑variance trade‑off
- Logistic regression: sigmoid link, log‑odds, cross‑entropy loss
- Decision boundaries, feature scaling, interpretability

## 2) Derivations
- ∇w MSE and closed form; ridge normal equation (X^T X + λI)w = X^T y
- Logistic regression NLL and gradient; effect of L2 penalty

## 3) Metrics & validation
- Regression: RMSE, MAE, R^2; residual plots
- Classification: accuracy, precision/recall, F1, ROC‑AUC; calibration
- Cross‑validation; stratification; hyperparameter tuning (C/penalty)

## 4) Practice questions
1) What happens to coefficients under L1 vs L2?
2) Why is scaling important for regularization paths?
3) When would LogReg underperform vs tree‑based models?

## 5) Applied tasks
- Ridge vs Lasso on same dataset; compare coefficients and errors
- Logistic regression with class imbalance; try class_weight='balanced'; plot PR curve
- Calibration curve and threshold tuning for F1 optimization

## 6) Pitfalls and checks
- Multicollinearity inflates variance; check singular values or VIF
- Don’t evaluate on training data; use held‑out or CV
- Beware data leakage when doing feature selection

## 7) Mini checklist
- [ ] Can derive and implement GD for linear regression
- [ ] Can tune ridge/lasso and interpret coefficients
- [ ] Can calibrate and threshold logistic regression

---

# Practice Preparation Kit (focused for CAS 751)

## A) Ridge vs Lasso interpretation
Example
- On standardized features, ridge shrinks all coefficients; lasso zeros some. When pick which?

How to think
- L2 for small, smooth shrinkage; L1 for sparsity and selection.

Why it matters
- Stability/interpretability in audits; affects sensitivity under DP.

Steps
1) Run CV for both
2) Compare coefficients and errors

Analogy
- Ridge = dimmer; Lasso = on/off switches.

Try similar
- ElasticNet blend; vary l1_ratio and observe patterns.

## B) Calibration and thresholds
Example
- Same ROC‑AUC, different calibration; choose threshold for F1.

How to think
- Use precision‑recall curve; pick threshold maximizing F1 on validation; consider group‑wise effects for fairness.

Why it matters
- Deployment decisions and fairness constraints rely on thresholds.

Steps
1) Calibrate (isotonic/Platt)
2) Sweep thresholds, select by F1

Analogy
- Volume knob vs mute button; find the sweet spot.

Try similar
- Optimize threshold for cost‑sensitive loss.
