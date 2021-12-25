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
    C = pow(np.sum([Ci * Ni * Mi for Ci, Ni, Mi in zip(lC, lN, lM)]), 1, n) 
    return C

#sense of arguments same as in chineserem
def SE_attack (lC, ln, e) :
    C = chineserem(lC, ln)
    M = root(C, e)
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
    lim = 2 ** l 
    X = np.zeros(lim, dtype=object)
    
    #list of vaules T^e mod n, for T = {1..2^l}
    for T in range(1, lim + 1) :
        X[T - 1] = encrypt(T, e, n)
    
    print(X[:3])

    for S in range(1, lim + 1) :
        #C_S = C * S^(-e) mod n
        C_S = pow(C * gcd(X[S], n)[2], 1, n)
        #if successful return plaintext M = T * S
        if np.any(X == C_S) :
            T = np.where(X == C_S)[0][0]
            print (f'{hex(T)}')
            return T * S

    return "no plaintext found"

SE_location = "08-SE.txt"
MitM_location = "08-MitM.txt"

#SE attack
e = 3 #given in the text of the task
with open(SE_location, "r") as file_SE : 
    lC, ln = read_params(file_SE)
M = SE_attack(lC, ln, e)
print(f'Retieved plaintext: {hex(M)}')


#MitM attack
with open(MitM_location, "r") as file_MitM :
    lC, ln = read_params(file_MitM)
    #only one value for each list
#M = MitM_attack(lC[0], ln[0]) #running with default parameters
#if M is int :
#    print(f'Retrieved plaintext: {hex(M)}')
#else :
#    print(f'Faliure: {M}')

