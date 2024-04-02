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
    res = 0

    for n in range(len(c)):
        res += abs(c[n]) ** 2

    return 2 * np.pi * res


#  ||f||^2
_f2 = lambda f: integral_counter(f, f, -np.pi, np.pi)


def parseval_check():
    N = 10
    print('Parseval for F: ', parseval_F(fun_not_odd_not_even, N), '\n')
    print('Parseval for G: ', parseval_G(fun_not_odd_not_even, N), '\n')
    print('||f||^2: ', _f2(fun_not_odd_not_even), '\n')


parseval_check()
