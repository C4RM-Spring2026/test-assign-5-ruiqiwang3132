import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    t = np.arange(1, n + 1)
    c = face * couponRate / ppy
    disc = (1 + y / ppy) ** t
    return np.sum(c / disc) + face / disc[-1]
