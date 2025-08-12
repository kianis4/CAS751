# Local Differential Privacy (LDP) — Study Guide

Covers: Local trust models, mechanisms (randomized response, unary encoding, RAPPOR), estimation under LDP.

## 1) Core concepts
- LDP definition: For mechanism M run on a single record x, P[M(x)∈S] ≤ e^{ε} P[M(x')∈S] for all x,x'.
- Trust model: no trusted curator; privatization at the client.
- Mechanisms: k‑ary randomized response, unary/count encoding, hashing tricks.

## 2) Estimation under LDP
- Minimax risk degrades with ε; information‑theoretic lower bounds.
- Bias/variance corrections for randomized response estimators.

## 3) Practice questions
1) Contrast central DP vs LDP in terms of utility and deployment.
2) Derive unbiased estimator for Bernoulli mean using RR.
3) How does domain size k affect error in k‑RR?

## 4) Applied tasks
- Implement binary randomized response; estimate mean across n users; compute bias/variance vs ε.
- k‑ary RR simulation; show error vs k and ε.

## 5) Pitfalls and checks
- Hash collisions in sketch‑based LDP schemes; calibration is tricky.
- Privacy budget fragmentation when collecting many attributes.

## 6) Mini checklist
- [ ] Understand LDP vs central DP trade‑offs
- [ ] Can derive/apply RR estimators
- [ ] Can simulate accuracy vs ε, k, n

---

# Practice Preparation Kit (focused for CAS 751)

## A) Binary randomized response estimator
Example
- Each user reports \tilde X with RR at ε; derive unbiased estimator for p=Pr[X=1].

How to think
- RR flips with probabilities tied to ε; invert expectation to solve for p.

Why it matters
- Basic building block for LDP analytics.

Steps
1) Write Pr[\tilde X=1]=p·π_1+(1−p)·π_0
2) Solve for p in terms of observed mean and π’s

Try similar
- Extend to k‑ary RR and derive estimator.

## B) Error vs domain size
Example
- Simulate k‑RR; plot MSE vs k for fixed n, ε.

How to think
- Larger k inflates variance; need more users or structure.

Why it matters
- Feasibility assessment under LDP.

Steps
1) Generate synthetic data
2) Apply k‑RR and estimate; compute MSE
