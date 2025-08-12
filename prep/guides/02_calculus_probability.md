# Calculus, Probability, and Statistics — Study Guide

## 1) Core concepts (quick hits)
- Gradients/Jacobians; chain rule; convexity intuition
- Loss surfaces; stationary points; Hessian (curvature)
- Random variables, expectation, variance, covariance
- Common distributions: Bernoulli, Binomial, Gaussian
- Bayes rule; MLE vs MAP; likelihood vs prior vs posterior
- Law of large numbers; central limit theorem (intuition)

## 2) Intuition builders
- Gradient is the direction of steepest ascent; −gradient for descent
- MAP is MLE with a regularizer implied by the prior
- Variance adds for independent noise; covariance tracks dependency

## 3) Derivations you should be able to do
- ∇w (1/n)||Xw − y||^2 = (2/n) X^T (Xw − y)
- Logistic regression NLL and gradient for one sample (x,y)
- Derive mean/variance of a Bernoulli and Gaussian

## 4) Worked example
Show that ridge regression gives (X^T X + λI) w = X^T y. Hint: add λ||w||^2 to least squares objective and differentiate.

## 5) Practice questions
Conceptual
1) Why does feature scaling help gradient descent?
2) What does a negative off‑diagonal in covariance mean?
3) Contrast confidence intervals vs prediction intervals.

Short problems
1) Derive the gradient for logistic regression with L2 penalty.
2) Compute E[X], Var(X) for Binomial(n,p).
3) Show that if X and Y are independent, Cov(X,Y)=0.

Applied
- Estimate mean/variance from simulated Gaussian samples and compare to true values.
- For a binary dataset, fit logistic regression and visualize decision boundary.

## 6) How to apply in ML projects
- Normalize features; pick learning rates based on loss curvature.
- Use regularization (L2/L1) to reduce variance; tune via CV.
- Report uncertainty with CV std; for probabilistic outputs, calibrate.

## 7) Pitfalls and checks
- Don’t mix test data during scaling/feature selection.
- Beware class imbalance when using accuracy; prefer F1/ROC‑AUC.
- Check gradient sign and magnitude; plot loss to verify descent.

## 8) Mini checklist
- [ ] Comfortable with gradients and basic likelihoods
- [ ] Can derive ridge solution and LogReg gradient
- [ ] Know how to calibrate and validate probabilistic models

---

# Practice Preparation Kit (focused for CAS 751)

Format: Example → How to think → Why it matters (CAS 751) → Steps → Analogy → Try similar.

## A) Gradient of MSE and scaling
Example
- Derive ∇w L where L= (1/2n)||Xw−y||^2 and explain how feature scaling affects step sizes.

How to think
- Gradient is X^T(Xw−y)/n; large feature scales stretch the landscape ⇒ small LR needed.

Why it matters
- Proper scaling stabilizes private/regularized training and speeds convergence.

Steps
1) Expand L; differentiate using chain rule
2) Note conditioning via X^T X
3) Argue scaling reduces condition number

Analogy
- Hiking on a tilted bowl; scaling flattens the steep axis.

Try similar
- Show why standardizing features helps logistic regression optimization.

## B) Logistic regression NLL gradient
Example
- For y∈{0,1}, σ(z)=1/(1+e^{−z}), derive ∇w ℓ(w) for one sample (x,y).

How to think
- ℓ=−[y log σ(x^T w)+(1−y) log(1−σ(x^T w))]; gradient is (σ−y)x.

Why it matters
- Forms the building block for private SGD and regularized training.

Steps
1) Compute dℓ/dz with z=x^T w
2) Use dz/dw = x
3) Add L2 gradient if needed: +λw

Analogy
- Prediction error (σ−y) pushes weights along x.

Try similar
- Write gradient for multinomial logistic regression for class k.

## C) Bayes, MLE, MAP
Example
- For Gaussian likelihood with Gaussian prior, derive MAP and show it equals ridge.

How to think
- Prior adds a quadratic penalty; MAP = argmax posterior = argmin NLL+penalty.

Why it matters
- Connects regularization to probabilistic assumptions; used in DP analysis.

Steps
1) Write log posterior
2) Differentiate and set to zero
3) Identify (X^T X+λI)w=X^T y

Analogy
- Prior acts like a spring pulling weights to zero.

Try similar
- Derive MAP for Laplace prior (L1 penalty) qualitatively.

## D) Expectation/variance quick checks
Example
- For Binomial(n,p), find E[X], Var(X). What happens under CLT as n grows?

How to think
- Use known forms np, np(1−p); CLT ⇒ normalized sum ~ Gaussian.

Why it matters
- Sanity‑check simulated stats and confidence reasoning.

Steps
1) Recall mgf or known formulas
2) Standardize (X−np)/√(np(1−p))

Analogy
- Many small independent effects blur into a bell curve.

Try similar
- Compute mean/var for Poisson(λ) and compare to Gaussian approx for large λ.
