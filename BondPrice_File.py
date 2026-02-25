import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    k = np.arange(1, n + 1)
    r = y / ppy

    c = face * couponRate / ppy
    cf = np.full(n, c, dtype=float)
    cf[-1] += face

    df = (1.0 + r) ** (-k)
    return float(np.sum(cf * df))
