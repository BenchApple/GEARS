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

import time
from . import imu_interface as imu
from ..driving import turning
from .. import constants as r

# Determines if there is a within one maze block to the left, front, or right.
# Returns "none" if no magnet is detected, "1eft" if magnet is detected to the left, "front" if magnet is detected to the front, "right" if magnet is detected to the right
# TODO: Remove excess parameters by using the established constants
def checkMag(IMU, bp, left_motor_port, right_motor_port, dps):
    MAGNET_MAGNITUDE_CUTOFF = 200
    
    if (imu.getMagnMagnitude(IMU) > MAGNET_MAGNITUDE_CUTOFF):
        # Collect three magnitude values, each with the IMU closest to the right, front, and left maze units respectively
        turning.turn_90_degrees(bp, left_motor_port, right_motor_port, dps, "CW")
        left_mag_magn = imu.getMagnMagnitude(IMU)
        turning.turn_90_degrees(bp, left_motor_port, right_motor_port, dps, "CW")
        front_mag_magn = imu.getMagnMagnitude(IMU)
        turning.turn_90_degrees(bp, left_motor_port, right_motor_port, dps, "CW")
        right_mag_magn = imu.getMagnMagnitude(IMU)
        
        # Return the direction where the magnitude was the greatest
        if (right_mag_magn > front_mag_magn and right_mag_magn > left_mag_magn):
            return "right"
        # front_mag_magn is implicitly greater than right_mag_magn
        elif (front_mag_magn > left_mag_magn):
            return "front"
        # left_mag_magn is implicitly greater than right_mag_magn and front_mag_magn
        else:
            return "left"
    else:
        return "none"

def main():
    imu_obj = imu.init()
    robot = r.Robot()

    try: 
        while True:
#def checkMag(IMU, bp, left_motor_port, right_motor_port, dps):
       	    result = checkMag(imu_obj, robot.bp, robot.l_motor, robot.r_motor, robot.dps)
       	    print(result)
       	    time.sleep(1)
    except KeyboardInterrupt:
        robot.bp.reset_all()

if __name__ == "__main__":
    main()
