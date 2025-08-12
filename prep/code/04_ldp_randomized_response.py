import numpy as np

# Binary randomized response with privacy parameter epsilon

def rr_binary_bits(x: np.ndarray, epsilon: float, rng=None):
    rng = rng or np.random.default_rng()
    p = np.exp(epsilon) / (np.exp(epsilon) + 1.0)
    # flip with prob (1-p)
    flips = rng.random(size=x.shape) > p
    return x ^ flips


def rr_binary_estimator(x_tilde: np.ndarray, epsilon: float) -> float:
    p = np.exp(epsilon) / (np.exp(epsilon) + 1.0)
    mean_tilde = x_tilde.mean()
    # E[\tilde X] = p * E[X] + (1-p) * (1 - E[X]) = (2p-1) E[X] + (1-p)
    denom = max(1e-12, (2 * p - 1))
    est = (mean_tilde - (1 - p)) / denom
    return np.clip(est, 0.0, 1.0)


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    n = 10000
    p_true = 0.3
    x = (rng.random(n) < p_true).astype(int)
    for eps in [0.5, 1.0, 2.0]:
        x_tilde = rr_binary_bits(x, eps, rng=rng)
        est = rr_binary_estimator(x_tilde, eps)
        print(f"eps={eps}: true={p_true:.3f}, est={est:.3f}")
