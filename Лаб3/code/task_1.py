import numpy as np
import matplotlib.pyplot as plt


#  original function g(t)
def _g(a, t_1, t_2, t):

    if t_1 <= t <= t_2:
        return a
    else:
        return 0


_g_vec = np.vectorize(_g)
#  draw graphic of original function
def _draw_g():
    a = 1
    t_1 = 0
    t_2 = 2
    T = 20
    t = np.linspace(- T / 2, T / 2, 1000)

    plt.plot(t, _g_vec(a, t_1, t_2, t), label='g(t)')
    plt.legend()
    plt.grid()
    plt.title('График исходной функции g(t)')
    plt.show()


#  run function
def _run():
    _draw_g()


_run()