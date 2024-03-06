from manim import *
import numpy as np

# Original Function
func_period_from, func_period_to = 0, 2
func_discontinuities = np.arange(0, 2, 1)


def func(x):
    if 0 <= x < 1:
        return 0
    if 1 <= x < 2:
        return 2 - x
    return 0


# Fourier series for the func above
def series(x, num_terms):
    sum_terms = 0.25

    # reverse order
    # adding up from small numbers
    for n in range(num_terms, 0, -1):
        first_part = 4 * (np.cos(0.5 * np.pi * n) - (-1) ** n) / (np.pi * n) ** 2
        second_part = 2 * np.sin(np.pi * n * 0.5) / (np.pi * n)
        sum_part = first_part - second_part
        mult_part = sum_part * np.cos(0.5 * np.pi * n * x)
        sum_terms += mult_part

    return sum_terms


# Tex
# Web Tool : Handwriting math expression to Tex
#   https://webdemo.myscript.com/views/math/index.html#
tex_func = r"""
f\left( x\right) =\begin{cases}0, & x \in [0, 1) \\ 2-x, & x \in [1,2] \end{cases}
"""
tex_sim_or_equals = r"\sim"
tex_series = r"""
\frac{1}{4} \sum_{n=1}^{\infty}
    \left( \frac{4 (\cos \frac{\pi n}{2} - (-1)^n)}{(\pi n)^2} - \frac{2 \sin \frac{\pi n}{2}}{\pi n} \right) \cos \frac{\pi n x}{2}
"""

# Number of terms
series_start, series_end, series_step = 1, 19, 1
series_run_time = 15

series_more_start, series_more_end, series_more_step = 20, 200, 10
series_more_run_time = 10

# Axes
x_min, x_max, x_step = -0.1, 2.5, 1
y_min, y_max, y_step = -0.1, 1.1, 1
y_length = 3
include_ticks = True
include_tip = True
is_pi_label = True
show_x_0_label = True

# Function plot
func_x_range_min, func_x_range_max = 0, 2
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