import numpy as np
import matplotlib.pyplot as plt


a = 1
b = 5

#  functions
_rectangle_f = lambda t: a if b >= abs(t) else 0

_v_rect = np.vectorize(_rectangle_f)
get_wave_func = lambda: np.vectorize(lambda t: _rectangle_f(t), otypes=[complex])


_triangle_f = lambda t: a - abs(a * t / b) if b >= abs(t) else 0

_v_triag = np.vectorize(_triangle_f)

_sinc_f = lambda t: a * np.sinc(b * t)

_gauss_f = lambda t: a * np.exp(-b * t ** 2)

_attenuation_f = lambda t: a * np.exp(-b * abs(t))


#  draw plots of functions
def _draw_fun(f):

    t = np.linspace(-10, 10, 1000)

    plt.plot(t, f(t), label=r'f(t)')
    plt.ylabel(r'f(t)')
    plt.xlabel(r't')
    plt.legend()
    plt.grid()
    plt.title('Прямоугольная функция a = ' + str(a) + ', b = ' + str(b))
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

    wave = get_wave_func()(X)

    V_1 = np.linspace(-25, 25, 1000)

    plt.plot(V_1, _fourier_img_0(wave, V_1).real, label=r'$Re \, \hat{f}(\omega)$')
    #  plt.plot(V_1, _fourier_img_0(wave, V_1).imag, label=r'$Im \, \hat{f}(\omega)$')
    plt.grid()
    plt.legend()
    plt.xlabel(r'$\omega$')
    plt.ylabel(r'$\hat{f}(\omega)$')
    plt.title('Фурье-образ прямоугольной функции a = ' + str(a) + ', b = ' + str(b))
    plt.show()


#  _draw_fun(_v_rect)
_draw_image_fourier(get_wave_func)


