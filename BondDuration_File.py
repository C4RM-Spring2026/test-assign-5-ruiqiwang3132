import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    r = y / ppy
    c = face * couponRate / ppy

    t = np.arange(1, n + 1)
    cf = np.full(n, c, dtype=float)
    cf[-1] = cf[-1] + face

    disc = (1.0 / (1.0 + r)) ** t
    pvcf = cf * disc
    price = np.sum(pvcf)

    dur_periods = np.sum(t * pvcf) / price
    return dur_periods / ppy
