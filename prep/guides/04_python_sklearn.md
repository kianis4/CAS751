# Python Data Stack & scikit‑learn — Study Guide

## 1) Core concepts (quick hits)
- NumPy arrays vs pandas DataFrames; indexing and dtypes
- EDA patterns: describe, missingness, correlations, distributions
- Scikit‑learn API: fit/transform/predict; estimators vs transformers
- Pipelines and ColumnTransformer; proper CV with pipelines

## 2) Hands‑on checklist
- Load a dataset; split train/test with stratify if classification
- Baseline: simple model; log metrics
- Pipeline with StandardScaler + model; add OneHotEncoder for categoricals
- Hyperparameter tuning with GridSearchCV; keep a results table

## 3) Practice questions
1) Why use Pipeline instead of manual scaling?
2) How to avoid leakage with target encoding or scaling?
3) When use ColumnTransformer, and why?

## 4) Applied tasks
- Build a pipeline for a mixed‑type dataset; compare LogReg vs RandomForest
- Save best model and a short `model_card.md` describing data, metrics, caveats

## 5) Pitfalls and checks
- Always set random_state for reproducibility
- Balance classes or adjust metrics when imbalanced
- Validate with cross‑val; avoid peeking at test set until the very end

## 6) Mini checklist
- [ ] Can build a clean Pipeline with preprocessing
- [ ] Can run GridSearchCV and interpret results
- [ ] Have a small model card template

---

# Practice Preparation Kit (focused for CAS 751)

## A) Leakage vs Pipeline
Example
- You scale features on the whole dataset before CV and get 0.92; with Pipeline you get 0.84. Which is correct and why?

How to think
- Scaling must be fit only on train folds; otherwise information leaks.

Why it matters
- Fairness/DP claims require sound evaluation.

Steps
1) Build `Pipeline([('scaler', StandardScaler()), ('clf', ...)])`
2) Use cross_val_score on the pipeline

Analogy
- Studying with answer key visible.

Try similar
- Show leakage with feature selection outside CV vs inside Pipeline.

## B) ColumnTransformer for mixed data
Example
- Dataset with numeric and categorical features: set up preprocessing and compare LogReg vs RandomForest.

How to think
- Different preprocessors per column set; keep everything inside Pipeline.

Why it matters
- Baseline rigor for later fairness/DP experiments.

Steps
1) Build ColumnTransformer with scalers/encoders
2) Wrap in Pipeline with model; evaluate

Analogy
- Different tools for different materials.

Try similar
- Add OneHotEncoder(handle_unknown='ignore') and compare performance.
