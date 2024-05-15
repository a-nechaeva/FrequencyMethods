import numpy as np


a_1 = 1
a_2 = 2
w_1 = 3
w_2 = 4
fi_1 = np.pi
fi_2 = 2 * np.pi
d = 100


_f = lambda t: a_1 * np.sin(w_1 * t + fi_1) + a_2 * np.sin(w_2 * t + fi_2)

t = np.linspace(-d, d, 1000)

