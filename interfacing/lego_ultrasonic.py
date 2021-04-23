# Project 3: GEARS Robot
# File: lego_ultrasonic.py
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
# Handles low level communication and error handling with Lego Ultrasonic. Mainly just reading the sensor data.
# Inputs: Surroundings
# Outputs: Ultrasonic Readings

from __future__ import print_function # use python 3 syntax but make it compatible with python 2
from __future__ import division       #                           ''

import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers

def init(bp, port):
    bp.set_sensor_type(port, bp.SENSOR_TYPE.EV3_ULTRASONIC_CM)
    time.sleep(5)

def legoUltrasonic(bp, sensor): #port must be declared in same way as brick would i.e. BP.PORT_1
    return(bp.get_sensor(sensor))

def main():
    bp = brickpi3.BrickPi3()

    port = bp.PORT_3

    init(bp, port)
    try:
        while True:
            print(legoUltrasonic(bp, port))
            time.sleep(0.05)
    except KeyboardInterrupt:
        bp.reset_all()

if __name__ == "__main__":
    main()

