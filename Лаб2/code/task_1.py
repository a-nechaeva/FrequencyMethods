import numpy as np
import matplotlib.pyplot as plt
import librosa
import soundfile as sf


a = 1
b = 1
c = 5


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

_attenuation_f = lambda t: a * np.exp(-b * abs(t + c))

get_atten = lambda: np.vectorize(lambda t: _attenuation_f(t), otypes=[complex])


#  draw plots of functions
def _draw_fun(f):

    t = np.linspace(-10, 10, 1000)

    plt.plot(t, f(t), label=r'g(t)', color='b')
    #  t_1 = np.linspace(-10, -b, 100)
    #  t_2 = np.linspace(b, 10, 100)
    #  plt.plot(t_1, f(t_1), color='b')
    #  plt.plot(t_2, f(t_2), color='b')
    plt.ylabel(r'g(t)')
    plt.xlabel(r't')
    plt.legend()
    plt.grid()
    plt.title('Двустороннее затухание c = ' + str(c))
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

    plt.plot(V_1, _fourier_img_0(wave, V_1).real, label=r'$Re \, \hat{g}(\omega)$', color='b')
    plt.plot(V_1, _fourier_img_0(wave, V_1).imag, label=r'$Im \, \hat{g}(\omega)$', color='r')
    plt.grid()
    plt.legend()
    plt.xlabel(r'$\omega$')
    plt.ylabel(r'$\hat{g}(\omega)$')
    plt.title('Фурье-образ двустороннего затухания c = ' + str(c))
    plt.show()


# here we count integral of two fun mult
def _par_integral_counter(f_1, f_2, st, fn):

    t = np.linspace(st, fn, 1000)
    dt = (fn - st) / 1000

    return np.dot(f_1(t), f_2(t)) * dt


def fourier_image(func, st, fn):
    image = lambda v: 1 / (np.sqrt(2 * np.pi)) * _par_integral_counter(func, lambda t: np.e ** (-1j * v * t), st, fn)
    return np.array(image)


def parseval_check(f):
    f_image = fourier_image(f, -25, 25)

    f_image_abs = np.vectorize(lambda t: abs(f_image(t)))

    left = _par_integral_counter(f, f, -100, 100)

    right = _par_integral_counter(f_image_abs, f_image_abs, -100, 100)
    print(left, right)


#  draw fourier image absolute value
def _draw_image_fourier_abs(f):
    X = np.linspace(-10, 10, 1000)

    wave = f()(X)

    V_1 = np.linspace(-25, 25, 1000)

    plt.plot(V_1, np.sqrt(_fourier_img_0(wave, V_1).real ** 2 + _fourier_img_0(wave, V_1).imag ** 2), label=r'$ | \hat{g}(\omega) |$', color='b')
    #plt.plot(V_1, _fourier_img_0(wave, V_1).imag, label=r'$Im \, \hat{g}(\omega)$', color='r')
    plt.grid()
    plt.legend()
    plt.xlabel(r'$\omega$')
    plt.ylabel(r'$\hat{g}(\omega)$')
    plt.title('Модуль Фурье-образа двустороннего затухания c = ' + str(c))
    plt.show()


#  parseval_check(_attenuation_f)
#  _draw_fun(_attenuation_f)
#  _draw_image_fourier(get_atten)
#  _draw_image_fourier_abs(get_atten)


# music task 3

wave_from_sample, sr = librosa.load('m29.mp3')

wave_from_time = np.vectorize(lambda t: wave_from_sample[int(t * sr)])
time = len(wave_from_sample) / sr - 0.001


def _draw_mp3(f, _time):
    t = np.linspace(0, _time - 0.1, 100000)
    plt.plot(t, f(t), label=r'f(t)', color='purple')
    plt.ylabel(r'f(t)')
    plt.xlabel(r't')
    plt.grid()
    plt.legend()
    plt.title(r'График f(t)')
    plt.show()


#_draw_mp3(wave_from_time, time)

_v = 1000
_v_arr = np.linspace(-_v, _v, 1000)


def _draw_mp3_image(f, _time):
    t = np.linspace(0, _time, 10000)
    wave = f(t)
    V_1 = np.linspace(0, 1000, 10000)
    Y_1 = []
    Y_2 = []

    max_1 = 0
    max_2 = 0
    max_3 = 0

    fr1 = 0
    fr2 = 0
    fr3 = 0

    for v_1 in V_1:
        k = abs(np.trapz(wave * np.exp(-1j * 2 * np.pi * v_1 * t), t))
        Y_1.append(k)
        if k > max_1:
            max_1 = k
            fr1 = v_1
        if k > max_2 and (max_1 != k) and (v_1 < 170):
            max_2 = k
            fr2 = v_1

        if k > max_3 and (max_2 != k) and (max_1 != k) and (v_1 > 200):
            max_3 = k
            fr3 = v_1
        #Y_1.append(np.trapz(wave * np.exp(-1j * 2 * np.pi * v_1 * t), t).real)
        #Y_2.append(np.trapz(wave * np.exp(-1j * 2 * np.pi * v_1 * t), t).imag)
    print('max_1 = ' + str(max_1) + ' nu = ' + str(fr1))
    print('max_2 = ' + str(max_2) + ' nu = ' + str(fr2))
    print('max_3 = ' + str(max_3) + ' nu = ' + str(fr3))

    #plt.plot(V_1, Y_1, label=r'$Re \, \hat{g}(\nu)$', color='b')
    plt.plot(V_1, Y_1, label=r'$| \hat{g}(\nu)|$', color='purple')
    #plt.plot(V_1, Y_2, label=r'$Im \, \hat{g}(\nu)$', color='r')
    plt.ylabel(r'$\hat{g}(\nu)$')
    plt.xlabel(r'$\nu$')
    plt.legend()
    plt.grid()
    plt.title('Модуль Фурье-образа первой четверти аудиодорожки')
    #plt.plot(V_1, Y.imag)

    plt.show()



_draw_mp3_image(wave_from_time, time / 4)
# print(time)
# # fourier transform
#wave_image = wave_fourier_image(wave_from_time, 0, 0.1)
#wave_image_abs = lambda t: abs(wave_image(t))
# plot_wave_image(wave_image_abs, 0, 4000, caption='Fourier image of Chord23', title='media/wave_image')



