import numpy as np
from scipy.stats import norm

# KL between two univariate Gaussians N(m1,s1^2) and N(m2,s2^2)
def kl_gauss(m1, s1, m2, s2):
    return np.log(s2/s1) + (s1**2 + (m1-m2)**2)/(2*s2**2) - 0.5

# Symmetric TV bound via KL (Pinsker): TV <= sqrt(0.5 * KL)
def tv_bound_from_kl(kl):
    return np.sqrt(0.5 * kl)

# Jensen-Shannon divergence between univariate Gaussians (approx via sampling)
def js_divergence_samples(m1, s1, m2, s2, n=200000, seed=0):
    rng = np.random.default_rng(seed)
    x = rng.normal(m1, s1, size=n)
    y = rng.normal(m2, s2, size=n)
    # Estimate JS via definition using mixture M = 0.5(P+Q)
    # JS(P,Q) = 0.5 KL(P||M) + 0.5 KL(Q||M)
    # For univariate Gaussians, M is not Gaussian; do sampling-based estimate
    grid = np.linspace(min(x.min(), y.min()), max(x.max(), y.max()), 2000)
    px = norm.pdf(grid, m1, s1)
    qx = norm.pdf(grid, m2, s2)
    mx = 0.5*(px+qx)
    # numerical integration (trapz)
    # avoid log(0)
    eps = 1e-12
    kl_p_m = np.trapz(px * (np.log(px+eps) - np.log(mx+eps)), grid)
    kl_q_m = np.trapz(qx * (np.log(qx+eps) - np.log(mx+eps)), grid)
    return 0.5*(kl_p_m + kl_q_m)

# Empirical MI for BSC(p) with uniform X

def bsc_mi(p, n=200000, seed=0):
    rng = np.random.default_rng(seed)
    x = rng.integers(0, 2, size=n)
    noise = rng.binomial(1, p, size=n)
    y = x ^ noise
    # estimate MI via entropies
    def H(vec):
        counts = np.bincount(vec, minlength=2) / len(vec)
        probs = counts[counts > 0]
        return -np.sum(probs * np.log2(probs))
    hx = H(x)
    hy = H(y)
    hxy_counts = np.zeros((2,2))
    for xi, yi in zip(x, y):
        hxy_counts[xi, yi] += 1
    pxy = hxy_counts / n
    px = pxy.sum(axis=1, keepdims=True)
    py = pxy.sum(axis=0, keepdims=True)
    eps = 1e-12
    mi = np.sum(pxy * (np.log2(pxy+eps) - np.log2(px+eps) - np.log2(py+eps)))
    return mi

if __name__ == "__main__":
    print("Divergences for N(0,1) vs N(1,1):")
    kl = kl_gauss(0,1,1,1)
    print(" KL:", kl)
    print(" TV bound (Pinsker):", tv_bound_from_kl(kl))
    js = js_divergence_samples(0,1,1,1)
    print(" JS (approx):", js)

    print("\nMI of BSC(p):")
    for p in [0.0, 0.05, 0.1, 0.2, 0.3, 0.5]:
        print(f" p={p:.2f} -> I(X;Y)≈ {bsc_mi(p):.4f} bits")
