import numpy as np

#python does not provide a sensible way
#to calculate root of a large integer
#therefore I decided to use a simle implementation
#based on bisection method
def root (x, n) :
    #choose initial boundaries for x^(1/n)
    b = 1
    while b ** n <= x :
        b *= 2
    a = b // 2

    while a < b :
        #bisection
        c = (a + b) // 2
        aux = c ** n
        #then either we are too low
        if a < c and aux < x :
            a = c
        #or too high
        elif b > c and aux > x :
            b = c
        #or we have found the root
        else :
            return c
    return c + 1

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
    lN = [n // ni for ni in ln]
    lM = [gcd(Ni, ni)[2] for Ni, ni in zip(lN, ln)]
    C = np.sum([Ci * Ni * Mi for Ci, Ni, Mi in zip(lC, lN, lM)]) % n
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
            lC.append(int(line[7:], 16))
        if line[0] == 'N' :
            ln.append(int(line[7:], 16))
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
            T = X.index(C_S) #throws ValueError exception if no match is found
            #if successful return plaintext M = T * S
            return T * S
        except ValueError :
            pass

    return "no plaintext found"

SE_location = "08-SE.txt"
MitM_location = "08-MitM.txt"

#SE attack
e = 3 #given in the text of the task
file_SE = open(SE_location, "r")
lC, ln = read_params(file_SE)
M = SE_attack(lC, ln, e)
print(f'Retieved plaintext: {M}')

