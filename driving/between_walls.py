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

import time
import brickpi3
import interfacing.motor

## This code just drives the robot forward while keeping it between the walls
def stay_between_walls(bp, right, left, u_right, u_left):
    # Tuning parameters
    KP = 0.0 # Proportional gain
    KI = 0.0 # Integral gain
    KD = 0.0 # Derivative gain

    # Target pos represents where we want to be, which should be a sum of 240 cm^2
    target_pos = 240 # we are trying to minimize the distance, so we just set it to 0

    current_pos = 0

    P = 0
    I = 2
    D = 0

    e_prev = 0

    # Initialize our hardware



