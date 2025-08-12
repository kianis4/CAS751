# CAS 751 Machine Learning — 2‑Week Preparation Plan (ADHD‑friendly)

This is a focused, day‑by‑day plan tailored to CAS 751: Information‑Theoretic Methods in Trustworthy ML. It covers only what you need for this course: f‑divergences, DPI/SDPI, central and local differential privacy (including RDP and DP‑SGD), statistical estimation under LDP, and algorithmic fairness. It uses short blocks, concrete deliverables, and checklists to keep momentum.

---

## How to use this plan
- Time blocks: 2–3 focus blocks per day (25 min on, 5 min off, repeat 3×, then 15–20 min break). Target ~3–4 hours/day.
- Setup ritual (2 minutes): open today’s section, start timer, put phone away, start with the first checkbox.
- Done ritual (2 minutes): check off deliverables, jot 1–2 blockers, schedule tomorrow’s first task.
- Materials: Python 3.10+, Jupyter or VS Code, NumPy, pandas, matplotlib, scikit‑learn.
- Output: Keep all artifacts in a folder named `prep/` (notes, code, plots). Each day has “deliverables” you can tick.

---

## Quick readiness checklist (CAS 751)
Tick these by the end of Week 2:
- [ ] Can define f‑divergence and state DPI/SDPI; sketch proofs at a high level
- [ ] Compute and compare KL/TV/JS on simple parametric distributions
- [ ] State (ε,δ)‑DP, calibrate Laplace/Gaussian noise for simple queries
- [ ] Explain composition (basic/advanced) and post‑processing; do a simple accountant workflow
- [ ] Run a small DP‑SGD training on synthetic data; report (ε,δ) via RDP
- [ ] Define LDP and implement randomized response, with unbiased estimators and error analysis
- [ ] Audit group disparities and apply a simple threshold‑based fairness mitigation

---

## Week 1 (Syllabus‑aligned)

### Day 1 — Linear algebra refresh (90–150 min)
Focus: vectors, norms, operator norm, eigen/SVD intuition (for PCA and sensitivity bounds).

Study
- Vector/matrix operations, shapes, broadcasting
- Norms (L1/L2), dot products, projections
- Eigenvalues/eigenvectors, SVD (what/why), PCA link

Do
- Derive: projection of y onto span{x} and residual norm
- Compute by hand a small 2×2 eigendecomposition (when possible)
- Code: create random matrices, verify (AB)^T = B^T A^T; check orthogonality

Deliverables
- [ ] One page of LA notes with 3 worked examples
- [ ] Python snippet that checks a few matrix identities

### Day 2 — Calculus + probability/statistics (120–180 min)
Focus: gradients/chain rule; expectation/variance; Bayes; for optimization and likelihoods used later.

Study
- Gradients/Jacobians; chain rule on scalar loss L(w)
- Common distributions: Bernoulli, Gaussian; log‑likelihood
- Bayes rule, MAP vs MLE intuition

Do
- Derive ∇w of MSE: L(w)=||Xw−y||^2 / n and closed‑form solution
- Compute by hand: mean/var and confidence intuition on small samples
- Code: sample from N(0,1); estimate mean/var; visualize histogram

Deliverables
- [ ] Derivation of MSE gradient and normal equation
- [ ] Plot of sampled Gaussian with sample stats

### Day 3 — Optimization foundations (120–150 min)
Focus: GD/SGD, step size, convexity intuition.

Study
- Gradient descent vs stochastic; convergence intuition; learning rate
- Convex vs non‑convex; line search basics (heuristics)

Do
- From scratch: implement gradient descent for linear regression (NumPy)
- Experiment: compare step sizes; plot loss vs iterations

Deliverables
- [ ] `gd_linear_regression.py` (or notebook cell) with loss curve

### Day 4 — Python data stack + sklearn (120–180 min)
Focus: pandas, plotting, scikit‑learn APIs, pipelines.

Study
- pandas indexing, joins, groupby; matplotlib/seaborn quick plots
- scikit‑learn: estimators, transformers, `fit/transform/predict`, pipelines

Do
- Load a CSV (Iris or Wine), EDA: describe, missingness, correlations
- Train/test split; baseline LinearRegression; evaluate R^2/MSE
- Build a `Pipeline` with `StandardScaler` + model

