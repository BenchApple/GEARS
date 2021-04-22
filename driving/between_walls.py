# Project 3: GEARS Robot
# File: between_walls.py
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
# Keeps the robot from bumping into the walls while driving through corridors. Should implement basic control theory (as discussed in class).
# Inputs: Wall Closeness, Driving State, Corridor Data
# Outputs: Keeping bot between walls.

import sys
import os
#sys.path.append(os.path.realpath('.'))
import time
import brickpi3
from ..interfacing import motor as motor
#import GEARS.interfacing.motor as motor
from ..interfacing import grove_ultrasonic as ultra
from ..import constants as c

# Takes the robot object and performs one loop of PID on it.
# This one does not include the time step that the normal one has at the end.
def pid_one_loop(robot):
    u_right_reading = ultra.readGroveUltrasonic(robot.r_ultra)
    u_left_reading = ultra.readGroveUltrasonic(robot.l_ultra)
    # We can do it like this because we want them to be equidistant from the walls
    error = u_right_reading - u_left_reading

    robot.P = robot.KP * error
    robot.I += robot.KI * error * robot.dt / 2
    robot.D = robot.KD * (error - robot.e_prev) / robot.dt

    value = robot.P - robot.I + robot.D
    # If value is greater than 0, then we need to turn to the right, otherwise we need to turn to the left

    m_turn_val = int(value * 0.1)
    # Adjust the motor values according to what we have.
    motor.set_dps(robot.bp, robot.r_motor, robot.dps + m_turn_val)
    motor.set_dps(robot.bp, robot.l_motor, robot.dps - m_turn_val)

    #print("Right motor dps: " + str(robot.dps - m_turn_val))
    #print("Left motor dps: " + str(robot.dps + m_turn_val))

# Performs the pid loop if we're missing one wall, ie when we enter an intersection.
# robot is the robot object, side is the side missing. "right" or "r" means right side missing, 
# "left" or "l" means left side missing
# initial reading takes the reading of the non-missing side right before it dropped off. This will
# be the target value.
def pid_missing_wall(robot, side):
    if side == "right" or side == "r":
        u_left_reading = ultra.readGroveUltrasonic(robot.l_ultra)
        # We can do it like this because we want them to be equidistant from the walls
        error = robot.CENTER_DIST - u_left_reading

    elif side == "left" or side == "l":
        u_right_reading = ultra.readGroveUltrasonic(robot.r_ultra)
        # We can do it like this because we want them to be equidistant from the walls
        error = u_right_reading - robot.CENTER_DIST 
        #error = init_reading - u_right_reading

    print("Calculated Error is: " + str(error))

    robot.P = robot.KP * error
    robot.I += robot.KI * error * robot.dt / 2
    robot.D = robot.KD * (error - robot.e_prev) / robot.dt

    value = robot.P - robot.I + robot.D
    # If value is greater than 0, then we need to turn to the right, otherwise we need to turn to the left

    m_turn_val = int(value * 0.1)
    # Adjust the motor values according to what we have.
    motor.set_dps(robot.bp, robot.r_motor, robot.dps + m_turn_val)
    motor.set_dps(robot.bp, robot.l_motor, robot.dps - m_turn_val)

    #print("Right motor dps: " + str(robot.dps - m_turn_val))
    #print("Left motor dps: " + str(robot.dps + m_turn_val)) 

## This code just drives the robot forward while keeping it between the walls
def stay_between_walls(): 
    # Tuning parameters
    KP = 0.5 # Proportional gain
    KI = 0.5 # Integral gain
    KD = 0.5 # Derivative gain
    dt = 0.05

    P = 0
    I = 2
    D = 0

    e_prev = 0

    # Hardware inits
    bp = brickpi3.BrickPi3()

    m_right = bp.PORT_C
    m_left = bp.PORT_B
    motor.init_motors(bp, m_right, m_left)
    m_dps = 80

    motor.set_limits(bp, m_right, m_left, 90, m_dps)

    u_right = 5
    u_left = 6

    # Set the degrees per second for each motor
    motor.set_dps(bp, m_right, m_dps)
    motor.set_dps(bp, m_left, m_dps)

    try:
        while True:
            u_right_reading = ultra.readGroveUltrasonic(u_right)
            u_left_reading = ultra.readGroveUltrasonic(u_left)
            # We can do it like this because we want them to be equidistant from the walls
            error = u_right_reading - u_left_reading

            P = KP * error
            I += KI * error * dt / 2
            D = KD * (error - e_prev) / dt

            value = P + I + D
            # If value is greater than 0, then we need to turn to the right, otherwise we need to turn to the left

            m_turn_val = int(value * 0.1)
            # Adjust the motor values according to what we have.
            motor.set_dps(bp, m_right, m_dps - m_turn_val)
            motor.set_dps(bp, m_left, m_dps + m_turn_val)

            print("Right motor dps: " + str(m_dps - m_turn_val))
            print("Left motor dps: " + str(m_dps + m_turn_val))

           #  NOTE: System is working about as intended, needs testing though.
           # One pootential issue is rotation messing up the readings we want (needs to be tested)
           # Can offset this using the gyroscope to calculate relative orientation and calculate actual
           #       distance to the walls using trig
           # Overall we just need a lot more testing in order to make sure that this works well.
            
            
            print(value)
            time.sleep(dt)
            print("")
    except KeyboardInterrupt:
        #bp.reset_all()
        pass

def main():
    stay_between_walls()

if __name__ == "__main__":
    main()


