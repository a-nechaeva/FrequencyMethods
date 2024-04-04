from task_1 import *
from numpy.fft import *
import librosa
import soundfile as sf

y, sr = librosa.load('MUHA.wav')


#  draw graphic of original sound
def _draw_g():

    t = np.linspace(0, len(y) / sr, len(y))

    plt.plot(t, y, label='original sound')
    plt.legend()
    plt.grid()
    plt.title('График исходных данных MUHA.wav')
    plt.show()


#  draw fourier image for MUHA
def _draw_image_fourier_muha():

    plt.plot(fftfreq(len(y), 1 / sr), abs(fft(y)), label=r'$Re \, \hat{f}(\nu)$')
    #plt.plot(fftfreq(len(y), 1 / sr), fft(y).imag, label=r'$Im \, \hat{f}(\nu)$')
    plt.grid()
    plt.legend()
    plt.xlabel(r'$\nu$')
    plt.ylabel(r'$\hat{f}(\nu)$')
    plt.title('Модуль Фурье-образа исходной аудиодорожки')
    plt.show()


clip_delta_image_values = lambda nu: lambda X, func: np.array([0 if (-nu <= X[i] <= nu
                                                                     or 7000 < X[i] or X[i] < -7000)
                                                               else func[i] for i in range(len(func))])

#  draw final image
def _draw_image_f_muha_final():
    clipped_image = clip_delta_image_values(400)(fftfreq(len(y), 1 / sr), fft(y))
    plt.plot(fftfreq(len(y), 1 / sr), abs(clipped_image), label=r'$Re \, \hat{f}(\nu)$')
    plt.grid()
    plt.legend()
    plt.xlabel(r'$\nu$')
    plt.ylabel(r'$\hat{f}(\nu)$')
    plt.title('Модуль Фурье-образа финальной аудиодорожки')
    plt.show()

    t = np.linspace(0, len(y) / sr, len(y))
    restored = ifft(clipped_image).real
    plt.plot(t, restored, label=r'final sound')
    plt.grid()
    plt.legend()
    plt.title('График финальных данных')
    plt.show()
    sf.write('NEW_MUHA.wav', restored, sr, subtype='PCM_24')

#_draw_g()
_draw_image_fourier_muha()
_draw_image_f_muha_final()

