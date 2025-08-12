# Optimization for ML — Study Guide

## 1) Core concepts (quick hits)
- GD, SGD, mini‑batch, momentum, Nesterov
- Learning rate schedules; warmup; cosine/step decay
- Convex vs non‑convex; local minima/saddle points
- Line search intuition; Lipschitz constants (high level)
- Early stopping; regularization as implicit bias

## 2) Intuition builders
- Too large LR ⇒ divergence; too small ⇒ slow; use loss curves
- Momentum accumulates gradients; helps push through small valleys
- SGD noise helps escape shallow local minima

## 3) Derivations / must‑knows
- Convergence condition for GD on L‑smooth convex functions (intuition)
- Relationship between weight decay and L2 regularization
- Batch size vs variance trade‑off

## 4) Hands‑on
- Implement GD for linear regression (from scratch); try 3 learning rates
- Compare SGD vs full‑batch on runtime and convergence
- Add momentum; observe effect on oscillations

## 5) Practice questions
1) How do you choose an initial LR and adjust it?
2) Why does feature scaling speed up convergence?
3) When does early stopping act like regularization?

## 6) Pitfalls and checks
- Plot losses; if noisy/diverging, reduce LR or add scaling
- Shuffle data for SGD each epoch; set seeds for reproducibility
- Watch for exploding gradients (clip or lower LR)

## 7) Mini checklist
- [ ] Implemented GD/SGD once
- [ ] Can diagnose LR issues from loss curves
- [ ] Understand momentum and early stopping

---

# Practice Preparation Kit (focused for CAS 751)

## A) Diagnosing learning rate from curves
Example
- You run GD with LR={0.1, 0.01, 0.001}. Loss explodes for 0.1, flat for 0.001. Pick a good LR and justify.

How to think
- Aim for monotone but brisk decrease; try geometric search and watch first 10–20 steps.

Why it matters
- Private training budgets steps; bad LR wastes privacy.

Steps
1) Plot loss per epoch
2) Pick LR with fastest stable descent

Analogy
- Tuning car throttle: avoid stall (too low) and spin out (too high).

Try similar
- Add momentum and show it smooths oscillations.

## B) SGD vs full batch trade‑offs
Example
- Compare runtime and convergence on n=50k samples; when does SGD win?

How to think
- SGD reduces per‑step cost; noise can help generalize; use mini‑batches.

Why it matters
- DP‑SGD relies on mini‑batches and subsampling amplification.

Steps
1) Fix epochs
2) Compare wall time and final loss

Analogy
- Noisy compass that still points downhill on average.

Try similar
- Vary batch size and observe variance in updates.

## C) Early stopping as regularization
Example
- Validation loss starts rising after epoch 15; what to do and why?

How to think
- Stop at best validation; this limits effective complexity.

Why it matters
- Reduces overfitting and saves privacy budget.

Steps
1) Track train/val losses
2) Keep best weights

Analogy
- Baking: take out when just done, not overbaked.

Try similar
- Add weight decay and compare to early stopping alone.
