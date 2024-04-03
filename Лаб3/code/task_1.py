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
def _draw_g(a, t_1, t_2, T, _sigma):

    t = np.linspace(- T / 2, T / 2, _sigma)

    plt.plot(t, _g_vec(a, t_1, t_2, t), label='g(t)')
    plt.legend()
    plt.grid()
    plt.title('График исходной функции g(t)')
    plt.show()


#  noise function
_noise_fun = lambda a, b, c, d, t_1, t_2, t:  (_g_vec(a, t_1, t_2, t) + b * (np.random.rand(t.size) - 0.5)
                                               + c * np.sin(d * t))


#  draw graphic of noisy function
def _draw_noise(a, b, c, d, t_1, t_2, T, _sigma):

    t = np.linspace(- T / 2, T / 2, _sigma)

    plt.plot(t, _noise_fun(a, b, c, d, t_1, t_2, t), label='g(t) with noise')
    plt.legend()
    plt.grid()
    plt.title('Зашумленный график функции g(t) при b = 0.5, c = 0.5, d = 0.5')
    plt.show()



#  run function
def _run():
    a = 1
    b = 0.5
    c = 0.5
    d = 0.5

    t_1 = 0
    t_2 = 2
    T = 20
    _sigma = 1000

    #  _draw_g(a, t_1, t_2, T, _sigma)
    _draw_noise(a, b, c, d, t_1, t_2, T, _sigma)


_run()