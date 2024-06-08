import matplotlib.pyplot as plt
import numpy as np


a_1 = 1
a_2 = 2
w_1 = 3
w_2 = 4
fi_1 = np.pi
fi_2 = 2 * np.pi
d = 10
st = 1000


_f = lambda t: a_1 * np.sin(w_1 * t + fi_1) + a_2 * np.sin(w_2 * t + fi_2)



def _sin_gr():

    t = np.linspace(-d, d, st)
    t_1 = np.linspace(-d, d, st // 20)
    plt.plot(t, _f(t), label='исходная функция', color='lightblue')
    plt.plot(t_1, _f(t_1), ":", label='сэплирование', color='k')
    plt.xlabel(r'$t$')
    plt.ylabel(r'$y(t)$')
    plt.xlim([-5, 5])
    plt.grid()
    plt.legend()
    plt.title(r'Сэмплирование $\Delta t = 0.1$ c')
    plt.show()


def _interpol():
    


_sin_gr()