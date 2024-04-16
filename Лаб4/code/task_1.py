import numpy as np
import matplotlib.pyplot as plt


a = 1
_sin = lambda t: np.sin(t)

_cos = lambda t: np.cos(t)

_noise_sin = lambda t: np.sin(t) + a * (np.random.rand(1000) - 0.5)

_noise_dif = lambda t, dt: (np.sin(t + dt) + a * (np.random.rand(1000) - 0.5) -
                            (np.sin(t) + a * (np.random.rand(1000) - 0.5))) / dt


int_c = lambda x, f1, f2: np.dot(f1, f2) * (x[1] - x[0])


_fourier_image = lambda f, x, v: np.array([1 / (np.sqrt(2 * np.pi)) *
                                     int_c(x, f, (lambda t: np.e ** (-1j * i * t))(x)) for i in v])


_fourier_fun = lambda im, x, v: np.array([1 / (np.sqrt(2 * np.pi)) *
                                          int_c(v, im, (lambda t: np.e ** (1j * i * t))(v)) for i in x])


def integral_counter(X, f_1, f_2):

    dt = X[1] - X[0]

    return np.dot(f_1, f_2) * dt


def _fourier_img_0(f, V):
    X = np.linspace(-10, 10, 1000)
    return np.array([1 / (np.sqrt(2 * np.pi)) * integral_counter(X, f, (lambda t:  np.e ** (-1j * image_clip * t))(X)) * 1j * image_clip
                     for image_clip in V])


def _inverse_fourier(image, V):
    X = np.linspace(-10, 10, 1000)
    return np.array([1 / (np.sqrt(2 * np.pi)) * integral_counter(V, image, (lambda t: np.e ** (1j * x * t))(V)) for x in X])


def _noise_diff(t, dt):
    n = a * (np.random.rand(10000) - 0.5)
    return (np.sin(t + dt) + n - (np.sin(t) + n)) / dt

def _draw_fun(f):
    t = np.linspace(-10, 10, 1000)
    plt.plot(t, f(t), label=r'$f(t)$', color='midnightblue')
    plt.ylabel(r'$f(t)$')
    plt.xlabel(r'$t$')
    plt.grid()
    plt.legend()
    plt.title(r'График функции $f = cos(t)$')
    plt.show()


def _draw_noise(f):

    t = np.linspace(-10, 10, 1000)
    dt = t[1] - t[0]

    plt.plot(t, f(t, dt), label=r'$f(t)$', color='midnightblue')
    plt.ylabel(r'$f(t)$')
    plt.xlabel(r'$t$')
    plt.grid()
    plt.legend()
    plt.title(r'График зашумленного сигнала при $a = $' + str(a))
    plt.show()


def _draw_noise_diff(f):

    t = np.linspace(-10, 10, 1000)
    dt = t[1] - t[0]

    plt.plot(t, f(t, dt), label=r'$f\'(t)$', color='midnightblue')
    plt.ylabel(r'$f\'(t)$')
    plt.xlabel(r'$t$')
    plt.grid()
    plt.legend()
    plt.title(r'График  производной зашумленного сигнала при $a = $' + str(a))
    plt.show()


def _draw_spectrum_diff(f):
    t = np.linspace(-10, 10, 1000)
    v = np.linspace(-10, 10, 1000)

    img = _fourier_img_0(f, v)
    fun = _inverse_fourier(img, v)

    plt.plot(t, fun.real, label=r'$Re \, f\'(t)$', color='b')
    plt.plot(t, fun.imag, label=r'$Im \, f\'(t)$', color='r')
    plt.ylabel(r'$f\'(t)$')
    plt.xlabel(r'$t$')
    plt.grid()
    plt.legend()
    plt.title(r'График спектральной производной зашумленного сигнала при $a = $' + str(a))
    plt.show()


def _draw_image(f):
    t = np.linspace(-10, 10, 1000)
    v = np.linspace(-10, 10, 1000)

    img = _fourier_img_0(f, v)

    plt.plot(t, img.real, label=r'$Re \, \hat{f}(\omega)$', color='b')
    plt.plot(t, img.imag, label=r'$Im \, \hat{f}(\omega)$', color='r')
    plt.ylabel(r'$\hat{f}$')
    plt.xlabel(r'$\omega$')
    plt.grid()
    plt.legend()
    plt.title(r'График Фурье-образа зашумленного сигнала при $a = $' + str(a))
    plt.show()


_draw_fun(_cos)
#_draw_noise_diff(_noise_dif)
t_ = np.linspace(-10, 10, 1000)
#_draw_spectrum_diff(_noise_sin(t_))
#_draw_image(_noise_sin(t_))
