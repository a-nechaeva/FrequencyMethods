from a_b_c_counter import *
import numpy as np
import matplotlib.pyplot as plt

def graphics_F(t, N, f):

    a_n = a_coef(f, N)
    b_n = b_coef(f, N)
    res = a_n[0] / 2

    for n in range(1, N):
        res += a_n[n] * np.cos(n * t) + b_n[n] * np.sin(n * t)

    return res


def graphics_G(t, N, f):
    c_n = c_coef(f, N)
    res = 0

    for n in range(-N, N + 1):
        res += c_n[n + N] * np.exp(1j * n * t)

    return res

def draw_():
    N = 2
    t = np.linspace(-7, 7, 1000)
    plt.plot(t, fun_wave(t))
    plt.plot(t, graphics_F(t, N, fun_wave))
    plt.grid()
    plt.show()

draw_()


