import numpy as np
import matplotlib.pyplot as plt


#  start function
_f = lambda t: 1 if abs(t) <= 0.5 else 0

_f_image = lambda v: np.sinc(np.pi * v)

_vf = np.vectorize(_f)


def _draw_graph(f, t, title):

    #plt.plot(t, f(t), label=r'$\hat{\Pi}(\nu)$', color='midnightblue')
    plt.plot(t, f(t), label=r'$\Pi(t)$', color='midnightblue')
    plt.xlabel(r'$t$')
    #plt.ylabel(r'$\hat{\Pi}(\nu)$')
    plt.ylabel(r'$\Pi(t)$')
    plt.grid()
    plt.legend()
    plt.title(title)
    plt.show()


time = np.linspace(-5, 5, 1000)
_draw_graph(_vf, time, 'График исходной функции')
#_draw_graph(_f_image, time, 'График Фурье-образа')

