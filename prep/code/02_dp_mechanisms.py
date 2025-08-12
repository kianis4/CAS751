import numpy as np

# Laplace mechanism for count/mean with L1 sensitivity Delta

def laplace_mechanism(true_value: float, epsilon: float, sensitivity: float = 1.0, rng=None):
    rng = rng or np.random.default_rng()
    scale = sensitivity / epsilon
    noise = rng.laplace(0.0, scale)
    return true_value + noise

# Analytic Gaussian mechanism placeholder (use simple sigma selection for demo)
# WARNING: For real use, prefer a vetted library; this is for intuition only.

def gaussian_mechanism(true_value: float, sigma: float, rng=None):
    rng = rng or np.random.default_rng()
    return true_value + rng.normal(0.0, sigma)

# Empirical DP check (very rough): estimate P[M(D) in S] and P[M(D') in S]

def empirical_dp_check(mech_fn, D, D_prime, S_low, S_high, trials=20000, **mech_kwargs):
    rng = np.random.default_rng(0)
    c1 = 0
    c2 = 0
    for _ in range(trials):
        o1 = mech_fn(D, rng=rng, **mech_kwargs)
        o2 = mech_fn(D_prime, rng=rng, **mech_kwargs)
        if S_low <= o1 <= S_high:
            c1 += 1
        if S_low <= o2 <= S_high:
            c2 += 1
    p1 = c1 / trials
    p2 = c2 / trials
    return p1, p2

if __name__ == "__main__":
    # Count query with sensitivity 1
    D = 100
    D_prime = 99
    eps = 1.0
    p1, p2 = empirical_dp_check(laplace_mechanism, D, D_prime, S_low=95, S_high=105, epsilon=eps, sensitivity=1.0)
    print("Empirical DP check (Laplace, eps=1.0) on interval [95,105]:")
    print(" P[M(D) in S]=", p1, " P[M(D') in S]=", p2, " ratio<= e^eps?", (p1/(p2+1e-12)) <= np.exp(eps)+1e-2)

    # Mean query demo (bounded data in [0,1])
    n = 1000
    data = np.random.default_rng(1).random(n)
    true_mean = data.mean()
    noisy_mean = laplace_mechanism(true_mean, epsilon=0.5, sensitivity=1.0/n)
    print(f"True mean={true_mean:.4f}, noisy mean (eps=0.5)={noisy_mean:.4f}")
