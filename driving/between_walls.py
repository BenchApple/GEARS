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

import os
import time
import brickpi3
from ..interfacing import motor as motor
from ..interfacing import grove_ultrasonic as ultra
from ..interfacing import MPU9250
from ..interfacing import imu_interface as i

## This code just drives the robot forward while keeping it between the walls
def stay_between_walls(): 
    # Tuning parameters
    KP = 0.5 # Proportional gain
    KI = 2 # Integral gain
    KD = 3 # Derivative gain
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

    m_dps = 250

    motor.set_limits(bp, m_right, m_left, 90, m_dps)

    u_right = 5
    u_left = 6

    # Target pos represents where we want to be, which should be a sum of 240 cm^2
    target_dist_sum  = ultra.readGroveUltrasonic(u_right) + ultra.readGroveUltrasonic(u_left)

    # Set the degrees per second for each motor
    motor.set_dps(bp, m_right, m_dps)
    motor.set_dps(bp, m_left, m_dps)

    accum_error = 0
    # Tracks which direction we have been turning. 1 means we have been turning to the left (CCW)
    # -1 means we have been turning to the right (CW)
    turn_dir = 0

    # turn_tracker keeps track of how many iterations in a row we've been turning the opposite direction of the current turn_dir
    turn_tracker = 0

    # turn_limit denotes the amount of iteratiosn in a row that the turning direction has to be different in order to swithc the direction.
    turn_limit = 5

    try:
        start_time = time.time()
        while (time.time() - start_time <= 20):
            u_right_reading = ultra.readGroveUltrasonic(u_right)
            u_left_reading = ultra.readGroveUltrasonic(u_left)
            print("Right Reading: " + str(u_right_reading))
            print("Left Reading: " + str(u_left_reading))
            # We can do it like this because we want them to be equidistant from the walls
            dist_error = u_right_reading - u_left_reading

            # dist_sum_error tracks the error in rotation by taking the sum of the distances.
            dist_sum_error = (u_right_reading + u_left_reading) - target_dist_sum
            dist_sum_error *= (10* turn_dir)

            print("Distance Error: " + str(dist_error))
            print("Distance Sum Error: " + str(dist_sum_error))

            # Sum the two errors to get the final error.
            error = dist_error + dist_sum_error
            print("Error: "+ str(error))

            P = KP * error
            I += KI * error * dt / 2
            D = KD * (error - e_prev) / dt

            value = P + I + D
            # If value is greater than 0, then we need to turn to the right, otherwise we need to turn to the left

            m_turn_val = int(value * 0.01)
            print("Turn Value: " + str(m_turn_val))
            right_dps = -(m_dps + m_turn_val)
            left_dps = -(m_dps - m_turn_val)
            # Adjust the motor values according to what we have.
            motor.set_dps(bp, m_right, right_dps)
            motor.set_dps(bp, m_left, left_dps)

            accum_error += abs(error)

            print("Right motor dps: " + str(right_dps))
            print("Left motor dps: " + str(left_dps))

           #  NOTE: System is working about as intended, needs testing though.
           # One pootential issue is rotation messing up the readings we want (needs to be tested)
           # Can offset this using the gyroscope to calculate relative orientation and calculate actual
           #       distance to the walls using trig
           # Overall we just need a lot more testing in order to make sure that this works well.
            
            # Check to change the turn direction.
            if right_dps > left_dps and turn_dir != -1:
                turn_tracker += 1 
                if turn_tracker > turn_limit:
                    turn_dir = -1
                    turn_tracker = 0
            elif left_dps > right_dps and turn_dir != 1:
                turn_tracker += 1
                if turn_tracker > turn_limit:
                    turn_dir = 1
                    turn_tracker = 0
            
            print(value)
            time.sleep(dt)
            print("")

        print("Accumulated Error: " + str(accum_error));
        bp.reset_all()

    except KeyboardInterrupt:
        bp.reset_all()
        pass

def track_rotational():
    imu = i.init()

    init_pos = 0 

    dt = 0.05
    cur_pos = init_pos
    prev_reading = 0
    try:
        while True:
            cur_reading = i.getZAngular(imu) - 1

            cur_pos += (cur_reading * dt)
            prev_ang = cur_reading
            print("Current Position: " + str(cur_pos))

    except KeyboardInterrupt:
        pass


def main():
    stay_between_walls()
    #track_rotational()

if __name__ == "__main__":
    main()


