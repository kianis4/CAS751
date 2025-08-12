# Linear Algebra for ML — Study Guide

## 1) Core concepts (quick hits)
- Vectors/matrices, shapes, broadcasting
- Norms (L1/L2), inner product, cosine similarity
- Projections, orthogonality, orthonormal bases
- Matrix rank, range/null space
- Eigenvalues/eigenvectors; spectral decomposition
- SVD: UΣV^T; low-rank approximation
- Positive (semi)definiteness; quadratic forms

## 2) Intuition builders
- Projection = “shadow” on a subspace; residual is orthogonal
- SVD as rotation–stretch–rotation; top k singular vectors capture most variance
- Condition number ≈ sensitivity to noise; affects optimization stability

## 3) Derivations you should be able to do
- Projection of y onto span(X): X(X^T X)^{-1} X^T y
- Show (AB)^T = B^T A^T and ||Ax||_2 ≤ ||A||_2 ||x||_2
- For symmetric A: orthogonal eigenbasis; diagonalization A=QΛQ^T

## 4) Worked example
Given X ∈ R^{n×d} full column rank, prove the residual r=y−Xw* is orthogonal to columns of X for least squares w*.

Sketch: w* = argmin ||Xw−y||^2 ⇒ normal equation X^T(Xw*−y)=0 ⇒ X^T r = 0.

## 5) Practice questions
Conceptual
1) Why does PCA use eigenvectors of the covariance matrix?
2) When does a matrix have an inverse? What does rank deficiency imply?
3) How does SVD help with noisy data and overfitting?

Short problems
1) Compute eigenvalues/eigenvectors of [[2,1],[1,2]].
2) Given A=[[1,2],[0,1]], compute A^T A and its eigenvalues.
3) Show that columns of U in SVD are orthonormal.

Applied
- Build a small PCA on a dataset; visualize first two PCs and explained variance.
- Use low‑rank approximation to compress an image; compare reconstruction errors vs rank.

## 6) How to apply in ML projects
- Always check feature scales (norms) before distance‑based methods.
- Use PCA to de‑noise, visualize, or speed up models; retain 95% variance as a heuristic.
- If X^T X is ill‑conditioned, prefer regularization (ridge) or dimensionality reduction.

## 7) Pitfalls and checks
- Feature collinearity ⇒ unstable least squares; check VIF or singular values.
- Data leakage: fit PCA inside CV pipeline only.
- Don’t overinterpret PCs; they’re linear combos without labels.

## 8) Mini checklist
- [ ] Can compute projections and reason about orthogonality
- [ ] Understand eigen/SVD intuitively and algebraically
- [ ] Use PCA correctly inside a pipeline

---

# Practice Preparation Kit (focused for CAS 751)

Format per item: Example question → How to think → Why it matters (CAS 751) → Step‑by‑step → Quick analogy → Similar questions to try.

## A) Projections and residual orthogonality
Example question
- Given x = [2,1]^T and y = [3,4]^T, compute the projection of y onto span{x} and the residual r. Verify x^T r = 0.

How to think
- Projection = “shadow” of y onto the direction x. Residual is what’s left, perpendicular to x.

Why it matters (CAS 751)
- Least squares and many estimators rely on orthogonality of residuals. You’ll use this logic when proving optimality or sensitivity bounds in private optimization.

Step‑by‑step
1) p = (x^T y / x^T x) x
2) r = y − p
3) Check x^T r ≈ 0 (numerical round‑off is fine)

Quick analogy
- Flashlight casting y’s shadow on the line along x.

Try similar
- Project y = [1,2,3]^T onto span of x = [1,0,1]^T in R^3.
- With a matrix X ∈ R^{3×2} full column rank, write the projector P = X(X^T X)^{-1}X^T and project y = [1,0,1]^T.

## B) Norms and sensitivity (L1/L2)
Example question
- A query q(D) = a^T v where v is a data vector with each coordinate changing by at most 1 between neighboring datasets. What’s the L1‑ and L2‑sensitivity of q in terms of a?

How to think
- Sensitivity = worst‑case change. For linear forms, it’s the dual norm: L1 data change pairs with ||a||_∞; L2 with ||a||_2.

