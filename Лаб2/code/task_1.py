import numpy as np
import matplotlib.pyplot as plt


a = 1
b = 1

#  functions
_rectangle_f = lambda t: a if b >= abs(t) else 0

_v_rect = np.vectorize(_rectangle_f)
get_wave_func = lambda: np.vectorize(lambda t: _rectangle_f(t), otypes=[complex])


#  _triangle_f = lambda t: (a - abs((a * t) / b)) if b >= abs(t) else 0
def _triangle_f(t):
    if b >= abs(t):
        return a - abs(a * t / b)
    else:
        return 0

get_tria_func = lambda: np.vectorize(lambda t: _triangle_f(t), otypes=[complex])

_v_tria = np.vectorize(_triangle_f)


_sinc_f = lambda t: a * np.sinc(b * t)

get_sinc = lambda: np.vectorize(lambda t: _sinc_f(t), otypes=[complex])

_gauss_f = lambda t: a * np.exp(-b * t ** 2)

get_gauss = lambda: np.vectorize(lambda t: _gauss_f(t), otypes=[complex])

_attenuation_f = lambda t: a * np.exp(-b * abs(t))

get_atten = lambda: np.vectorize(lambda t: _attenuation_f(t), otypes=[complex])


#  draw plots of functions
def _draw_fun(f):

    t = np.linspace(-10, 10, 1000)

    plt.plot(t, f(t), label=r'f(t)', color='b')
    #  t_1 = np.linspace(-10, -b, 100)
    #  t_2 = np.linspace(b, 10, 100)
    #  plt.plot(t_1, f(t_1), color='b')
    #  plt.plot(t_2, f(t_2), color='b')
    plt.ylabel(r'f(t)')
    plt.xlabel(r't')
    plt.legend()
    plt.grid()
    plt.title('Двустороннее затухание a = ' + str(a) + ', b = ' + str(b))
    plt.show()


# here we count integral of two fun mult
def integral_counter(X, f_1, f_2):

    dt = X[1] - X[0]

    return np.dot(f_1, f_2) * dt


#  convert to fourier-image
def _fourier_img_0(f, V):
    X = np.linspace(-10, 10, 1000)
    return np.array([1 / (np.sqrt(2 * np.pi)) * integral_counter(X, f, (lambda t:  np.e ** (-1j * image_clip * t))(X))
                     for image_clip in V])


#  draw fourier image
def _draw_image_fourier(f):
    X = np.linspace(-10, 10, 1000)

    wave = f()(X)

    V_1 = np.linspace(-25, 25, 1000)

    plt.plot(V_1, _fourier_img_0(wave, V_1).real, label=r'$Re \, \hat{f}(\omega)$', color='b')
    #  plt.plot(V_1, _fourier_img_0(wave, V_1).imag, label=r'$Im \, \hat{f}(\omega)$')
    plt.grid()
    plt.legend()
    plt.xlabel(r'$\omega$')
    plt.ylabel(r'$\hat{f}(\omega)$')
    plt.title('Фурье-образ двустороннего затухания a = ' + str(a) + ', b = ' + str(b))
    plt.show()


# here we count integral of two fun mult
def _par_integral_counter(f_1, f_2, st, fn):

    t = np.linspace(st, fn, 1000)
    dt = (fn - st) / 1000

    return np.dot(f_1(t), f_2(t)) * dt


def fourier_image(func, st, fn):
    image = lambda v: 1 / (np.sqrt(2 * np.pi)) * _par_integral_counter(func, lambda t: np.e ** (-1j * v * t), st, fn)
    return np.vectorize(image)


def parseval_check(f):
    f_image = fourier_image(f, -25, 25)

    f_image_abs = np.vectorize(lambda t: abs(f_image(t)))

    left = _par_integral_counter(f, f, -100, 100)

    right = _par_integral_counter(f_image_abs, f_image_abs, -100, 100)
    print(left, right)


parseval_check(_v_rect)
#  _draw_fun(_attenuation_f)
#  _draw_image_fourier(get_atten)


