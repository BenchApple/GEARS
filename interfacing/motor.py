# Project 3: GEARS Robot
# File: motor.py
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
# Handles Low level communication with motors, such as motor encoders, turning the motors at specific speeds or distances, etc. The most basic motor Code. Should be built first.
# Inputs: Motor Encoders
# Outputs: Motor Action, Motor encoder data

import brickpi3

# Initiailizing the motor, offsetting the motor encoder given the bp object and the motor port
def init_motor(bp, port):
    pass

# Set the motor limits for each of the ports.
def motor_limits(bp, port1, port2):
    pass

# Sets the given motor to the target position given the current position
# Returns the final position of the motor.
def set_motor_position(bp, port, current, target):
    pass

# Sets the motor dps given the target dps and port. Returns the final dps of the motor
def set_motor_dps(bp, port, target):
    pass



