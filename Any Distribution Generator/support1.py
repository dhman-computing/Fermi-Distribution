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


def e_x(x):
    return e**(-1*x)

def dist_f_N(x, N=100):
    return e**(-1*x/N)

def dist_f_1(x, N=100):
    return e**(-1*x/N)/N


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
    
    return mid_pt_of_segment, value_of_f_for_mid_pt
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
