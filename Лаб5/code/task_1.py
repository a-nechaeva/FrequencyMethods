import numpy as np
import matplotlib.pyplot as plt
import datetime


_start = datetime.datetime.now()


n = 100
d = 5
#  start function
_f = lambda t: 1 if abs(t) <= 0.5 else 0

get_wave_func = lambda: np.vectorize(lambda t: 1 if abs(t) <= 0.5 else 0, otypes=[complex])

_f_image = lambda v: np.sinc(v)

_vf = np.vectorize(_f, otypes=[complex])

int_c = lambda x, f1, f2: np.trapz(f1 * f2, x=x, dx=x[1] - x[0])


_fourier_image = lambda f, x, v: np.array([int_c(x, f, (lambda t: np.e ** (-1j * i * t * 2 * np.pi))(x)) for i in v])


_fourier_fun = lambda im, x, v: np.array([int_c(v, im, (lambda t: np.e ** (1j * i * t * 2 * np.pi))(v)) for i in x])



def _draw_graph_im(f, t, title):
    new_t = np.linspace(-d, d, 5000)
    #plt.plot(t, f(t), label=r'$\hat{\Pi}(\nu)$', color='midnightblue')
    plt.plot(t, f, label=r'восстановленный', color='darkmagenta')
    plt.plot(new_t, _f_image(new_t), label=r'исходный', color='midnightblue')
    #plt.plot(t, f, label=r'$\Pi(t)$', color='midnightblue')
    plt.xlabel(r'$\nu$')
    #plt.xlabel(r'$t$')
    plt.ylabel(r'$\hat{\Pi}(\nu)$')
    #plt.ylabel(r'$\Pi(t)$')
    plt.grid()
    plt.legend()
    plt.title(title)
    plt.show()


def _draw_graph_f(f, t, title):
    new_t = np.linspace(-d, d, 5000)
    plt.plot(new_t,  _vf(new_t), label=r'$\Pi(t)$', color='midnightblue')
    plt.plot(t, f, label=r'восстановленная $\Pi(t)$', color='darkmagenta')
    plt.xlabel(r'$t$')
    plt.ylabel(r'$\Pi(t)$')
    plt.grid()
    plt.legend()
    plt.title(title)
    plt.show()


def _fft_im(t, title):

    new_t = np.linspace(-d, d, 5000)
    ff = _vf(t)
    im_ff = np.fft.fftshift(np.fft.fft(ff)) / np.sqrt(n)
    res_ff = num_restored = np.fft.ifft(np.fft.ifftshift(im_ff)) * np.sqrt(n)
    plt.plot(new_t, _vf(new_t), label=r'исходный', color='midnightblue')
    plt.plot(t, res_ff, label=r'ifft', color='darkmagenta')
    #plt.xlabel(r'$\nu$')
    #plt.ylabel(r'$\hat{\Pi}(\nu)$')
    plt.xlabel(r'$t$')
    plt.ylabel(r'$\Pi(t)$')
    plt.grid()
    plt.legend()
    plt.title(title)
    plt.show()


_steps = 1000


def _fft_im_correct(title):

    new_t = np.linspace(-d, d, _steps)
    ff = get_wave_func()
    f = ff(new_t)
    # im_ff = np.fft.fftshift(np.fft.fft(ff)) / np.sqrt(n)
    #  res_ff = num_restored = np.fft.ifft(np.fft.ifftshift(im_ff)) * np.sqrt(n)
    nu = np.fft.fftshift(np.fft.fftfreq(_steps, 10 / _steps))
    image_dft = np.fft.fftshift(np.fft.fft(f, norm='ortho'))

    dt = new_t[1] - new_t[0]

    dft_cont_image = image_dft * dt * np.exp(-1j * nu * 2 * np.pi * new_t[0]) * np.sqrt(_steps)
    #  plt.plot(nu, np.sinc(nu), label=r'истинный Фурье-образ', color='midnightblue')
    #  plt.plot(nu, dft_cont_image, '.', label=r'приближение', color='darkmagenta')

    dv = nu[1] - nu[0]
    f_restored_cont = np.fft.fftshift(np.fft.ifft(np.fft.ifftshift(dft_cont_image), norm='ortho') * np.sqrt(_steps) * dv)
    plt.plot(new_t, f, label='исходная функция', color='midnightblue')
    plt.plot(new_t, f_restored_cont, '.', label=r'приближение', color='darkmagenta')


    #  plt.xlabel(r'$\nu$')
    #  plt.ylabel(r'$\hat{\Pi}(\nu)$')
    plt.xlabel(r'$t$')
    plt.ylabel(r'$\Pi(t)$')
    plt.xlim([-5, 5])
    plt.grid()
    plt.legend()
    plt.title(title)
    plt.show()



time = np.linspace(-d, d, n)
_v = np.linspace(-d, d, n)

_fft_im_correct(r"Приближение непрерывного с помощью DFT")
#_fft_im(time, r'График восстановленной функции $ifft$ при $n=$' + str(n))
#  _draw_graph(_vf, time, 'График исходной функции')
#_draw_graph(_f_image, time, 'График Фурье-образа')
#_draw_graph_im(_fourier_image(_vf(time), time, time), time, r'График Фурье-образа при $n = $' + str(n))
# _draw_graph_f(_fourier_fun(_fourier_image(_vf(time), time, _v), time, _v), time, r'Графики функций при $n = $' + str(n))


_finish = datetime.datetime.now()

print('Processing time: ' + str(_finish - _start))
