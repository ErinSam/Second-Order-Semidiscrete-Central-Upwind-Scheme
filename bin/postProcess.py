"""
    Python script to process the data 
"""

# Erin Sam Joe | NITK '23 | Mechanical Engg. Major | Electronics & Electrical Engg. Minor


import sys
import glob
from math import sqrt
from scipy.ndimage import rotate
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from simple_colors import *


def processData(arg):
    """
        Function that bdscdsncf
    """

    files = glob.glob("./data/*.csv")

    print(yellow("\n\tCreating Images", 5))
    if ( arg == 0 ):
        # Holding the image open to view the final contour plot much better
        plotDensity(files[-1], True)

    else:
        # Saving all the files
        for i, fileName in enumerate(files):
            print(blue("Reading in "), fileName)
            plotDensity(fileName)



def plotDensity(fileName, hold=False):
    """
        Function that plots the density
    """
    # Reading in files
    df = pd.read_csv("./" + fileName)

    time = fileName.split("/")
    time = time[-1].split(".csv")
    time = time[0]
    print("Reading for %s" % time)

 
    # PROCESSING DATA
    row_count = df.shape[0]

    # Density 
    densityDist = np.array(df['rho'].tolist())
    densityDist = densityDist.reshape((int(sqrt(row_count)), -1))
    densityDist = rotate(densityDist, angle=90)

    # Locations
    x = np.array(df['x'].tolist())
    x = x.reshape((int(sqrt(row_count)), -1))
    x = rotate(x, angle=90)

    y = np.array(df['y'].tolist())
    y = y.reshape((int(sqrt(row_count)), -1))
    y = rotate(y, angle=90)
    

    # PLOTTING
    fig = plt.figure(figsize=(18.2, 7.9))
    #fig = plt.figure()
    fig.suptitle("Density Plots for time - " + time)

    # Density heatmap
    ax = fig.add_subplot(1,3, 1)
    ax = sns.heatmap(densityDist, xticklabels=False, yticklabels=False, 
                     cmap='viridis', vmin=0.0,
                     cbar_kws={"orientation": "horizontal", 
                               "label": "Density"})
    ax.set_title("Distribution")
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # Density Surface
    ax = fig.add_subplot(1,3, 2, projection='3d')
    ax.plot_surface(x, y, densityDist, cmap='viridis')
    ax.set_zlim(0.0,5.0)
    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.0, 1.0)
    #cset = ax.contour(x, y, densityDist, zdir='x', offset=0.0, cmap='magma')
    #cset = ax.contour(x, y, densityDist, zdir='y', offset=1.0, cmap='magma')
    #cset = ax.contour(x, y, densityDist, zdir='z', offset=0.0, cmap='plasma')
    ax.set_title("Surface Plot")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('Density')
    ax.view_init(elev=5.0, azim=-151)

    # Contour Plots
    ax = fig.add_subplot(1,3, 3)
    ax.contour(x, y, densityDist, 10, cmap='viridis')
    ax.set_title("Contour Plot")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    
    plt.tight_layout()
    plt.savefig("./data/img/CONFIG6REF200DT2.5e-05/%s.png" %time)
    if ( hold ):
        print(blue("Display the latest data... "))
        plt.show()


if __name__ == "__main__":
    if ( sys.argv[1] == "0" ):
        # Display and hold the latest data 
        processData(0)
    else:
        processData(-1)

