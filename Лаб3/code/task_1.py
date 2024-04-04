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
    plt.title('Зашумленный график функции g(t) при b = 0.5, c = 0, d = 0.5')
    plt.show()


# here we count integral of two fun mult
def integral_counter(X, f_1, f_2):

    dt = X[1] - X[0]

    return np.dot(f_1, f_2) * dt


#get_wave_func = lambda a, t1, t2: np.vectorize(lambda t: _g(a, t1, t2, t), otypes=[complex])


#  convert to fourier-image
def _fourier_img(f, V):
    X = np.linspace(-10, 10, 1000)
    return np.array([1 / (np.sqrt(2 * np.pi)) * integral_counter(X, f, (lambda t: np.e ** (-1j * image_clip * t))(X)) for image_clip in V])


#  draw fourier image
def _draw_image_fourier(f):
    V = np.linspace(-10, 10, 1000)
    plt.plot(V, _fourier_img(f, V).real, label=r'$Re \, u$')
    plt.plot(V, _fourier_img(f, V).imag, label=r'$Im \, u$')
    plt.grid()
    plt.legend()
    plt.title('Фурье-образ сигнала u при b = d = 0.5, c = 0')
    plt.show()


#  run function
def _run():
    a = 1
    b = 0.5
    c = 0
    d = 0.5

    t_1 = 0
    t_2 = 2
    T = 20
    _sigma = 1000
    X = np.linspace(-10, 10, 1000)

    #  _draw_g(a, t_1, t_2, T, _sigma)
    #_draw_noise(a, b, c, d, t_1, t_2, T, _sigma)
    #wave = get_wave_func(a, t_1, t_2)(X)
    t = np.linspace(-10, 10, 1000)
    _draw_image_fourier(_noise_fun(a, b, c, d, t_1, t_2, t))


_run()