Why it matters (CAS 751)
- DP noise scales with sensitivity. Getting norms right is critical for correct privacy calibration.

Step‑by‑step
1) L1‑change ≤ 1 per coordinate ⇒ |Δq| ≤ ||a||_∞
2) L2‑change ≤ 1 in Euclidean norm ⇒ |Δq| ≤ ||a||_2

Quick analogy
- Dual norms are “best adversary grips” on your vector.

Try similar
- For q(D)=||v||_1, bound L1‑sensitivity when one coordinate can change by ±1.
- For matrix query q(D)=Av, give L2‑sensitivity in terms of operator norm ||A||_2.

## C) PSD matrices and quadratic forms
Example question
- Let A = [[2,−1], [−1,2]]. Show A is positive semidefinite and bound x^T A x between λ_min||x||_2^2 and λ_max||x||_2^2.

How to think
- Symmetric A diagonalizes: A=QΛQ^T. Quadratic form equals sum of λ_i times squared coordinates in eigenbasis.

Why it matters (CAS 751)
- Curvature bounds appear in optimization convergence and in sensitivity/utility trade‑offs under noise.

Step‑by‑step
1) Compute eigenvalues (both ≥0 ⇒ PSD)
2) Use λ_min, λ_max to bound x^T A x

Quick analogy
- A is a bowl whose steepness is set by eigenvalues.

Try similar
- Check PSD of covariance matrix Σ from a small dataset.
- For A = [[1,0],[0,3]], find λ_min, λ_max and bound x^T A x.

## D) Operator norm and composition bounds
Example question
- Given A and B, explain why ||AB||_2 ≤ ||A||_2 ||B||_2 and use it to bound ||A(Bx)|| for any x.

How to think
- Spectral norm is the max stretch of a unit vector. Two stretches compose multiplicatively.

Why it matters (CAS 751)
- Bounds propagate through pipelines: preprocessing then model; also used to upper‑bound sensitivity of composed maps.

Step‑by‑step
1) ||ABx||_2 ≤ ||A||_2 ||Bx||_2
2) ≤ ||A||_2 ||B||_2 ||x||_2

Quick analogy
- Two rubber bands in series; total stretch ≤ product of stretches.

Try similar
- Show ||A^k||_2 ≤ ||A||_2^k.
- If ||A||_2 ≤ 1 and ||B||_2 ≤ 1, what can you say about ||AB||_2?

## E) SVD and PCA linkage
Example question
- For centered data matrix X ∈ R^{n×d}, explain why the first right singular vector v_1 maximizes variance of Xw over ||w||_2=1, and compute the first principal component on a 2D toy set.

How to think
- PCA solves max_w ||Xw||_2^2 subject to ||w||_2=1 → top eigenvector of X^T X.

Why it matters (CAS 751)
- Dimensionality reduction for de‑noising and privacy‑utility trade‑offs; also to visualize and detect group disparities before fairness analysis.

Step‑by‑step
1) Form covariance C = (1/n) X^T X
2) Compute top eigenvector v_1
3) PC scores = X v_1

Quick analogy
- Rotating to the direction where the cloud is widest.

Try similar
- Manually compute PCA for three 2D points: (0,0), (1,1), (2,2).
- Compare PCA before vs after standardizing features with different scales.

## F) Rank, null space, and invertibility
Example question
- For A=[[1,2,3],[2,4,6],[1,1,1]], find rank(A), a basis for Null(A), and say if A^T A is invertible.

How to think
- Look for dependent rows/columns. Rank tells information content; null space are directions killed by A.

Why it matters (CAS 751)
- Inverse/conditioning affects stability of estimators and the noise you must add for privacy.

Step‑by‑step
1) Row‑reduce to find rank
2) Solve Ax=0 to get Null(A)
3) A^T A invertible iff columns of A are independent (full column rank)

Quick analogy
- Rank = number of independent “features”; null space = directions that disappear.

Try similar
- Construct a 3×2 full‑column‑rank matrix and write the projector onto its column space.
- Give an example where A has rank d−1 and explain consequences for least squares.
