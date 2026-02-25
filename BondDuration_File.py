import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    n = m * ppy
    t = np.arange(1, n + 1)

    coupon = face * couponRate / ppy
    cf = np.ones(n) * coupon
    cf[-1] += face

    discount = 1 / (1 + y / ppy) ** t
    pvcf = cf * discount

    return np.sum(t * pvcf) / np.sum(pvcf)
