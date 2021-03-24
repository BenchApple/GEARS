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

## This code just drives the robot forward while keeping it between the walls
def stay_between_walls(): 
    # Tuning parameters
    KP = 1 # Proportional gain
    KI = 10 # Integral gain
    KD = 2 # Derivative gain
    m_dps = 250 
    dt = 0.05

    current_pos = 0

    P = 0
    I = 0
    D = 0

    e_prev = 0

    # Hardware inits
    bp = brickpi3.BrickPi3()

    m_right = bp.PORT_C
    m_left = bp.PORT_B
    motor.init_motors(bp, m_right, m_left)

    motor.set_limits(bp, m_right, m_left, 90, m_dps)

    u_right = 5
    u_left = 6

    # Set the degrees per second for each motor
    motor.set_dps(bp, m_right, m_dps)
    motor.set_dps(bp, m_left, m_dps)

    accum_error = 0

    try:
        start_time = time.time()
        while (time.time() - start_time <= 20):
            u_right_reading = ultra.readGroveUltrasonic(u_right)
            u_left_reading = ultra.readGroveUltrasonic(u_left)
            print("Right Reading: " + str(u_right_reading))
            print("Left Reading: " + str(u_left_reading))
            # We can do it like this because we want them to be equidistant from the walls
            error = u_right_reading - u_left_reading
            print("Error: "+ str(error))

            P = KP * error
            I += KI * error * dt / 2
            D = KD * (error - e_prev) / dt

            value = P + I + D
            # If value is greater than 0, then we need to turn to the right, otherwise we need to turn to the left

            m_turn_val = int(value * 0.01)
            accum_error += abs(error)

            # Adjust the motor values according to what we have.
            motor.set_dps(bp, m_right, -(m_dps + m_turn_val))
            motor.set_dps(bp, m_left, -(m_dps - m_turn_val))

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

        print("Accumulated Error: " + str(accum_error));
        bp.reset_all()

    except KeyboardInterrupt:
        bp.reset_all()
        pass

def main():
    stay_between_walls()

if __name__ == "__main__":
    main()


