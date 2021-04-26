# Project 3: GEARS Robot
# File: turning.py
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
# 
# Turn the robot appropriately. Must be able to do proper 90 degree turns and keep the robot between the walls as it changes corridors.
# Inputs: Driving, Wall Data, Maze Navigation Instructions
# Outputs: Turns robot

from ..interfacing.motor import *
import math as m
import time
import brickpi3
 
# Description: Has the GEARS bot perform a point rotation centered on the middle of the wheel axis (the center of the GEARS bot)
# Arguments: 
#   bp = brickpi3 object
#   left_motor_port = port # of the left motor (from the GEARS bot's perspective)
#   right_motor_port = port # of the right motor (from the GEARS bot's perspective)
#   dps = Speed at which the two motors will turn (will typically be set to the maximum dps defined in main)
#   direction = "CW" for clockwise turning and "CCW" for counter-clockwise turning
#   degrees = number of degrees the GEARS bot should turn
def turn_X_degrees(bp, LEFT_MOTOR_PORT, RIGHT_MOTOR_PORT, dps, direction, degrees):
    set_dps(bp, LEFT_MOTOR_PORT, 0)
    set_dps(bp, RIGHT_MOTOR_PORT, 0)

    robotCircumference = 18 * 3.14159
    wheelCircumference = 4.2 * 2 * 3.14159
    
    degreesTurn = m.floor(((robotCircumference * (degrees / 360)) / wheelCircumference) * 360)

    turnTime = (1 / dps) * degreesTurn

    if (direction == "CCW"):
        set_dps(bp, LEFT_MOTOR_PORT, dps)
        set_dps(bp, RIGHT_MOTOR_PORT, (-1 * dps))
    elif (direction == "CW"):
        set_dps(bp, LEFT_MOTOR_PORT, (-1 * dps))
        set_dps(bp, RIGHT_MOTOR_PORT, dps)

    time.sleep(turnTime)

    set_dps(bp, LEFT_MOTOR_PORT, 0)
    set_dps(bp, RIGHT_MOTOR_PORT, 0)
    
    return
  
# Implementation of turn_X_degrees with the degrees given as 90 
def turn_90_degrees(bp, left_motor_port, right_motor_port, dps, direction):
    turn_X_degrees(bp, left_motor_port, right_motor_port, dps, direction, 90)
    return

# Implementation of turn_X_degrees with the degrees given as 180 and doesn't require a direction argument
def turn_180_degrees(bp, left_motor_port, right_motor_port, dps):
    turn_X_degrees(bp, left_motor_port, right_motor_port, dps, "CW", 180)
    return

def main():
    bp = brickpi3.BrickPi3()
    left = bp.PORT_C
    right = bp.PORT_B
    init_motors(bp, right, left)

    #for d in range(20, 361, 20):
    #    turn_X_degrees(bp, left, right, 150, "CW", d)
    #    time.sleep(1)
    turn_X_degrees(bp, left, right, 150, "CCW", 100)
    bp.reset_all()

if __name__ == "__main__":
    main()


