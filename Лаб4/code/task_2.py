import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import tf2zpk, lsim, freqs_zpk

from task_1 import *
from task_1 import _draw_fun, _fourier_img_0

b = 0.5
c = 0
d = 1



#  original function g(t)
def _g(t):

    if 0 <= t <= 2:
        return 2
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

    _t1 = np.linspace(0, 10, 1000)
    _t_ = np.linspace(0, 10, 1000)
    noised_g = _noise_fun(_t_)

    v = np.linspace(-25, 25, 1000)

    t_f, g_f, remainder_ = lsim(_fil(_t), noised_g, _t_)
    img_1 = _fourier_img_0(_g_vec(_t1), v, _t1)
    img_2 = _fourier_img_0(g_f, v, _t_)

    z, p, k = _fil(_t)
    w, h = freqs_zpk(z, p, k, worN=np.linspace(-25, 25, 1000))

    plt.plot(w, h.real, label='АЧХ фильтра', color='midnightblue')

    #plt.plot(v, abs(img_1), label=r'исходный', color='b')
    #plt.plot(v, abs(img_2), label=r'фильтрованный', color='r')
    #plt.plot(v, img_1.real, label=r'зашумленный', color='skyblue')
    #t_f, g_f, remainder_ = lsim(_fil(_t), noised_g, t)

    #plt.plot(t, _f(t), label=r'зашумленный', color='skyblue')
    #plt.plot(t_f, g_f, label=r'отфильтрованный', color='r')
    #plt.plot(t, _g_vec(t), label=r'исходный', color='indigo')
    #plt.ylabel(r'$\hat{f}(\omega)$')
    plt.ylabel(r'$|A|$')
    plt.xlabel(r'$\omega$')
    plt.grid()
    plt.legend()
    plt.title(r'АЧХ фильтра при $T=$' + str(_t))
    #plt.title(r'Фурье-образы исходного и фильтрованного сигналов $T=$' + str(_t))
    #plt.title(r'Сигнал исходный, зашумленный и после фильтрации при $T=$' + str(_t))
    plt.show()




# _draw_u(_noise_fun)
_filter_(f_filter, 1, _noise_fun)

