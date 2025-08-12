# SVMs, Decision Trees, and Ensembles — Study Guide

## 1) Core concepts (quick hits)
- SVM: margin maximization; hard vs soft margin; kernels (RBF)
- Hyperparameters: C (regularization), gamma (RBF width)
- Trees: impurity (Gini/entropy), depth/pruning, variance
- Ensembles: bagging (Random Forest), boosting (GB, XGBoost)

## 2) Intuition builders
- SVM margin trades off slack via C; RBF gamma controls locality
- Trees overfit without constraints; RF reduces variance via averaging
- Boosting fits residuals iteratively; sensitive to learning rate and depth

## 3) Practice questions
1) When does linear SVM rival logistic regression?
2) Compare RF vs GB in bias/variance and tuning complexity
3) What does feature importance mean, and when is it misleading?

## 4) Applied tasks
- Compare LogReg, LinearSVC, RBF SVC with standardized features
- Train DecisionTree, RandomForest, GradientBoosting; tune depth/estimators
- Plot learning curves and validation curves for C, gamma, max_depth

## 5) Pitfalls and checks
- Always scale features for SVM; watch out for class imbalance
- RF importances can be biased with categorical cardinality—use permutation importance
- Boosting can overfit; use early stopping and CV

## 6) Mini checklist
- [ ] Know how C and gamma affect SVM decision boundaries
- [ ] Can train RF/GB and interpret validation curves
- [ ] Use permutation importance for robust insights

---

# Practice Preparation Kit (focused for CAS 751)

## A) Tuning SVM hyperparameters
Example
- Standardized data: how do you pick C and gamma for RBF SVM?

How to think
- Log‑grid search; watch validation curve: high gamma overfits; low gamma underfits.

Why it matters
- Comparable baselines vs fairness/DP constrained models.

Steps
1) Pipeline with scaler + SVC
2) GridSearchCV over C, gamma

Analogy
- C = rule strictness; gamma = how local the lens is.

Try similar
- Plot decision boundaries for 2D toy data with varying gamma.

## B) RF vs GB trade‑offs
Example
- Choose between RF and GB for tabular data under limited tuning budget.

How to think
- RF: robust, less tuning; GB: stronger when tuned, sensitive to LR/depth.

Why it matters
- Reliable baselines for audits.

Steps
1) Start with RF; if plateaued, try GB with small LR and early stopping

Analogy
- RF = ensemble of generalists; GB = focused specialists.

Try similar
- Learning curves for both methods on same dataset.
