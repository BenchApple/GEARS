# Project 3: GEARS Robot
# File: grove_ultrasonic.py
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
# Handles low level communication and error handling with the Grove Ultrasonic Sensor. Mainly just a read function that takes the part and outputs the reading from the sensor.
# Inputs: External Surroundings
# Outputs: Grove Ultrasonic Readings

import grovepi

# Return the reading of the ultrasonic sensor in cm
def readGroveUltrasonic(PORT_DIGITAL):
    return grovepi.ultrasonicRead(PORT_DIGITAL)

# Tests, will only run if this file is ran as an executable
if __name__ == "__main__":
    import time
    # Print the readings from digital port 2 for 5 seconds
    for i in range(0,51):
    print(readGroveUltrasonic(2))
    time.sleep(0.1)