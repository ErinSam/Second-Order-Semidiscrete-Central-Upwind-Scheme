"""
    Python script that serves as the main controls for the meshClass
"""


# Erin Sam Joe | NITK '23 | Mechanical Engg. Major | Electronics & Electrical Engg. Minor


import sys

from simple_colors import *

sys.path.append("./../lib/")
import meshClass



def userInterface():
    """
        The user interface 
    """

    print(blue("\n\t\tSecond-Order Semidiscrete Central-Upwind Scheme", 1))
    print(blue("\t\t\t\t\t\t\t\tE. S. Joe", 2))

    print(yellow("\n\tRUNNING SIMULATION...", 5))
    controlSequence()


def controlSequence():
    """
        Main function that controls the mesh
    """

    # Control Properties
    numIterations = 125000
    saveFreq = 20

    # Mesh properties
    meshsize = 200
    dx = 0.005
    dt = 0.000025

    # Creating the mesh 
    mesh = meshClass.Mesh(meshsize, dx, dx)
    
    # Choosing an initial configurations (initial conditions)
    mesh.initialise(6)
    mesh.save()

    for i in range(1, numIterations+1):
        print(green("Simulation on iteration "+str(i), 2))
        mesh.update(dt)
        mesh.applyBC()
        if ( i % saveFreq == 0 ):
            print(green("Saving data for iteration "+str(i)))
            mesh.save()


if __name__ == "__main__":
    userInterface()
