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
def _fourier_img_0(f, V):
    X = np.linspace(-10, 10, 1000)
    return np.array([1 / (np.sqrt(2 * np.pi)) * integral_counter(X, f, (lambda t:  np.e ** (-1j * image_clip * t)
    if -10 <= image_clip <= 10 else 0 * np.e ** (-1j * image_clip * t))(X))
                     for image_clip in V])


def _fourier_img_1(f, V):
    X = np.linspace(-10, 10, 1000)
    return np.array([1 / (np.sqrt(2 * np.pi)) * integral_counter(X, f, (lambda t: np.e ** (-1j * image_clip * t))(X))
                     for image_clip in V])


#  inverse Fourier transform
def _inverse_fourier(image, V):
    X = np.linspace(-10, 10, 1000)
    return np.array([1 / (np.sqrt(2 * np.pi)) * integral_counter(V, image, (lambda t: np.e ** (1j * x * t))(V)) for x in X])


#  draw inverse fourier transform
def _draw_inverse(f):
    V_1 = np.linspace(-25, 25, 1000)
    X = np.linspace(-10, 10, 1000)
    plt.plot(X, _inverse_fourier(_fourier_img_0(f, V_1), V_1).real, label=r'$Re \, f(t)$')
    # plt.plot(X, _inverse_fourier(_fourier_img(f, V_1), V_1).imag, label=r'$Im \, f(t)$')
    plt.grid()
    plt.legend()
    plt.xlabel(r'$t$')
    plt.ylabel(r'$f(t)$')
    plt.title('Обратное Фурье-преобразование сигнала u при b = d = 0.5, c = 0')
    plt.show()


#  draw inverse fourier transform and original function
def _draw_orig_and_ift(f):

    V_1 = np.linspace(-25, 25, 1000)
    X = np.linspace(-10, 10, 1000)
    plt.plot(X, _g_vec(1, 0, 2, X), label=r'$g(t)$ original')
    plt.plot(X, _inverse_fourier(_fourier_img_0(f, V_1), V_1).real, label=r'$u(t)$ after IFFT')
    # plt.plot(X, _inverse_fourier(_fourier_img(f, V_1), V_1).imag, label=r'$Im \, f(t)$')
    plt.grid()
    plt.legend()
    plt.xlabel(r'$t$')
    plt.ylabel(r'$f(t)$')
    plt.title(r'График $g(t)$ и $u(t)$ после фильтрации при b = 0.5 d = 1 c = 0.5')
    plt.show()


#  draw fourier image
def _draw_image_fourier(f):
    V_1 = np.linspace(-25, 25, 1000)

    plt.plot(V_1, _fourier_img_0(f, V_1).real, label=r'$Re \, \hat{f}(\nu)$')
    plt.plot(V_1, _fourier_img_0(f, V_1).imag, label=r'$Im \, \hat{f}(\nu)$')
    plt.grid()
    plt.legend()
    plt.xlabel(r'$\nu$')
    plt.ylabel(r'$\hat{f}(\nu)$')
    plt.title('Фурье-образ сигнала u при b = c = 0.5, d = 5')
    plt.show()


#  draw abs of fourier image of original and transform function
def _draw_abs_images_fourier(u, f):
    V_1 = np.linspace(-25, 25, 1000)

    plt.plot(V_1, abs(_fourier_img_1(u, V_1)), label=r'$ |u(t)|$')
    plt.plot(V_1, abs(_fourier_img_1(f, V_1)), label=r'$|g(t)|$')
    plt.grid()
    plt.legend()
    plt.xlabel(r'$\nu$')
    plt.ylabel(r'$\hat{f}(\nu)$')
    plt.title(r'Модули Фурье-образов $u(t)$ до фильтрации и '
              r'$g(t)$')
    plt.show()


#  run function
def _run():
    a = 1
    b = 1
    c = 1
    d = 1

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
    #_draw_inverse(_noise_fun(a, b, c, d, t_1, t_2, t))
    _draw_orig_and_ift(_noise_fun(a, b, c, d, t_1, t_2, t))
    #_draw_abs_images_fourier(_noise_fun(a, b, c, d, t_1, t_2, t), _g_vec(a, t_1, t_2, t))


_run()