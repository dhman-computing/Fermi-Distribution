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
from datetime import datetime
# from scipy.constants import Boltzmann, elementary_charge
# import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from support import fermi_distribution as F
from support import plot_function as plotf


# veriable initialization

# Get the current date and time in a custom format
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d-%H-%M-%S")

T = 0.001
T_inc = 5
e_F = 1
repeat = 2000
fps = 30
video_name = f"fermi-distribution-{formatted_datetime}.mp4"

# Body

plot = plotf(F,
                  (0, 2), (-0.25, 1.25),
                  f_args=(e_F, T),
                  labels=('Energy(E)', 'F(E)', 'Plot of Fermi Distribution', 'Fermi Distribution (F(E))'))

# Add text to the top right corner
top_right_text = f"Tempareture = {T}K"
plot.text(0.65, 0.85, top_right_text, ha='left',
             va='center', transform=plt.gca().transAxes)
top_right_text = f"Fermi Energy = {e_F}eV"
plot.text(0.65, 0.80, top_right_text, ha='left',
             va='center', transform=plt.gca().transAxes)

plot_path = "plots\\fermi.png"
    
plot.savefig(plot_path)
plot.clf()

frame = cv.imread(plot_path)
height, width, _ = frame.shape

video = cv.VideoWriter(video_name, cv.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

T = T_inc

for i in range(repeat):
    plot = plotf(F,
                  (0, 2), (-0.25, 1.25),
                  f_args=(e_F, T),
                  labels=('Energy(E)', 'F(E)', 'Plot of Fermi Distribution', 'Fermi Distribution (F(E))'))
    
    # Add text to the top right corner
    top_right_text = f"Tempareture = {T}K"
    plot.text(0.65, 0.85, top_right_text, ha='left',
                va='center', transform=plt.gca().transAxes)
    top_right_text = f"Fermi Energy = {e_F}eV"
    plot.text(0.65, 0.80, top_right_text, ha='left',
                va='center', transform=plt.gca().transAxes)

    plot_path = "plots\\fermi.png"
        
    plot.savefig(plot_path)
    plot.clf()
    
    frame = cv.imread(plot_path)
    video.write(frame)
    print(f"Written Frame : {i:08d}")
    T += T_inc
    
video.release()

