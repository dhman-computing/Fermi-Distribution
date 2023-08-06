# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=consider-using-enumerate
# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name
# pylint: disable=consider-using-f-string
# pylint: disable=trailing-whitespace
# pylint: disable=no-member
# pylint: disable=trailing-newlines


# import math
# import os
# from datetime import datetime
from scipy.constants import Boltzmann, elementary_charge
import numpy as np
import matplotlib.pyplot as plt
# import cv2 as cv
# from pathlib import Path

# # Get the current date and time in a custom format
# current_datetime = datetime.now()
# formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted_datetime)


def fermi_distribution(energy, fermi_constants):
    k = Boltzmann / elementary_charge  # Boltzmann constant in eV/k
    fermi_energy, tempareture = fermi_constants
    exponent = (energy - fermi_energy) / (k * tempareture)
    clipped_exponent = np.clip(exponent, -700, 700)
    return 1 / (np.exp(clipped_exponent) + 1)


def plot_function(f,
                  xlimit: set[float], ylimit: set[float],
                  x_number=10000, f_args=(),
                  labels=('x', 'f(x)', 'Plot of f(x)', 'f(x)')):
    x = np.linspace(xlimit[0], xlimit[1], x_number)
    y = f(x, f_args)

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

