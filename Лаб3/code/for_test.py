from task_1 import *
import numpy as np


#  original function f(t)
def _ff(t):

    if t <= 0:
        return np.exp(t)
    else:
        return 0


_f_vec = np.vectorize(_ff)


gg = lambda t: np.cos(t)


