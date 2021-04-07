# Project 3: GEARS Robot
# File: magnet_sensor.py
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
# Detecting magnetic hazards
# Inputs: IMU Sensor Data
# Outputs: Magnetic Hazards

# TODO: import "imu_interface" for "getMagnet"
from math import sqrt

# Determines if there is a within one maze block to the left, front, or right.
# Returns "none" if no magnet is detected, "1eft" if magnet is detected to the left, "front" if magnet is detected to the front, "right" if magnet is detected to the right
# NOTE: This function should only be called after the GEARS bot has been centered within the maze block and realigned.
# NOTE: If the MAGNET_MAGNITUDE_CUTOFF has too small of a magnitude, then the function may report a magnet in a maze block diagonal from the GEARS bot as existing within a connected maze block.
def checkMag(IMU):
    magVector = getMagnet(IMU)
    
    magCompX = magVector['x']
    magCompY = magVector['y']
    magCompZ = magVector['z']
    
    # getMagnMagnitude was not directly called to prevent double retrieving the IMU magnetometer readings
    magnetMagnitude = sqrt((magCompX * magCompX) + (magCompY * magCompY) + (magCompZ * magCompZ))
    
    # TODO: Need to experimentally determine magnetMagnitude cutoff
    if (magnetMagnitude > MAGNET_MAGNITUDE_CUTOFF):
        # Direction vectors determined through trigonometry, can provide derivation if necessary
        # The magVector is determined if it is within the range via two cross products and the resulting sign
        # NOTE: If a magVector is the same as one of the direction vectors then the program will report no magnet.  This should not cause an error as this should not occur in real-life.  (Famous last words)
        if ((((-0.62348 * magCompY) - (0.78184 * magCompX)) > 0) and (((-0.80154 * magCompY) - (-0.59795 * magCompX)) < 0)):
            return "left"
        elif ((((0.62348 * magCompY) - (0.79184 * magCompX)) > 0) and (((-0.62348 * magCompY) - (0.79184 * magCompX)) < 0)):
            return "front"
        elif ((((0.80154 * magCompY) - (-0.59795 * magCompX)) > 0) and (((0.62348 * magCompY) - (0.79184 * magCompX)) < 0)):
            return "right"
            
    return "none"