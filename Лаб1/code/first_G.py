from manim import *
import numpy as np

# Original Function
func_period_from, func_period_to = np.pi, 3 * np.pi
func_discontinuities = np.arange(0, 2, 1)


def func(x):
    if np.pi <= x < 2 * np.pi:
        return 1
    if 2 * np.pi <= x < 3 * np.pi:
        return 2
    return 0


# Fourier series for the func above
def series(x, num_terms):
    sum_terms = 3/2

    # reverse order
    # adding up from small numbers
    for n in range(num_terms, 0, -1):
        sum_part = ((-2 * np.exp(-3 * 1j * n * np.pi) + np.exp(-1j * n * np.pi) + np.exp(-2 * 1j * n * np.pi)) /
                    (1j * 2 * n * np.pi))
        '''sum_part = ((1j * np.e ** (1j * np.pi * n) + 1j * np.e ** (2j * np.pi * n) - 2j * np.e ** (3j * np.pi * n)) /
                    (2 * n * np.pi))'''
        mult_part = sum_part * np.exp(1j * n * x)
        sum_terms += mult_part

    for n in range(num_terms, 0, -1):
        sum_part = ((-2 * np.exp(-3 * 1j * (-n) * np.pi) + np.exp(-1j * (-n) * np.pi) + np.exp(-2 * 1j * (-n) * np.pi)) /
                    (1j * 2 * (-n) * np.pi))
        '''sum_part = ((1j * np.e ** (1j * np.pi * (-n)) + 1j * np.e ** (2j * np.pi * (-n)) - 2j * np.e ** (3j * np.pi * (-n))) /
                    (2 * (-n) * np.pi))'''
        mult_part = sum_part * np.exp(1j * (-n) * x)
        sum_terms += mult_part

    return sum_terms


# Tex
# Web Tool : Handwriting math expression to Tex
#   https://webdemo.myscript.com/views/math/index.html#
tex_func = r"""
f\left( x\right) =\begin{cases}1, & t \in [\pi, 2 \pi) \\ 2, & t \in [2 \pi ,3 \pi) \end{cases}
"""
tex_sim_or_equals = r"\sim"
tex_series = r"""
 \sum  \limits_{n=-N}^N   \frac{ e^{-i n \pi} + e^{-2i n \pi} - 2 e^{-3i n \pi}}{2 i n \pi} e^{i n t}
"""

# Number of terms
series_start, series_end, series_step = 1, 19, 1
series_run_time = 15

series_more_start, series_more_end, series_more_step = 20, 100, 10
series_more_run_time = 10

# Axes
x_min, x_max, x_step = -0.1, 10.0, 1
y_min, y_max, y_step = -0.1, 3.1, 1
y_length = 3
include_ticks = True
include_tip = True
is_pi_label = True
show_x_0_label = True

# Function plot
func_x_range_min, func_x_range_max = np.pi, 3 * np.pi
plot_x_delta = 5e-3

# Color
COLOR_MESSAGE = WHITE
COLOR_FUNC = "#98ff98"
COLOR_PERIODIC = YELLOW
COLOR_SERIES = "#ffc0cb"
COLOR_TILDE = WHITE
COLOR_N_TERM_COUNT = WHITE

# Message displayed before the formula
message = "Fourier Series for"