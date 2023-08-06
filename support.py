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
from scipy.constants import Boltzmann, elementary_charge
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv


def fermi_distribution(energy, fermi_energy, tempareture):
    k = Boltzmann / elementary_charge  # Boltzmann constant in eV/k
    exponent = (energy - fermi_energy) / (k * tempareture)
    clipped_exponent = np.clip(exponent, -1000, 1000)
    return 1 / (np.exp(clipped_exponent) + 1)


