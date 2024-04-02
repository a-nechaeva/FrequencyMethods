import numpy as np
import matplotlib.pyplot as plt
from a_b_c_counter import *

#  complex function
def fun_complex(t):
    _r = 1
    T = 8
    _re = 0
    _im = 0

    if -1 <= t < 1:
        _re = _r
        _im = t

    elif 1 <= t % T < 3:
        _re = 2 - t
        _im = 1

    elif 3 <= t % T < 5:
        _re = -1
        _im = 4 - t

    elif 5 <= t % T < 7:
        _re = -6 + t
        _im = -1
    elif t == 7:
        _re = _r
        _im = -1

    return _re + 1j * _im

fc_vec = np.vectorize(fun_complex)

#  draw graphic of complex fun
def _graphic_complex():
    t = np.linspace(-1, 7, 1000)
    plt.plot(fc_vec(t).real, fc_vec(t).imag, label='Исходная функция')
    plt.grid()
    plt.title('График исходной функции.')
    plt.xlabel('Re (f)')
    plt.ylabel('Im (f)')
    plt.legend()
    plt.show()


# count coefficient c_n for complex fun
def c_complex(f, N):
    res = []
    for n in range(-N, N + 1):
        fourier_exp = lambda t: np.exp(-1j * n * t * np.pi / 4)
        res.append(integral_counter(f, fourier_exp, -1, 7) / (8))
    return res


def mm():
    c = c_complex(fc_vec, 3)
    for n in range(len(c)):
        print(round(c[n].real, 5), '        ', round(c[n].imag, 2))


mm()
#_graphic_complex()

