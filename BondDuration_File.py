import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    k = np.arange(1, n + 1)

    c = face * couponRate / ppy
    cf = np.full(n, c, dtype=float)
    cf[-1] += face

    df = (1 + y / ppy) ** k
    pv = cf / df
    price = pv.sum()

    weights = pv / price
    time_years = k / ppy

    return (weights * time_years).sum()
