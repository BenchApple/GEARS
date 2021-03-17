# Project 3: GEARS Robot
# File: imu_interface.py
# Date: 3/14/21
# By: Alex Wiseman
# ajwisema
# Ben Chappell
# chappeb
# Trevor Moorman
# tmoorma
# Cole Kingery
# ckinger
# Section: 5
# Team: 70
#
# ELECTRONIC SIGNATURE
# Ben Chappell
# Cole Kingery
# Trevor Moorman
# Alex Wiseman
# 
# The electronic signatures above indicate that the program
# submitted for evaluation is the combined effort of all
# team members and that each member of the team was an
# equal participant in its creation. In addition, each
# member of the team has a general understanding of
# all aspects of the program development and execution.
# 
# Low level communication and error handling with IMU
# Inputs: Surroundings
# Outputs: Magnetic Field Intensity, Velocity Data

from MPU9250 import MPU9250
import sys
import time
from math import sqrt

# This gets all of the accel data and returns it as a dictionary with the major axes as keys.
# Only argument takes the imu object.
def getAccel(imu): 
    # Get the acceleration reading from the IMU object
    accel = imu.readAccel()

    # Return the dictionary
    return accel

# Gets the x acceleration value given the mpu imu object.
def getAccelX(imu):
    # Call the main getAccel function to get the dictionary and return the x value
    return getAccel(imu)['x']

# Gets the y acceleration value given the mpu imu object.
def getAccelY(imu):
    # Call the main accel function to get the dictionary and return the y value
    return getAccel(imu)['y']

# Same as X and Y functions
def getAccelZ(imu):
    # Call main function
    return getAccel(imu)['z']

# Get all of the magnetic data.
def getMagnet(imu):
    # Get the magnetic reading from the imu object
    magn = imu.readMagnet()

    # Return the dictionary
    return magn

def getMagnMagnitude(imu):
    # Calculate the magnitude of the magnetic force.
    magnetMagnitude = sqrt((getMagnet(imu) ** 2) + (getMagnet(imu) ** 2) + (getMagnet(imu) ** 2))

    return magnetMagnitude