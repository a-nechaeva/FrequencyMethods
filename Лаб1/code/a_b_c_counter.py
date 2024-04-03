import scipy.integrate as integrate
import numpy as np


my_sigma = 100000  # мелкость разбиения


def fun_square_wave(t):
    if (t // np.pi) % 2 == 0:
        return 2
    else:
        return 1

fun_wave = np.vectorize(fun_square_wave)

fun_even = lambda t: 4 * np.cos(np.sin(t / 2) ** 2)

fun_odd = lambda t: np.sin(t) ** 3

fun_not_odd_not_even = lambda t: np.sin(t) - (np.cos(t)) ** 2

# here we count integral of two fun mult
def integral_counter(f_1, f_2, a, b):

    t = np.linspace(a, b, my_sigma)
    dt = (b - a) / my_sigma

    return np.dot(f_1(t), f_2(t)) * dt


def a_coef(f, N):
    res = []
    for n in range(N + 1):
        fourier_cos = lambda t: np.cos(n * t)
        res.append(integral_counter(f, fourier_cos, np.pi, 3 * np.pi) / np.pi)

    return res


def b_coef(f, N):
    res = []
    for n in range(N + 1):
        fourier_sin = lambda t: np.sin(n * t)
        res.append(integral_counter(f, fourier_sin, np.pi, 3 * np.pi) / np.pi)
    return res


def c_coef(f, N):
    res = []
    for n in range(-N, N + 1):
        fourier_exp = lambda t: np.exp(-1j * n * t)
        res.append(integral_counter(f, fourier_exp, np.pi, 3 * np.pi) / (2 * np.pi))
    return res


f_1_test = lambda t: t / 2.5
f_2_test = lambda t: 2 - t / 2.5


def for_test(f_1, f_2, N):
    res = []
    for n in range(1, 2):
        new_exp = lambda t: np.exp(-2j * np.pi * t)
        res.append(integral_counter(f_1, new_exp, 0, 2.5))
        res.append(integral_counter(f_2, new_exp, 2.5, 5))
    return res


def m():
    N = 4
    a = a_coef(fun_not_odd_not_even, N)
    b = b_coef(fun_not_odd_not_even, N)
    #  c = c_coef(fun_even, N)

    for n in range(N):
        print("a_", n, " = ", a[n], "    ", "b_", n, " = ", b[n],  "\n")

    print(c_coef(fun_not_odd_not_even, 3))


#m()
    #f_test_1 = for_test(f_1_test, f_2_test, 1)

    #print(f_test_1[0] + f_test_1[1])