Deliverables
- [ ] Notebook with EDA + baseline model + pipeline

### Day 5 — Information theory I: f‑divergences, MI, DPI (150–180 min)
Focus: definitions and intuition; compute divergences; prove DPI for MI.

Study
- `prep/guides/12_information_theory_basics.md` sections 1–4

Do
- Compute KL/TV/JS for two Gaussians (code skeleton provided)
- DPI proof sketch for MI using chain rule

Deliverables
- [ ] One‑page summary of f‑divergences + DPI

### Day 6 — Information theory II: SDPI and contractions (120–150 min)
Focus: SDPI motivation; contraction coefficients; simple channel examples.

Study
- `prep/guides/12_information_theory_basics.md` SDPI parts

Do
- Simulate BSC(p) and estimate MI vs p; discuss contraction

Deliverables
- [ ] Short note on SDPI intuition with one numerical example
Focus: bias‑variance, L2/L1, classification metrics.

Study
- Linear vs logistic regression objectives; link functions
- Regularization: ridge vs lasso; feature scaling; interpretations
- Metrics: regression (MSE/RMSE/R^2), classification (accuracy, precision/recall, F1, ROC‑AUC); class imbalance

Do
- Ridge vs Lasso on same dataset; compare coefficients and errors
- Logistic regression on a binary dataset; inspect coefficients and decision boundary
- Cross‑validation with `GridSearchCV`

Deliverables
- [ ] Plots/tables comparing ridge vs lasso; CV report

### Day 7 — Differential Privacy I: definitions and mechanisms (120–180 min)
Focus: (ε,δ)‑DP, sensitivity, Laplace/Gaussian mechanisms, post‑processing.

Study
- `prep/guides/13_differential_privacy_central.md` definitions and mechanisms

Do
- Implement DP counts/means with Laplace/Gaussian noise; empirically check inequalities

Deliverables
- [ ] Notebook or script with DP queries + sanity plots

---

## Week 2 (Syllabus‑aligned)

### Day 8 — DP II: Approximate DP and composition (120–180 min)
Focus: δ>0, basic vs advanced composition, privacy amplification.

Study
- `prep/guides/13_differential_privacy_central.md` composition section

Do
- Track privacy over multiple queries; show utility‑privacy trade‑off

Deliverables
- [ ] One‑pager: composition examples and pitfalls

### Day 9 — DP‑SGD and Rényi DP (120–180 min)
Focus: gradient clipping, Gaussian noise, RDP accounting and ε conversion.

Study
- `prep/guides/14_renyi_dp_private_sgd.md`

Do
- Train a toy logistic regression with DP‑SGD; compute (ε,δ) via simple RDP accountant

Deliverables
- [ ] Report: utility vs (ε,δ), config and seeds
Focus: leakage, proper CV, data hygiene.

Study
- Data leakage cases; nested CV; stratification; temporal splits
- Calibration and probability outputs; threshold tuning

Do
- Build a pipeline with scaling + model; show how leakage occurs if scaling is outside CV
- Reliability curve (calibration plot) for a classifier

Deliverables
- [ ] Notebook demonstrating leakage vs correct pipeline

### Day 10 — Local DP (120–150 min)
Focus: trust models, randomized response (binary and k‑ary), estimation under LDP.

Study
- `prep/guides/15_local_dp.md`

Do
- Implement RR estimators; simulate error vs ε, k, n

Deliverables
- [ ] Plots and derivations for unbiased estimators

### Day 11 — Statistical estimation under LDP (90–120 min)
Focus: bias/variance, minimax flavor (intuitive), practical estimators.

Study
- Reproducibility: seeds, versioning, deterministic ops
- Experiment tracking (even a CSV log); artifact management; simple reporting

Do
- Create a tiny experiment log (CSV) with columns: dataset, features, model, seeds, mean score, std
- Save plots and a one‑page report template

Deliverables
- [ ] `prep/experiments_log.csv` with ≥5 rows; `prep/report_template.md`

### Day 12 — Fairness I: metrics and auditing (120–180 min)
Focus: demographic parity, equalized odds/opportunity, calibration by group; auditing.

