import numpy as np
import matplotlib.pyplot as plt
import datetime


_start = datetime.datetime.now()


n = 1000
#  start function
_f = lambda t: 1 if abs(t) <= 0.5 else 0

_f_image = lambda v: np.sinc(v)

_vf = np.vectorize(_f)

int_c = lambda x, f1, f2: np.trapz(f1 * f2, x=x, dx=x[1] - x[0])


_fourier_image = lambda f, x, v: np.array([int_c(x, f, (lambda t: np.e ** (-1j * i * t * 2 * np.pi))(x)) for i in v])


_fourier_fun = lambda im, x, v: np.array([int_c(v, im, (lambda t: np.e ** (1j * i * t * 2 * np.pi))(v)) for i in x])



def _draw_graph_im(f, t, title):

    #plt.plot(t, f(t), label=r'$\hat{\Pi}(\nu)$', color='midnightblue')
    #plt.plot(t, f, label=r'$\hat{\Pi}(\nu)$', color='midnightblue')
    plt.plot(t, f, label=r'$\Pi(t)$', color='midnightblue')
    plt.xlabel(r'$t$')
    #plt.ylabel(r'$\hat{\Pi}(\nu)$')
    plt.ylabel(r'$\Pi(t)$')
    plt.grid()
    plt.legend()
    plt.title(title)
    plt.show()


def _draw_graph_f(f, t, title):

    plt.plot(t,  _vf(t), label=r'$\Pi(t)$', color='midnightblue')
    plt.plot(t, f, label=r'восстановленная $\Pi(t)$', color='darkmagenta')
    plt.xlabel(r'$t$')
    plt.ylabel(r'$\Pi(t)$')
    plt.grid()
    plt.legend()
    plt.title(title)
    plt.show()




time = np.linspace(-5, 5, n)
_v = np.linspace(-1, 1, 1000)

#  _draw_graph(_vf, time, 'График исходной функции')
#_draw_graph(_f_image, time, 'График Фурье-образа')
#_draw_graph(_fourier_image(_vf(time), time, time), time, 'График Фурье-образа')
_draw_graph_f(_fourier_fun(_fourier_image(_vf(time), time, _v), time, _v), time, r'Графики функций при $n = $' + str(n))


_finish = datetime.datetime.now()

print('Processing time: ' + str(_finish - _start))
