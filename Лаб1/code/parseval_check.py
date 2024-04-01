from a_b_c_counter import *


#  parseval for F
def parseval_F(f, N):

    a = a_coef(f, N)
    b = b_coef(f, N)
    res = a[0] ** 2 / 2

    for n in range(1, N):
        res += a[n] ** 2 + b[n] ** 2

    return np.pi * res


#  parseval for G
def parseval_G(f, N):

    c = c_coef(f, N)

    for n in range(len(c)):
        