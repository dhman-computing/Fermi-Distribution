from support1 import r_integration as rint
from support1 import plot_function as plf
# import matplotlib.pyplot as plt

def f(x):
    return x**40


xlimit = (-100, 100)
N = 10**6

plot = plf(f,
           xlimit, (),
                  x_number=10000,
                  labels=('x', 'f(x)', 'x**2', 'x**2'))

steps = 100
resolution = (xlimit[1] - xlimit[0]) / steps
modified_upper_limit = float(xlimit[0])

x = []
y = []

for _ in range(int(steps)):
    modified_upper_limit += resolution
    y.append(rint(f, (xlimit[0], modified_upper_limit), N) + (-100**41)/41)
    x.append(modified_upper_limit)
    print(_)
  
plot.plot(x, y, color = 'red')

plot.show()
# print(f"Result : {result}")

# answer = float(input("Correct Answer : "))

# print(f"Error : {100 * (result - answer) / answer}")
