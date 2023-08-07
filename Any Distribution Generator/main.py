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
from support1 import distribution_count#, plot_function#, save_to_pkl
import random


def F(x):
    # N = 1000
    return e**(-1*x)

def f(x):
    return x**2


# plot = plot_function(f, (0, 10), (-0.1, 1.1), x_number=10**6)

dx = 0.01

x, y, delta_x = distribution_count(F, (0, 10), dx)

# plot.bar(x, y, color='red', width=dx)

# text = f"Plot for f(x)=e**(-1*x) for segment length {dx}."
# plot.text(1500, -0.40, text, ha='center')
# plot.title(text)

# plot.savefig(f'plot-{dx}.png',dpi=1500)

sum_y = sum(y)
# print(sum_y)
total_random_no = 10**8
total_random_no_genareted = 0

# plot.show()
# plot.clf()
integration = 0
no_of_segments = len(delta_x)
for i in range(no_of_segments):
    random_no_for_segment = int(total_random_no * y[i] / sum_y)
    # integration_for_segment = 0
    for j in range(random_no_for_segment):
        random_no = random.uniform(delta_x[i][0], delta_x[i][1])
        integration += f(random_no)
    total_random_no_genareted += random_no_for_segment
    # integration += integration_for_segment / random_no_for_segment

# print(total_random_no_genareted)    
integration = integration/total_random_no_genareted
print(total_random_no_genareted)
print(integration)
print((2 - integration)*100)
