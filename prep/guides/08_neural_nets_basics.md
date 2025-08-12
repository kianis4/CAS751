# Neural Networks (Lite) — Study Guide

## 1) Core concepts (quick hits)
- Perceptron/MLP; layers, neurons, activations (ReLU/sigmoid)
- Losses: MSE vs cross‑entropy; softmax for multi‑class
- Backpropagation (high level); weight initialization; regularization (dropout/L2)
- Optimization: SGD, Adam; batch size and LR schedules

## 2) Intuition builders
- ReLU helps gradients flow; sigmoid saturates
- Overparameterized nets can generalize with regularization and early stopping

## 3) Practice questions
1) When does MLP beat logistic regression?
2) Why do we standardize inputs for MLPs?
3) What’s the effect of dropout rate on training/validation curves?

## 4) Applied tasks
- Train a small MLP (sklearn MLPClassifier or PyTorch) on a tabular dataset
- Compare to logistic regression; plot learning curves
- Tune hidden sizes, activation, LR; record results in an experiment table

## 5) Pitfalls and checks
- Monitor validation loss for early stopping
- Scale inputs; check for label leakage and target normalization errors
- Set seeds; log configs for reproducibility

## 6) Mini checklist
- [ ] Can train a simple MLP and compare baselines
- [ ] Can tune core hyperparameters (hidden size, LR)
- [ ] Can diagnose over/underfitting from curves

---

# Practice Preparation Kit (focused for CAS 751)

## A) Hidden size and overfitting
Example
- Increase hidden units until validation loss worsens; pick a good size.

How to think
- Capacity vs data size; use early stopping and weight decay.

Why it matters
- Sensible baselines before adding DP noise.

Steps
1) Train with sizes {16,32,64}
2) Plot train/val losses; pick best

Analogy
- Fitting a suit: too small vs too large.

Try similar
- Add dropout and compare curves.

## B) Learning rate schedules
Example
- Try constant vs cosine decay; compare convergence.

How to think
- Start higher, end lower; smoother convergence.

Why it matters
- Helps when DP noise makes optimization harder.

Steps
1) Train with two schedules
2) Compare accuracy and stability

Analogy
- Starting fast, then cruising.

Try similar
- Warmup + cosine vs step decay.
