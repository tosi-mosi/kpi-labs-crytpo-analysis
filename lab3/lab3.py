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
