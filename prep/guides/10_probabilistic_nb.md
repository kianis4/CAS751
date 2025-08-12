# Probabilistic Modeling & Naive Bayes — Study Guide

## 1) Core concepts (quick hits)
- Generative vs discriminative models; likelihood and priors
- Naive Bayes assumptions; GaussianNB, MultinomialNB, BernoulliNB
- MAP estimation; smoothing (Laplace)
- Probabilistic outputs and calibration

## 2) Intuition builders
- NB strong independence assumption can be OK for text (bag of words)
- MultinomialNB aligns with term counts; GaussianNB with continuous features

## 3) Derivations
- Posterior ∝ prior × likelihood; log‑space computations
- MAP with Dirichlet prior for multinomial (adds smoothing)

## 4) Practice questions
1) When does NB outperform logistic regression?
2) How does smoothing affect rare features?
3) Why might NB be poorly calibrated, and how to fix it?

## 5) Applied tasks
- Compare GaussianNB/MultinomialNB vs LogReg on synthetic/text‑like data
- Show calibration plots; apply isotonic/Platt scaling if needed

## 6) Pitfalls and checks
- Feature scaling for GaussianNB; proper count preprocessing for MultinomialNB
- Avoid leakage in vectorization; fit vectorizer within CV pipeline

## 7) Mini checklist
- [ ] Understand NB variants and assumptions
- [ ] Can compare NB vs LogReg and calibrate outputs
- [ ] Fit text/vectorization safely within CV

---

# Practice Preparation Kit (focused for CAS 751)

## A) When NB wins
Example
- On bag‑of‑words with many sparse features, NB beats LogReg with little tuning. Why?

How to think
- Independence + multinomial generative story matches data; LogReg needs more data/tuning.

Why it matters
- Strong baseline under privacy constraints and limited tuning.

Steps
1) Vectorize text (inside Pipeline)
2) Compare MultinomialNB vs LogReg

Analogy
- A model designed for counts vs a generic linear classifier.

Try similar
- Add smoothing and see rare‑word effects.

## B) Calibration of NB
Example
- NB is overconfident; fix calibration.

How to think
- Fit a calibrator on validation folds; report Brier and reliability.

Why it matters
- Thresholding and fairness need calibrated scores.

Steps
1) CalibratedClassifierCV with isotonic/Platt
2) Evaluate before/after

Analogy
- Re‑scaling a miscalibrated meter.

Try similar
- Group‑wise calibration comparisons.
