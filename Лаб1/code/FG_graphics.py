from a_b_c_counter import *
import numpy as np
import matplotlib.pyplot as plt

def graphics_F(t, N, f):

    a_n = a_coef(f, N)
    b_n = b_coef(f, N)
    res = a_n[0] / 2

    for n in range(1, N + 1):
        res += a_n[n] * np.cos(n * t) + b_n[n] * np.sin(n * t)

    return res


def graphics_G(t, N, f):
    c_n = c_coef(f, N)
    res = 0 + 0j

    for n in range(-N, N + 1):
        res += c_n[n + N] * np.exp(1j * n * t)

    return res

def draw_1():
    N = 50
    t = np.linspace(-7, 7, 1000)
    plt.plot(t, fun_not_odd_not_even(t), label='Исходная функция')
    plt.plot(t, graphics_F(t, N, fun_not_odd_not_even), label='График F(t)')
    plt.title('Ни четная, ни нечетная функция, N = 50, приближение F(t).')
    plt.grid()
    plt.legend()
    plt.show()


def draw_2():
    N = 50
    t = np.linspace(-7, 7, 1000)
    plt.plot(t, fun_not_odd_not_even(t), label='Исходная функция')
    plt.plot(t, graphics_G(t, N, fun_not_odd_not_even), label='График G(t)')
    plt.grid()
    plt.title('Ни четная, ни нечетная функция, N = 50, приближение G(t).')
    plt.legend()
    plt.show()

#draw_1()
draw_2()


