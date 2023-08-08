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
import numpy as np
# import matplotlib.pyplot as plt
# import pickle as pkl
from support1 import distribution_count, \
    mc_integration, new_integration, r_integration#, plot_function#, save_to_pkl
# import random
# import cProfile


def F(x):
    # N = 1000
    return e**(-1*x)

def f(x):
    return 5*x**2+6*x

def g(x):
    return f(x)*F(x)

# plot = plot_function(f, (0, 10), (-0.1, 1.1), x_number=10**6)

def main():
    dx = 0.1
    xlimit = (0,1000)
    answer = 16

    x, y, delta_x = distribution_count(F, xlimit, dx)

    # plot.bar(x, y, color='red', width=dx)

    # text = f"Plot for f(x)=e**(-1*x) for segment length {dx}."
    # plot.text(1500, -0.40, text, ha='center')
    # plot.title(text)

    # plot.savefig(f'plot-{dx}.png',dpi=1500)

    total_random_no = 10**5
    integration = new_integration(f, y, delta_x, total_random_no)
    # print(total_random_no_genareted)
    # print(integration)
    # print(100 * (answer - integration) / answer)

    monte_carlo = mc_integration(g, xlimit[1], xlimit[0], total_random_no)
    # print(monte_carlo)
    # print(100 * (answer - monte_carlo) / answer)
    
    regular = r_integration(g, xlimit, total_random_no)
    # print(regular)
    # print(100 * (answer - regular) / answer)
    return answer, integration, monte_carlo, regular

# cProfile.run('main()')

N = 10000
ni = np.zeros(N)
mci = ni.copy()
ri = ni.copy()

for i in range(N):
    answer, ni[i], mci[i], ri[i] = main()

av_ni = sum(ni) / N
av_mci = sum(mci) / N
av_ri = sum(ri) / N

print(f"New Integration :: result : {av_ni}, error : {100 * (answer - av_ni) / answer}") 
print(f"Monte Carlo Integration :: result : {av_mci}, error : {100 * (answer - av_mci) / answer}") 
print(f"Regular Integration :: result : {av_ri}, error : {100 * (answer - av_ri) / answer}") 
