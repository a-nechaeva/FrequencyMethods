import scipy.integrate as integrate
import numpy as np


my_sigma = 1000  # мелкость разбиения
def fun_square_wave(t):
    if (t // np.pi) % 2 == 0:
        return 2
    else:
        return 1


fun_even = lambda t: 4 * np.cos(np.sin(t / 2) ** 2)

fun_odd = lambda t: np.sin(t) ** 3



#def fun_not_odd_not_even(t):


# here we count integral of two fun mult
def integral_counter(f_1, f_2, a, b):

    t = np.linspace(a, b, my_sigma)
    dt = (a - b) / my_sigma

    return np.dot(f_1(t), f_2(t)) * dt


def a_coef(fun, N):
    a = []
    for n in range(N):
        fourier_cos = lambda t: np.cos(n * t)
        a.append(integral_counter(fun, fourier_cos, -np.pi, np.pi) / np.pi)

    return a


def main():
    print(a_coef(fun_even, 3))


main()


