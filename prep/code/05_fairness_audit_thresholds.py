import numpy as np
from sklearn.metrics import confusion_matrix, roc_curve, precision_recall_curve

# Simple group metrics and threshold tuning for equalized odds (approx) demo

def group_metrics(y_true, y_score, groups, threshold=0.5):
    y_pred = (y_score >= threshold).astype(int)
    metrics = {}
    for g in np.unique(groups):
        mask = (groups == g)
        tn, fp, fn, tp = confusion_matrix(y_true[mask], y_pred[mask]).ravel()
        tpr = tp / (tp + fn + 1e-12)
        fpr = fp / (fp + tn + 1e-12)
        metrics[g] = dict(tpr=tpr, fpr=fpr, tp=tp, fp=fp, tn=tn, fn=fn)
    return metrics


def tune_thresholds_equalized_odds(y_true, y_score, groups, grid=None):
    grid = grid or np.linspace(0.1, 0.9, 17)
    best = None
    for t0 in grid:
        for t1 in grid:
            t = np.where(groups == 0, t0, t1)
            y_pred = (y_score >= t).astype(int)
            m0 = group_metrics(y_true, y_score, groups, threshold=t0)[0]
            m1 = group_metrics(y_true, y_score, groups, threshold=t1)[1]
            gap = abs(m0['tpr'] - m1['tpr']) + abs(m0['fpr'] - m1['fpr'])
            acc = (y_pred == y_true).mean()
            score = -gap + 0.1 * acc
            if (best is None) or (score > best[0]):
                best = (score, t0, t1, gap, acc, m0, m1)
    return best


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    n = 5000
    # synthetic: two groups with different base rates
    groups = rng.integers(0, 2, size=n)
    logits = rng.normal(0, 1, size=n) + (groups * 0.5)
    y_true = (logits + rng.normal(0, 1, size=n) > 0).astype(int)
    # imperfect score with noise
    y_score = logits + rng.normal(0, 1.0, size=n)

    base = group_metrics(y_true, y_score, groups, threshold=0.5)
    print("Base (single threshold=0.5) group metrics:")
    print(base)

    best = tune_thresholds_equalized_odds(y_true, y_score, groups)
    score, t0, t1, gap, acc, m0, m1 = best
    print(f"Best thresholds t0={t0:.2f}, t1={t1:.2f}: gap={gap:.3f}, acc={acc:.3f}")
    print("Group 0:", m0)
    print("Group 1:", m1)
