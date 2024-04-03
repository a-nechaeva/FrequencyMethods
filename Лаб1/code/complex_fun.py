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
    N = 10
    t = np.linspace(-1, 7, 1000)
    plt.plot(fc_vec(t).real, fc_vec(t).imag, label='Исходная функция')
    plt.plot(graphics_G(t, N, fc_vec).real, graphics_G(t, N, fc_vec).imag, label='График G(t)')
    plt.grid()
    plt.title('Комплексная функция, N = 10, приближение G(t).')
    plt.xlabel('Re (f)')
    plt.ylabel('Im (f)')
    plt.legend()
    plt.show()


# count coefficient c_n for complex fun
def c_complex(f, N):
    res = []
    for n in range(-N, N + 1):
        fourier_exp = lambda t: np.exp(-1j * n * t * np.pi / 4)
        res.append(integral_counter(f, fourier_exp, -1, 7) / 8)
    return res


#  GN function for complex
def graphics_G(t, N, f):
    c_n = c_complex(f, N)
    res = 0 + 0j

    for n in range(-N, N + 1):
        res += c_n[n + N] * np.exp(1j * n * t * np.pi / 4)

    return res


#  draw Re f(t)
def _graph_re_f():
    N = 10
    t = np.linspace(-1, 7, 1000)
    plt.plot(t, fc_vec(t).real, label=r'$Re \, f(t)$')
    plt.plot(t, graphics_G(t, N, fc_vec).real, label=r'$Re \, G_N(t)$')
    plt.grid()
    plt.title('Графики вещественной части при N = 10.')
    plt.legend()
    plt.show()


#  draw Im f(t)
def _graph_im_f():
    N = 10
    t = np.linspace(-1, 7, 1000)
    plt.plot(t, fc_vec(t).imag, label=r'$Im \, f(t)$')
    plt.plot(t, graphics_G(t, N, fc_vec).imag, label=r'$Im \, G_N(t)$')
    plt.grid()
    plt.title('Графики мнимой части при N = 10.')
    plt.legend()
    plt.show()


def c_integral_counter(f_1, f_2, a, b):

    t = np.linspace(a, b, my_sigma)
    dt = (b + a) / my_sigma

    return np.dot(abs(f_1(t)), abs(f_2(t))) * dt


#  parseval check for complex function
def _c_parseval(f, N):
    c = c_complex(f, N)
    res = 0

    for n in range(len(c)):
        res += (abs(c[n])) ** 2

    f_norm = c_integral_counter(fc_vec, fc_vec, -1, 7)

    print(res * 2 * np.pi)
    print(f_norm)

def mm():
    c = c_complex(fc_vec, 3)
    for n in range(len(c)):
        print(round(c[n].real, 5), '        ', round(c[n].imag, 2))


#mm()
#_graphic_complex()
#_graph_re_f()

_c_parseval(fc_vec, 100)
