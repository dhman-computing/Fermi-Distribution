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
from support1 import distribution_count, \
    mc_integration, new_integration#, plot_function#, save_to_pkl
# import random
import cProfile


def F(x):
    # N = 1000
    return e**(-1*x)

def f(x):
    return 5*x**2+6*x


# plot = plot_function(f, (0, 10), (-0.1, 1.1), x_number=10**6)

def main():
    dx = 0.1
    xlimit = (0,1000)

    x, y, delta_x = distribution_count(F, xlimit, dx)

    # plot.bar(x, y, color='red', width=dx)

    # text = f"Plot for f(x)=e**(-1*x) for segment length {dx}."
    # plot.text(1500, -0.40, text, ha='center')
    # plot.title(text)

    # plot.savefig(f'plot-{dx}.png',dpi=1500)

    total_random_no = 10**7
    integration = new_integration(f, y, delta_x, total_random_no)
    # print(total_random_no_genareted)
    print(integration)
    print((16 - integration)*100)

    def g(x):
        return f(x)*F(x)
    monte_carlo = mc_integration(g, xlimit[1], xlimit[0], total_random_no)
    print(monte_carlo)
    print((16-monte_carlo)*100)

cProfile.run('main()')
