# Information Theory Basics for CAS 751 — Study Guide

Scope: f‑divergences, data-processing inequalities (DPI, SDPI), mutual information, channel capacity, rate‑distortion (at a glance).

## 1) Core definitions
- f‑divergence: D_f(P||Q) = E_Q[f(dP/dQ)] for convex f, f(1)=0; includes KL, TV, Hellinger, chi‑square.
- DPI: For Markov chain X→Y→Z, D_f(P_{XZ} || Q_{XZ}) ≤ D_f(P_{XY} || Q_{XY}). Intuition: processing cannot increase information.
- Strong DPI (SDPI): D_f(P_{XZ} || Q_{XZ}) ≤ η D_f(P_{XY} || Q_{XY}) for some contraction η<1 for a given channel.
- Mutual information I(X;Y) = D_{KL}(P_{XY} || P_X P_Y); conditional MI; chain rule.
- Channel capacity C = max_{P_X} I(X;Y); rate‑distortion R(D) = min_{P_{\hat X|X}: E[d(X,\hat X)]≤D} I(X; \hat X).

## 2) Intuition
- f‑divergence family offers smoothness and tail sensitivities to choose from.
- SDPI: some channels “wash out” information at a definite rate; powerful for generalization/privacy bounds.
- Capacity/Rate‑Distortion: two optimization lenses on information flow (limits of communication/inference under constraints).

## 3) Key results to know (names/forms)
- Pinsker: TV(P,Q) ≤ sqrt(0.5 KL(P||Q)).
- Data processing for MI: I(X;Z) ≤ I(X;Y) for X→Y→Z.
- Contraction coefficients (Dobrushin, KL‑contraction) for SDPI.

## 4) Practice questions
1) Give two examples of f generating KL and TV. What properties differ?
2) State DPI for MI and provide a one‑paragraph proof sketch.
3) Explain SDPI and how contraction helps derive generalization or privacy bounds.

## 5) Applied tasks
- Compute empirical f‑divergences (KL, JS, TV) between two fitted Gaussians; compare sensitivity.
- Simulate a binary symmetric channel; estimate I(X;Y) as a function of crossover p.
- Use an SDPI‑style argument to bound the effect of a noisy channel on hypothesis testing error.

## 6) Pitfalls and checks
- KL is asymmetric; choose divergence to match problem geometry.
- Estimating MI from finite samples is hard; prefer plug‑in/simple parametric setups for practice.
- Don’t overfit SDPI constants; understand the channel assumptions.

## 7) Mini checklist
- [ ] Can define/compare common f‑divergences
- [ ] Can state DPI/SDPI and explain their role
- [ ] Can run a small MI or divergence simulation

---

# Practice Preparation Kit (focused for CAS 751)

## A) Recognizing f‑divergences
Example
- Show that KL and TV are f‑divergences by providing their f functions.

How to think
- For KL: f(t)=t log t; for TV: f(t)=1/2|t−1| (up to measure conventions).

Why it matters
- Lets you apply general DPI/SDPI tools across divergences.

Steps
1) Write D_f(P||Q)=E_Q[f(dP/dQ)]
2) Plug in Radon‑Nikodym derivative

Analogy
- Different lenses measuring distribution gap.

Try similar
- Hellinger with f(t)=(√t−1)^2.

## B) DPI proof sketch for MI
Example
- Prove I(X;Z)≤I(X;Y) for X→Y→Z.

How to think
- Use chain rule: I(X;Y,Z)=I(X;Z)+I(X;Y|Z)=I(X;Y). Nonnegativity gives result.

Why it matters
- Validates bounds used in generalization/privacy.

Steps
1) Write joint chain rule
2) Rearrange terms

Analogy
- Processing can’t create information out of thin air.

Try similar
- Apply DPI to f‑divergences other than KL.

## C) SDPI intuition
Example
- For a binary symmetric channel with flip prob p, argue a contraction factor η(p) for KL.

How to think
- Noisy channels shrink divergences; look up known contraction bounds.

Why it matters
- Tool to bound information leakage after noise mechanisms.

Steps
1) Define channel; express output distributions
2) Use known KL contraction inequality

Analogy
- Fog that blurs distinctions.

Try similar
- Simulate MI vs p and observe monotone decrease.
