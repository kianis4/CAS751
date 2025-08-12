# CAS 751 Quick Cards — Formulas, Heuristics, and Pitfalls

This is a fast, scannable reference. Each card has: What, Why, How (recipe), Pitfalls, and Pointers (guide + code).

---

## Information Theory (f‑divergences, DPI/SDPI)
What
- f‑divergence: D_f(P||Q)=E_Q[f(dP/dQ)], f convex, f(1)=0. KL: f(t)=t log t; TV: f(t)=0.5|t−1|; Hellinger: f(t)=(√t−1)^2.
- DPI (MI): X→Y→Z ⇒ I(X;Z) ≤ I(X;Y). Pinsker: TV ≤ √(0.5 KL). SDPI: D_f(PK||QK) ≤ η D_f(P||Q).

Why (CAS 751)
- Formal handle on information loss and contraction. Used to bound leakage and generalization.

How (recipe)
1) Pick divergence matching geometry (KL for tails/likelihoods, TV for worst‑case probs).
2) For MI DPI proof: use chain rule I(X;Y,Z)=I(X;Z)+I(X;Y|Z) and non‑negativity.
3) For SDPI intuition: identify the channel; use known contraction bounds (e.g., BSC).

Pitfalls
- Estimating MI from small samples is unreliable—prefer parametric or synthetic demos.
- KL is asymmetric; choose direction consciously.

Pointers
- Guide: 12_information_theory_basics.md (Practice Kit A–C)
- Code: prep/code/01_divergences_mi.py

---

## Central Differential Privacy (ε,δ, mechanisms, composition)
What
- (ε,δ)‑DP: ∀ neighbors D,D', P[M(D)∈S] ≤ e^ε P[M(D')∈S]+δ. Δ: query sensitivity.
- Laplace noise scale b=Δ/ε (L1). Gaussian: choose σ via analytic bounds (L2).
- Post‑processing invariance; composition (basic/advanced); amplification by subsampling.

Why
- Rigorous privacy guarantees for statistics and learning.

How (recipe)
1) Bound sensitivity Δ (prove worst‑case change with one record).
2) Pick mechanism (Laplace/Gaussian) and calibrate noise from Δ, ε (and δ for Gaussian).
3) If multiple releases/steps: sum losses (or use advanced/RDP accountant).
4) Log (ε,δ), seeds, Δ assumptions, and number of releases.

Pitfalls
- Wrong Δ breaks guarantees; do not post hoc “tune” noise.
- Silent budget burn under composition; count every release.

Pointers
- Guide: 13_differential_privacy_central.md (Practice Kit A–C)
- Code: prep/code/02_dp_mechanisms.py

---

## Rényi DP and DP‑SGD (accounting)
What
- RDP: D_α(P||Q)=(1/(α−1)) log E_Q[(dP/dQ)^α); composes additively across steps.
- Convert to (ε,δ): ε = ε_α + log(1/δ)/(α−1), pick best α.
- DP‑SGD: per‑example clip to C, add Gaussian noise σ, track via RDP.

Why
- Tight, scalable accounting for iterative training.

How (recipe)
1) Choose batch size (rate q), clip C, noise σ, steps T.
2) Compute RDP per step and sum; convert to (ε,δ).
3) Sweep σ or T to hit target ε.

Pitfalls
- Forgetting subsampling amplification; not reporting α used.

Pointers
- Guide: 14_renyi_dp_private_sgd.md
- Code: prep/code/03_rdp_accountant_dp_sgd.py (didactic accountant)

---

## Local DP (randomized response, estimation)
What
- ε‑LDP: ∀x,x', P[M(x)∈S] ≤ e^ε P[M(x')∈S] (no trusted curator).
- Binary RR: p = e^ε/(e^ε+1). E[\tilde X] = (2p−1)E[X] + (1−p). Unbiased estimator recovers E[X].
- k‑RR: generalizes to categorical domains; variance ↑ with k.

Why
- Client‑side privacy where central trust is impossible.

How (recipe)
1) Pick RR variant (binary/k‑ary); compute p from ε.
2) Derive unbiased estimator by inverting expectation.
3) Simulate error vs ε, k, n to judge feasibility.

Pitfalls
- High variance at large k; careful with hash/sketch collisions.

Pointers
- Guide: 15_local_dp.md
- Code: prep/code/04_ldp_randomized_response.py

---

## Fairness (metrics, auditing, mitigation)
What
- Demographic parity (DP): P(Ŷ=1|A=a) equal.
- Equalized odds (EO): TPR and FPR equal; Equal opportunity (EOp): TPR equal.
- Incompatibility: EO vs calibration under different base rates.

Why
- Diagnose and mitigate disparate performance across groups.

How (recipe)
1) Compute per‑group TPR/FPR/PPV and calibration; visualize disparities.
2) Pick a target (EO/EOp/DP) and apply threshold adjustments; measure utility trade‑off.
3) Document choice and impact.

Pitfalls
- Simpson’s paradox (hidden subgroups), distribution shift, metric gaming.

Pointers
- Guide: 16_fairness.md
- Code: prep/code/05_fairness_audit_thresholds.py

---

## Math Quickies (you’ll actually use these)
What/How
- Projection onto Col(X): P = X(X^T X)^{-1}X^T; residual orthogonal.
- Ridge normal equation: (X^T X + λI)w = X^T y.
- Spectral norm inequalities: ||AB||_2 ≤ ||A||_2||B||_2; operator norm bounds sensitivity.
- PCA link: top eigenvector of X^T X maximizes variance; fit inside CV to avoid leakage.

Pitfalls
- Ill‑conditioning (fix via scaling/regularization). PCA leakage if fitted on full data.

Pointers
- Guides: 01_linear_algebra.md, 02_calculus_probability.md, 03_optimization.md
- Code: see prep/code/01_divergences_mi.py (PCA intuition via variance parts)
