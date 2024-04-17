import numpy as np
from scipy.signal import tf2zpk, lsim, freqs_zpk

from task_1 import *
from task_1 import _draw_fun

b = 0.5
c = 0
d = 1



#  original function g(t)
def _g(t):

    if 0 <= t <= 2:
        return 1
    else:
        return 0


_g_vec = np.vectorize(_g)

#  noise function
_noise_fun = lambda t:  _g_vec(t) + b * (np.random.rand(1000) - 0.5) + c * np.sin(d * t)


def _draw_u(_f):

    t = np.linspace(-10, 10, 1000)
    plt.plot(t, _f(t), label=r'$g(t)$', color='midnightblue')
    plt.ylabel(r'$g(t)$')
    plt.xlabel(r'$t$')
    plt.grid()
    plt.legend()
    plt.title(r'График $u(t)$ при $b=$' + str(b) + ', $c=$' + str(c) + ', $d=$' + str(d))
    plt.show()


f_filter = lambda _t: tf2zpk([0, 1], [_t, 1])


def _filter_(_fil, _t, _f):

    t = np.linspace(0, 10, 1000)
    noised_g = _noise_fun(t)

    t_f, g_f, remainder_ = lsim(_fil(_t), noised_g, t)

    plt.plot(t, _f(t), label=r'$u(t)$', color='c')
    plt.plot(t_f, g_f, label=r'g(t)', color='r')
    plt.ylabel(r'g(t)')
    plt.xlabel(r't')
    plt.grid()
    plt.legend()
    plt.title(r'Сигнал исходный и после фильтрации при $T=$' + str(_t))
    plt.show()

# _draw_u(_noise_fun)
_filter_(f_filter, 0.1, _noise_fun)
