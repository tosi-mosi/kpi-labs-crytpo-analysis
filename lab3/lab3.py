import numpy as np

def encrypt (m, e, n) :
    return pow(m, e, n)

def gcd (a, b) :
    v, v0, u, u0 = 1, 0, 0, 1
    while b :
        q = a // b
        a, b = b, a % b
        v, v0 = v0, v - v0 * q
        u, u0 = u0, u - u0 * q
    return (a, u, v)

#system of following type:
#C_1 = M^e (mod n_1)
#. . . . . . . . . .
#C_k = M^e (mon n_k)
#
#lC = [C_1, ... , C_k]
#ln = [n_1, ... , n_k]
def chineserem (lC, ln) :
    n = np.prod(ln)
    lN = [n / ni for ni in n]
    lM = [gcd(Ni, ni)[2] for Ni, ni in zip(lN, ln)]
    C = np.sum([Ci * Ni * Mi for Ci, Ni, Mi in zip(Ci, lN, lM)]) % n
    return C

#sense of arguments same as in chineserem
def SE_attack (lC, ln, e) :
    C = chineserem(lC, ln)
    M = C ** (1 / float(e))
    return M

def read_params (file) :
    params = file.readlines()
    lC = []
    ln = []
    for line in params :
        if line[0] == 'C' :
            lC.append(line)
        if line[0] == 'N' :
            lN.append(line)
    return lC, ln

#meeting in the middle
#e is stated to be 65537
def MitM_attack (C, n, e=65537, l=20) :
    X = []
    S = 0
    C_S = 0

    for T in range(0, 2 ** l + 1) :
        X.append(encrypt(T, e, n))

    for S in range(0, 2 ** l + 1) :
        try :
            #C_S = C * S^(-e) mod n
            C_S = pow(C * gcd(X[S])[2], 1, n)
            T = X.index(C_S)
            #if successful return plaintext M = T * S
            return T * S
        except ValueError :
            pass

    return "no plaintext found"