Do
- Choose a dataset (Iris/Wine/Diabetes/Heart)
- Clean, EDA, feature engineering (scaling/encoding)
- Baselines: LogReg, RandomForest, XGB/GB
- Model selection via CV; final evaluation on holdout
- Write a 1–2 page report (problem, data, method, results, conclusion)

Deliverables
- [ ] Repo folder `prep/project/` with notebook, saved plots, and report

### Day 13 — Fairness II: mitigation and trade‑offs (120–150 min)
Focus: post‑processing thresholds; brief view of in‑processing constraints; impossibility trade‑offs.
Focus: consolidate, identify gaps.

Do
- Take mock quiz (below) under 60–75 min
- Review wrong/unsure answers; write one‑sentence takeaways per item

Deliverables
- [ ] Completed mock quiz with corrections

### Day 14 — Capstone & midterm readiness (60–120 min)
Focus: consolidate formula sheets, redo 1–2 DP and fairness mini‑tasks, finalize cheat sheet.
Focus: tie to your interests; plan forward.

Do
- Re‑do Day 12 with a dataset closer to your domain or a harder metric (e.g., ROC‑AUC under imbalance)
- Create a personal “cheat sheet” (one page)
- Draft questions for the instructor (office hours/clarifications)

Deliverables
- [ ] One‑page cheat sheet; list of 3–5 questions

---

## Mock quiz (CAS 751‑focused)
Answer concisely. Aim for accuracy first, then brevity.

Concepts
1) Define f‑divergence and give examples generating KL and TV; state DPI.
2) Explain SDPI and give an intuitive example using a noisy channel.
3) State (ε,δ)‑DP; define sensitivity; describe post‑processing.
4) Contrast basic vs advanced composition; what is privacy amplification by subsampling?
5) Outline DP‑SGD (clip C, noise σ) and how to report (ε,δ) via RDP.
6) Define LDP; write randomized response and an unbiased estimator for a Bernoulli mean.
7) Define demographic parity and equalized odds; when do they conflict with calibration?

Short derivations / computations
1) Write D_f(P||Q) for KL and TV and verify non‑negativity on a toy two‑point distribution.
2) Show post‑processing for a DP output: if M is (ε,δ)‑DP, then g∘M is (ε,δ)‑DP.
3) Derive Laplace scale for count sensitivity 1 at ε=1; compute expected absolute error.
4) For binary RR with ε, derive the unbiased estimator for p and its variance.
5) Given per‑group TPR/FPR, decide thresholds to approximate EO and report utility trade‑offs.

Coding prompts
- Implement gradient descent for linear regression; plot loss vs iterations for 3 learning rates.
- Use scikit‑learn Pipelines to prevent leakage when scaling and cross‑validating.
- Compare Logistic Regression, Linear SVM, and RBF SVM on a standardized dataset; report CV scores.
- Perform PCA then K‑Means on a dataset; visualize clusters in 2D.

---

## ADHD‑friendly structure and focus aids
- Make the first task tiny: “Open notebook and run first cell.” Start momentum.
- Externalize everything: today’s 3 tasks live as checkboxes in your note.
- Timebox decisions: if stuck choosing a model, pick the simplest baseline in 60 seconds.
- Environment cues: same place, same playlist, timer visible. Phone out of reach.
- Dopamine hooks: quick wins first (plot, baseline), then harder derivations.
- Buddy up: a 15‑minute daily “stand‑up” with a friend or TA to say what you’ll do.
- If‑then planning: “If I get distracted -> I stand up, breathe, and restart the timer.”
- Measure output, not time: count deliverables (plots, notes, scripts, tables), not minutes.

---

## Folder suggestions (optional)
- `prep/notes/` — daily notes by topic
- `prep/code/` — small scripts or notebooks per day
- `prep/project/` — mini‑project assets and report

---

## Next steps to tailor to CAS 751
If you can share the outline text (topics, grading, assignments), I’ll:
- Map each day directly to your syllabus modules
- Add assignment‑style questions and rubrics
- Include any required software (e.g., PyTorch vs TensorFlow) and reading checkpoints

Good luck—you’ve got this. Keep it light, concrete, and consistent.
