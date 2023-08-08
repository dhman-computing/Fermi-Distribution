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
import matplotlib.pyplot as plt
import pickle as pkl
import random


def e_x(x):
    return e**(-1*x)

def dist_f_N(x, N=100):
    return e**(-1*x/N)

def dist_f_1(x, N=100):
    return e**(-1*x/N)/N

def xy(x):
    return x[0]*x[1]


def distribution_count(f, xlimit, precision):
    no_of_segments = int((xlimit[1] - xlimit[0]) / precision)
    
    x = np.linspace(xlimit[0], xlimit[1], no_of_segments + 1)
    # y = x.copy()
    
    segments = [0 for i in range(no_of_segments)]
    for i in range(no_of_segments):
        segments[i] = (x[i], x[i+1])
        
    mid_pt_of_segment = x[0:-1].copy()
    value_of_f_for_mid_pt = x[0:-1].copy()
    for i in range(no_of_segments):
        mid_pt_of_segment[i] = (segments[i][0] + segments[i][1]) / 2
        value_of_f_for_mid_pt[i] = f(mid_pt_of_segment[i])
    
    return mid_pt_of_segment, value_of_f_for_mid_pt, segments
    # pass

def plot_function(f,
                  xlimit: set[float], ylimit: set[float],
                  x_number=10000,
                  labels=('x', 'f(x)', 'Plot of f(x)', 'f(x)')):
    x = np.linspace(xlimit[0], xlimit[1], x_number)
    y = f(x)

    # Create the plot
    plt.plot(x, y, label=labels[3])
    plt.xlim(xlimit[0], xlimit[1])
    if ylimit != ():
        plt.ylim(ylimit[0], ylimit[1])

    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    plt.title(labels[2])
    plt.grid(True)
    plt.legend()
    
    # # Get the current date and time in a custom format
    # current_datetime = datetime.now()
    # formatted_datetime = current_datetime.strftime("%Y-%m-%d-%H-%M-%S")
    # # print(formatted_datetime)
    # png_path += f'-{formatted_datetime}.png'
    
    # plt.savefig(png_path)
    # if show:
    #     plt.show()
        
    # plt.clf()

    # return x, y
    return plt

def save_to_pkl(data, pkl_path):
    with open(pkl_path, 'wb') as file:
        pkl.dump(data, file)
        
def mc_integration(f, upper_limit, lower_limit, no_of_sample):
    sum_fx = 0
    for _ in range(no_of_sample):
        point = random.uniform(float(lower_limit), float(upper_limit))
        sum_fx += f(point)
        weightage = (upper_limit - lower_limit) / no_of_sample
    return sum_fx * weightage

def new_integration(f, y, delta_x, total_random_no):
    sum_y = sum(y)
    # print(sum_y)
    
    total_random_no_genareted = 0

    # plot.show()
    # plot.clf()
    integration = 0
    no_of_segments = len(delta_x)
    for i in range(no_of_segments):
        random_no_for_segment = int(total_random_no * y[i] / sum_y)
        # integration_for_segment = 0
        for _ in range(random_no_for_segment):
            random_no = random.uniform(delta_x[i][0], delta_x[i][1])
            integration += f(random_no)
        total_random_no_genareted += random_no_for_segment
        # integration += integration_for_segment / random_no_for_segment

    # print(total_random_no_genareted)
    integration = integration/total_random_no_genareted
    
    return integration

def r_integration(f, xlimit, N: int):
    integration = 0
    x_i = xlimit[0]
    
    dx = (xlimit[1] - xlimit[0]) / N
    for _ in range(N):
        integration += f(x_i)*dx
        
        x_i += dx
        
    return integration

def n_dimensional_monte_carlo_integration(f, xlimit, N):
    # xlist = [0 for _ in range(N)]
    n = len(xlimit) # dimension
    point = [0 for _ in range(n)]

    multiplier = 1
    result = 0
    for i in range(N):
        for j in range(n):
            point[j] = random.uniform(xlimit[j][0], xlimit[j][1])
            multiplier = multiplier * (xlimit[j][1] - xlimit[j][0])
        result += f(point)

    result = multiplier * result / N

    return result
