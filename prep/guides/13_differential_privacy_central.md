# Differential Privacy (Central) — Study Guide

Covers: Definitions, mechanisms (Laplace/Gaussian), properties (composition, post‑processing), privacy accounting, private GD/SGD.

## 1) Core definitions
- (ε,δ)‑DP: For any neighboring datasets D,D', and any event S, P[M(D)∈S] ≤ e^{ε} P[M(D')∈S] + δ.
- Sensitivity Δ: max change in query under one record change; calibrates noise.
- Mechanisms: Laplace(Δ/ε) for L1‑sensitivity; Gaussian(σ) for L2 with (ε,δ)‑DP.

## 2) Fundamental properties
- Post‑processing invariance: DP guarantees survive any randomized mapping of outputs.
- Composition: privacy losses add; advanced/optimal composition gives tighter bounds.
- Privacy amplification by subsampling: SGD minibatching reduces effective ε.

## 3) Private learning
- DP‑SGD: clip per‑example gradient to norm C; add Gaussian noise; track privacy via RDP or moments accountant.
- Key knobs: clipping norm C, noise multiplier σ, batch size, steps; target (ε,δ).

## 4) Practice questions
1) Derive Laplace noise scale for a count query with sensitivity 1 at ε=1.
2) Explain why post‑processing holds and give an example.
3) Outline DP‑SGD and how you’d choose C and σ for a target budget.

## 5) Applied tasks
- Implement a simple count/mean query with Laplace/Gaussian noise; empirically check DP inequality on samples.
- Train logistic regression with DP‑SGD (or use a library) on a small dataset; report accuracy vs ε.
- Use RDP accountant to convert noise schedule to (ε,δ) after T steps.

## 6) Pitfalls and checks
- Mis‑calibrated sensitivity ⇒ broken guarantees.
- Reporting too many stats (composition!) silently burns budget.
- Keep δ ≪ 1/n; log final (ε,δ), seed, clipping norm, steps.

## 7) Mini checklist
- [ ] Can state (ε,δ)‑DP and compute noise scales
- [ ] Understand composition and amplification at a high level
- [ ] Can run/interpret a small DP‑SGD experiment

---

# Practice Preparation Kit (focused for CAS 751)

## A) Calibrating Laplace/Gaussian noise
Example
- Count query with sensitivity 1 at ε=1: compute Laplace scale; for Gaussian with δ=1e−5, outline σ selection.

How to think
- Laplace: b=Δ/ε; Gaussian: use analytic Gaussian mechanism bounds with L2 sensitivity.

Why it matters
- First step to correct DP queries.

Steps
1) Identify sensitivity
2) Apply mechanism formula

Analogy
- Choosing the right thickness of privacy “fog.”

Try similar
- Mean query with bounded features.

## B) Post‑processing invariance
Example
- Show that squaring a DP output doesn’t change ε,δ.

How to think
- DP bound is over output distributions; measurable maps preserve inequalities.

Why it matters
- Safe to transform DP outputs; don’t double‑count privacy.

Steps
1) Write inequality for sets and their preimages

Try similar
- Randomized rounding of a DP mean.

## C) DP‑SGD knobs
Example
- Given target ε≈5 at δ=1e−5, discuss choices for (C, σ, batch size, steps).

How to think
- Higher σ, fewer steps, lower sampling rate → lower ε; trade vs utility.

Why it matters
- Practical private training.

Steps
1) Fix dataset size n
2) Use RDP accountant to sweep σ and steps
