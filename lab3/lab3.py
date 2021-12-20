import numpy as np

def encrypt (m, e, n) :
    return (m ** e) % n

def gcd (a, b) :
    v, v0, u, u0 = 1, 0, 0, 1
    while b :
        q = a // b
        a, b = b, a % b
        v, v0 = v0, v - v0 * q
        u, u0 = u0, u - u0 * q
    return (a, u, v)

def chineserem (lC, ln, Me) :
    n = np.prod(ln)
    lN = [n / ni for ni in n]
    lM = [gcd(Ni, ni)[2] for Ni, ni in zip(lN, ln)]
    C = np.prod([Me * Ni * Mi for Ni, Mi in zip(lN, lM)])
    return C

