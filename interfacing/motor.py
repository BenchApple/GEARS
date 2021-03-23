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
    # Offset the motor encoder.
    bp.offset_motor_encoder(port, get_position(bp, port))

# Initializes both motors
def init_motors(bp, port1, port2):
    init_motor(bp, port1)
    init_motor(bp, port2)
    
# Set the motor limits for each of the ports.
def set_limits(bp, port1, port2, power, dps):
    bp.set_motor_limits(port1, power = power, dps = dps)
    bp.set_motor_limits(port2, power = power, dps = dps)

# Gets the position of the motor using the encoder read.
def get_position(bp, port):
    return bp.get_motor_encoder(port)

# Get positions returns a tuple of positions of port 1 and port 2
def get_positions(bp, port1, port2):
    return [get_position(bp, port1), get_position(bp, port2)]

# Sets the given motor to the target position relative to the current position 
# This works in degrees
# Returns the final position of the motor.
def set_position_relative(bp, port, target):
    bp.set_motor_position_relative(port, target)
    return bp.get_position(bp, port)

# Sets the absolute motor position to target
# returns the position of the motor in degrees
def set_position_absolute(bp, port, target):
    bp.set_motor_position(port, target)
    return bp.get_position(bp, port)

# Sets the motor dps given the target dps and port. Returns the final dps of the motor
def set_dps(bp, port, target):
    bp.set_motor_dps(port, target)
    return target



