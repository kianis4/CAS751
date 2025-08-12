import math
import numpy as np
from typing import Tuple

# Simple RDP accountant for subsampled Gaussian mechanism (very rough; for intuition)
# Reference formulas omitted—this uses a toy approximation for didactic purposes only.


def rdp_gaussian_subsampled(q: float, sigma: float, steps: int, alphas=(2, 3, 5, 10, 20)):
    # Toy: epsilon_alpha ≈ steps * q**2 * alphas / (2 * sigma**2)
    # Do NOT use for real accounting. Use Opacus/TF Privacy in practice.
    eps = {a: steps * (q ** 2) * a / (2 * sigma ** 2) for a in alphas}
    return eps


def rdp_to_dp(eps_alpha: dict, delta: float) -> Tuple[float, float]:
    # Convert by minimizing over alphas: eps = min_a (eps_a + log(1/delta)/(a-1))
    best = math.inf
    best_a = None
    for a, ea in eps_alpha.items():
        cand = ea + math.log(1.0 / delta) / (a - 1)
        if cand < best:
            best = cand
            best_a = a
    return best, best_a


# Toy DP-SGD training on logistic regression (synthetic)

def dp_sgd_demo(n=5000, d=10, epochs=5, batch_size=128, lr=0.5, C=1.0, sigma=1.2, delta=1e-5, seed=0):
    rng = np.random.default_rng(seed)
    X = rng.normal(0, 1, size=(n, d))
    w_true = rng.normal(0, 1, size=(d,))
    logits = X @ w_true
    y = (logits + rng.normal(0, 1, size=n) > 0).astype(int)

    w = np.zeros(d)
    steps = 0
    q = batch_size / n

    def sigmoid(z):
        return 1.0 / (1.0 + np.exp(-z))

    for _ in range(epochs):
        idx = rng.permutation(n)
        for start in range(0, n, batch_size):
            batch = idx[start:start+batch_size]
            xb = X[batch]
            yb = y[batch]
            # per-example gradients
            preds = sigmoid(xb @ w)
            grads = ((preds - yb)[:, None] * xb)  # shape (b,d)
            # clip per-example
            norms = np.linalg.norm(grads, axis=1, keepdims=True) + 1e-12
            scale = np.minimum(1.0, C / norms)
            grads = grads * scale
            gbar = grads.mean(axis=0)
            # add Gaussian noise
            noise = rng.normal(0, sigma * C / batch_size, size=gbar.shape)
            g_tilde = gbar + noise
            # update
            w -= lr * g_tilde
            steps += 1

    # privacy accounting (toy)
    eps_alpha = rdp_gaussian_subsampled(q=q, sigma=sigma, steps=steps)
    eps, alpha = rdp_to_dp(eps_alpha, delta)
    # quick utility check
    preds = (X @ w > 0).astype(int)
    acc = (preds == y).mean()
    return acc, eps, alpha, steps


if __name__ == "__main__":
    acc, eps, alpha, steps = dp_sgd_demo()
    print(f"DP-SGD toy run: acc={acc:.3f}, eps≈{eps:.2f} at alpha={alpha}, steps={steps}")
    print("NOTE: Toy accountant; for real use, rely on a vetted library.")
