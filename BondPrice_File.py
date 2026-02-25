import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    k = np.arange(1, n + 1)
    r = y / ppy
    t = k / ppy

    c = face * couponRate / ppy
    cf = np.full(n, c, dtype=float)
    cf[-1] += face

    df = (1 + r) ** (-k)
    pv = cf * df

    return (t @ pv) / pv.sum()
