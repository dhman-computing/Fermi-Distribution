# pylint: disable=wrong-import-order
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=consider-using-enumerate
# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name
# pylint: disable=consider-using-f-string
# pylint: disable=trailing-whitespace
# pylint: disable=no-member


# from math import exp, e
import numpy as np
import matplotlib.pyplot as plt
import pickle
from support1 import dist_f_N


No_of_points = 1000
xlimit = (0, 10000)
dx = 0.01
segment = (xlimit[1] - xlimit[0]) / dx
print(segment)
x_set = np.linspace(xlimit[0], xlimit[1], int(segment) + 1)

# len(x_set)
# print(x_set)

y_set = x_set.copy()

print(len(x_set))
print(len(y_set))

for i in range(int(segment + 1)):
  y_set[i] = dist_f_N(x_set[i], N=No_of_points)

plt.plot(x_set, y_set)
plt.grid()

segments = [0 for i in range(int(segment))]
# print(len(segments))

for i in range(int(segment)):
  segments[i] = (x_set[i], x_set[i+1])

# print(segments[0])
# print(segments[1])
# print(segments[3])
# print(segments[-2])
# print(segments[-1])

x_val = x_set[0:-1].copy()
point_in_x = x_set[0:-1].copy()

for i in range(len(segments)):
  x_val[i] = (segments[i][0] + segments[i][1]) / 2
  point_in_x[i] = dist_f_N(x_val[i], N=No_of_points)

plt.bar(x_val, point_in_x)

plt.savefig('plot.png')
plt.show()


data = {
    'x_set' : x_set,
    'y_set' : y_set,
    'x_val' : x_val,
    'point_in_x' : point_in_x,
    'segments' : segments,
}

with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)
