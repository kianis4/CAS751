# Rényi Differential Privacy & Private SGD — Study Guide

Covers: Rényi DP (RDP), conversion to (ε,δ)‑DP, privacy accounting for DP‑SGD.

## 1) Core concepts
- Rényi divergence of order α>1: D_α(P||Q) = (1/(α−1)) log E_Q[(dP/dQ)^α].
- RDP: A mech M satisfies (α, ε(α))‑RDP if for all neighboring D,D', D_α(M(D)||M(D')) ≤ ε(α).
- Conversion: Given ε(α), derive (ε,δ) bounds by optimizing over α.

## 2) Why RDP for DP‑SGD?
- Composition across many steps becomes simple (add ε(α) values).
- Tight accounting vs naive composition; better utility at same privacy.

## 3) Practice questions
1) Define RDP and explain how it composes.
2) Sketch conversion from RDP to (ε,δ) and why we optimize over α.
3) For fixed noise multiplier and sampling rate, how do steps T affect ε?

## 4) Applied tasks
- Use a simple accountant (or library) to compute ε for DP‑SGD under various σ, batch sizes, and T.
- Plot ε vs utility (accuracy) trade‑offs.

## 5) Pitfalls and checks
- Don’t forget subsampling amplification in accounting.
- Report α grid and chosen α in final (ε,δ) report.

## 6) Mini checklist
- [ ] Can explain RDP and its advantage for composition
- [ ] Can perform a basic RDP→(ε,δ) conversion
- [ ] Can account privacy for a DP‑SGD training run

---

# Practice Preparation Kit (focused for CAS 751)

## A) RDP composition
Example
- Two mechanisms with ε_1(α), ε_2(α) satisfy RDP. What is ε_total(α)?

How to think
- Add them: ε_total=ε_1+ε_2 (same α), then convert to (ε,δ).

Why it matters
- Many‑step accounting for DP‑SGD.

Steps
1) Sum per‑step ε(α)
2) Optimize α for conversion

Try similar
- Include subsampling amplification effect.

## B) ε vs steps trade‑off
Example
- With fixed σ and batch size, how does ε grow with steps T?

How to think
- Roughly grows like √T (with amplification/RDP), better than linear naive comp.

Why it matters
- Budget training length.

Steps
1) Compute across T grid
2) Plot ε(T)
