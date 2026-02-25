import numpy as np

def FizzBuzz(start, finish):
    n = np.arange(start, finish + 1)
    out = n.astype(object)

    m3 = (n % 3 == 0)
    m5 = (n % 5 == 0)

    out[m3] = "fizz"
    out[m5] = "buzz"
    out[m3 & m5] = "fizzbuzz"
    return out
