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

import math
import time
from . import imu_interface as imu
from ..driving import turning


# Determines if there is a within one maze block to the left, front, or right.
# Returns "none" if no magnet is detected, "1eft" if magnet is detected to the left, "front" if magnet is detected to the front, "right" if magnet is detected to the right
# NOTE: This function should only be called after the GEARS bot has been centered within the maze block and realigned.
# NOTE: If the MAGNET_MAGNITUDE_CUTOFF has too large of a magnitude, then the function may report a magnet in a maze block diagonal from the GEARS bot as existing within a connected maze block.
# NOTE: All parameters sent aside from IMU are for turning the GEARS bot 180 degrees
def checkMag(IMU, bp, left_motor_port, right_motor_port, dps):
    MAGNET_MAGNITUDE_CUTOFF = 120 

    magVector = imu.getMagnet(IMU)
    print(magVector)
    
    magCompX1 = magVector['x']
    magCompY1 = magVector['y']
    magCompZ1 = magVector['z']
    magCompX1_reverse = magCompX1 * -1
    magCompY1_reverse = magCompY1 * -1
    magCompZ1_reverse = magCompZ1 * -1
    
    # getMagnMagnitude was not directly called to prevent double retrieving the IMU magnetometer readings
    magnetMagnitude1 = math.sqrt((magCompX1 * magCompX1) + (magCompY1 * magCompY1) + (magCompZ1 * magCompZ1))
    print(magnetMagnitude1)
    
    if (magnetMagnitude1 > MAGNET_MAGNITUDE_CUTOFF):
        turning.turn_180_degrees(bp, left_motor_port, right_motor_port, dps):
        
        magCompX2 = magVector['x']
        magCompY2 = magVector['y']
        magCompZ2 = magVector['z']
        magCompX2_reverse = magCompX2 * -1
        magCompY2_reverse = magCompY2 * -1
        magCompZ2_reverse = magCompZ2 * -1
        
        # Add the difference between the IMU's intial and final positions
        # NOTE: May need to scale the difference by the overall magnitude of the magnetic force to get an exact location
        magCompY2 += 6
        magCompY2_reverse += 6
        
        magnetMagnitude2 = math.sqrt((magCompX2 * magCompX2) + (magCompY2 * magCompY2) + (magCompZ2 * magCompZ2))
        
        turning.turn_180_degrees(bp, left_motor_port, right_motor_port, dps):
        
        # Calculate the interior angle between the first and second readings direction vectors and their opposing direction vector
        readingDifference = math.acos((magCompX1 * magCompX2 + magCompY1 * magCompY2 + magCompZ1 * magCompZ2) / (magnetMagnitude1 * magnetMagnitude2))
        reverseDifference = math.acos((magCompX1_reverse * magCompX2_reverse + magCompY1_reverse * magCompY2_reverse + magCompZ1_reverse * magCompZ2_reverse) / (magnetMagnitude1 * magnetMagnitude2))
        
        if (reverseDifference < readingDifference):
            # Same thing as using reverse direction for determining direction
            magCompX1 *= -1
            magCompY1 *= -1
            magCompZ1 *= -1
        
        # Direction vectors determined through trigonometry, can provide derivation if necessary
        # The magVector is determined if it is within the range via two cross products and the resulting sign
        # NOTE: If a magVector is the same as one of the direction vectors then the program will report no magnet.  This should not cause an error as this should not occur in real-life.  (Famous last words)
        if ((((-0.62348 * magCompY1) - (0.78184 * magCompX1)) > 0) and (((-0.80154 * magCompY1) - (-0.59795 * magCompX1)) < 0)):
            return "left"
        elif ((((0.62348 * magCompY1) - (0.79184 * magCompX1)) > 0) and (((-0.62348 * magCompY1) - (0.79184 * magCompX1)) < 0)):
            return "front"
        elif ((((0.80154 * magCompY1) - (-0.59795 * magCompX1)) > 0) and (((0.62348 * magCompY1) - (0.79184 * magCompX1)) < 0)):
            return "right"
            
    return "none"

def main():
    imu_obj = imu.init()

    while True:
        result = checkMag(imu_obj)
        print(result)
        time.sleep(0.2)


if __name__ == "__main__":
    main()
