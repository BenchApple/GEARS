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
sys.path.append("/team_70/")
import time
import brickpi3
import GEARS.interfacing.motor as motor
import GEARS.interfacing.grove_ultrasonic as ultra

## This code just drives the robot forward while keeping it between the walls
def stay_between_walls(): 
    # Tuning parameters
    KP = 1.0 # Proportional gain
    KI = 1.0 # Integral gain
    KD = 1.0 # Derivative gain
    dt = 0.02

    # Target pos represents where we want to be, which should be a sum of 240 cm^2
    target_pos = 240 # we are trying to minimize the distance, so we just set it to 0

    current_pos = 0

    P = 0
    I = 2
    D = 0

    e_prev = 0

    # Hardware inits
    bp = brickpi3.BrickPi3()

    m_right = bp.PORT_A
    m_left = bp.PORT_B
    motor.init_motors(bp, m_right, m_left)

    motor.set_limits(bp, m_right, m_left, 90, 180)

    u_right = 5
    u_left = 6

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
            print(value)
            time.sleep(dt)

    except KeyboardInterrupt:
        bp.reset_all()

def main():
    stay_between_walls()

if __name__ == "__main__":
    main()


