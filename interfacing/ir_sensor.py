# Project 3: GEARS Robot
# File: ir_sensor.py
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
# Low level communication and error handling with IR sensor.
# Inputs: Surroundings
# Outputs: IR Detection
import time
import grovepi

def readIR(sensor): #sensor port is input for IR
    grovepi.pinMode(sensor, "INPUT")

    return(grovepi.analogRead(sensor))
