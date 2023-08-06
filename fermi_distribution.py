# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=consider-using-enumerate
# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name
# pylint: disable=consider-using-f-string
# pylint: disable=trailing-whitespace
# pylint: disable=no-member

# import math
# import os
from scipy.constants import Boltzmann, elementary_charge
import numpy as np
import matplotlib.pyplot as plt
import cv2


def fermi_distribution(E, E_F, T):
    k = Boltzmann / elementary_charge  # Boltzmann constant in eV/k
    exponent = (E - E_F) / (k * T)
    clipped_exponent = np.clip(exponent, -700, 700)
    return 1 / (np.exp(clipped_exponent) + 1)


def fermi_plot(T):
    E = np.linspace(0, 10, 10000)

    # Example usage:
    E_F = 5.0  # Fermi energy (in eV)
    # T = 0.001  # Temperature in Kelvin
    # energy_value = 0.5  # Energy value (in eV)

    F_E = np.zeros(len(E))

    for i in range(len(E)):
        F_E[i] = fermi_distribution(E[i], E_F, T)

    # Step 4: Plot the function
    plt.plot(E, F_E, label='Fermi Distribution')
    plt.xlabel('Energy(E)')
    plt.ylabel('F(E)')
    plt.title('Fermi Distribution')
    plt.xlim(0, 10)
    plt.ylim(-0.25, 1.25)
    plt.grid(True)
    plt.legend()

    if T == 0.0001:
        T = 0
    
    # Add text to the top right corner
    top_right_text = f"Tempareture = {T}K"
    plt.text(0.65, 0.85, top_right_text, ha='left',
             va='center', transform=plt.gca().transAxes)
    top_right_text = f"Fermi Energy = {E_F}eV"
    plt.text(0.65, 0.80, top_right_text, ha='left',
             va='center', transform=plt.gca().transAxes)

    png_path = "Fremi Plots\\fermi.png"
    
    plt.savefig(png_path)
    plt.clf()
    # print(f"Saved : {png_path}")

    # plt.show()
    return png_path

def fermi_plot_video(video_name, T, T_icrement, no, fps=30):
    image = fermi_plot(T)
    frame = cv2.imread(image)
    height, width, _ = frame.shape

    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    for i in range(no):
        image_path = fermi_plot(T)
        
        if T == 0.0001:
            T = 0
        T += T_icrement
        
        frame = cv2.imread(image_path)
        video.write(frame)
        print(f"Written frame: {i + 1}")

no = 2000
T = 0.0001
T_icrement = 5
video_name = 'Generated Videos\\fermi_distribution.mp4'

fermi_plot_video(video_name, T, T_icrement, no, fps=30)
