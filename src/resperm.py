from dataclasses import dataclass
import numpy as np
from numpy.polynomial.polynomial import polyfit, polyval


@dataclass
class RespermResult:
    k_star: int  # the observation number in which the change-point was detected (indexed from 0)
    chp: float  # the value of change-point (on X-axis)
    d: float  # the Cohen's d value for the change-point


def resperm(x, y, N_perm=1000, seed=1992):
    if N_perm < 100:
        raise ValueError("Too few permutations!")

    n = len(x)
    if n != len(y):
        raise ValueError("Unequal lengths of x and y")
    if n < 21:
        raise ValueError("Too few observations")

    first_k = 10
    last_k = n - 10

    yf = polyval(x, polyfit(x, y, 1))
    res = yf - x

    cohen_ds = []
    np.random.seed(seed)
    for k in range(first_k, last_k + 1):
        b1 = polyfit(x[:k], y[:k], 1)[-1]
        b2 = polyfit(x[k:], y[k:], 1)[-1]

        b1s = []
        b2s = []
        for _ in range(N_perm):
            ys = yf + np.random.permutation(res)
            b1s.append(polyfit(x[:k], ys[:k], 1)[-1])
            b2s.append(polyfit(x[k:], ys[k:], 1)[-1])

        S1 = np.var(b1s)
        S2 = np.var(b2s)
        sigma_b = (k - 1) * S1 + (n - k - 1) * S2
        sigma_b = np.sqrt(sigma_b / (n - 2))
        d = np.abs(b2 - b1) / sigma_b
        cohen_ds.append(d)

    max_idx = int(np.argmax(cohen_ds))
    k_star = max_idx + first_k - 1

    return RespermResult(k_star, x[k_star], cohen_ds[max_idx])


if __name__ == "__main__":
    # Simple example
    y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    x = np.arange(1, len(y) + 1)
    result = resperm(x, y)
    print(result)
