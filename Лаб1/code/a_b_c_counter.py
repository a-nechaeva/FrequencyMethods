import scipy.integrate as integrate
import numpy as np


my_sigma = 10000  # мелкость разбиения


def fun_square_wave(t):
    if (t // np.pi) % 2 == 0:
        return 2
    else:
        return 1

fun_wave = np.vectorize(fun_square_wave)

fun_even = lambda t: 4 * np.cos(np.sin(t / 2) ** 2)

fun_odd = lambda t: np.sin(t) ** 3


#def fun_not_odd_not_even(t):

# here we count integral of two fun mult
def integral_counter(f_1, f_2, a, b):

    t = np.linspace(a, b, my_sigma)
    dt = (b - a) / my_sigma

    return np.dot(f_1(t), f_2(t)) * dt


def a_coef(f, N):
    res = []
    for n in range(N):
        fourier_cos = lambda t: np.cos(n * t)
        res.append(integral_counter(f, fourier_cos, -np.pi, np.pi) / np.pi)

    return res


def b_coef(f, N):
    res = []
    for n in range(N):
        fourier_sin = lambda t: np.sin(n * t)
        res.append(integral_counter(f, fourier_sin, -np.pi, np.pi) / np.pi)
    return res


def c_coef(f, N):
    res = []
    for n in range(-N, N):
        fourier_exp = lambda t: np.exp(-1j * n * t)
        res.append(integral_counter(f, fourier_exp, -np.pi, np.pi) / (2 * np.pi))
    return res


def main():
    N = 3
    a = a_coef(fun_wave, N)
    b = b_coef(fun_wave, N)
    c = c_coef(fun_wave, N)

    for n in range(N):
        print("a_", n, " = ", a[n], "    ", "b_", n, " = ", b[n],  "\n")

    print(c_coef(fun_wave, 3))


main()


