# pylint: disable=wrong-import-order
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=consider-using-enumerate
# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name
# pylint: disable=consider-using-f-string
# pylint: disable=trailing-whitespace
# pylint: disable=no-member
# pylint: disable=missing-function-docstring


from math import e
# import numpy as np
# import matplotlib.pyplot as plt
# import pickle as pkl
from support1 import distribution_count, plot_function#, save_to_pkl


def f(x):
    #N = 1000
    return e**(-1*x)

def func(dx):
    plot = plot_function(f, (0, 5000), (-0.1, 1.1), x_number=10**6)

    # dx = 1000

    x, y = distribution_count(f, (0, 5000), dx)

    plot.bar(x, y, color='red', width=dx)

    text = f"Plot for f(x)=e**(-1*x/1000) for segment length {dx}."
    # plot.text(1500, -0.40, text, ha='center')
    plot.title(text)

    plot.savefig(f'plot-{dx}.png',dpi=500)
    plot.clf()

# plot.show()

dx = 1000

while dx >= 10:
    func(dx)
    dx = dx / 10
