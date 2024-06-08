import matplotlib.pyplot as plt
import numpy as np


a_1 = 1
a_2 = 2
w_1 = 3
w_2 = 4
fi_1 = np.pi
fi_2 = 2 * np.pi
d = 20
st = 1000


_f = lambda t: a_1 * np.sin(w_1 * t + fi_1) + a_2 * np.sin(w_2 * t + fi_2)

int_c = lambda x, f1, f2: np.trapz(f1 * f2, x=x, dx=x[1] - x[0])


_fourier_image = lambda f, x, v: np.array([int_c(x, f, (lambda t: np.e ** (-1j * i * t * 2 * np.pi))(x)) for i in v])



def _sin_gr():

    t = np.linspace(-d, d, st)
    t_1 = np.linspace(-d, d, st // 20)
    plt.plot(t, _f(t), label='исходная функция', color='lightblue')
    plt.plot(t_1, _f(t_1), ":", label='сэплирование', color='k')
    plt.xlabel(r'$t$')
    plt.ylabel(r'$y(t)$')
    plt.xlim([-5, 5])
    plt.grid()
    plt.legend()
    plt.title(r'Сэмплирование $\Delta t = 0.1$ c')
    plt.show()


def _interpol(b):
    tt = np.linspace(-d, d, st)
    t_s = np.arange(-d, d, 0.1)
    f_s = _f(t_s)
    t = np.linspace(-d, d, st)

    nu = np.linspace(-20, 20, 1000)
    im = _fourier_image(f_s, t_s, nu)

    f_interp = np.vectorize(lambda t: np.sum([_f(n) * np.sinc(2 * b * (t - n)) for n in t_s]))
    t_interp = np.linspace(-10, 10, 1000)
    restored_image = _fourier_image(f_interp(t_interp), t_interp, nu)
    plt.plot(t, _f(t), label='исходная функция', color='b')
    plt.plot(t_interp, f_interp(t_interp), ':', label='восстановленная', color='r')
    plt.xlabel(r'$t$')
    plt.ylabel(r'$y(t)$')
    plt.xlim([-10, 10])
    plt.grid()
    plt.legend()
    plt.title(r'Восстановление $B = 5$')
    plt.show()


_interpol(5)
#_sin_gr()