# Project 3: GEARS Robot
# File: constants.py
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
# This file stores an object that handles all of the constants and attributes of the robot.
# this handles stuff like IR and ultrasonic ports, manages orientation and the current graph node
# as well as many other miscellaneous constants that we need like speed.
# Inputs: Probably everything
# Outputs: a fair amount.

# Imports
from .interfacing import motor as motor
from .interfacing import imu_interface as imu
from .interfacing import grove_ultrasonic as grove_ultra
from .interfacing import ir_sensor as ir
from .interfacing import lego_ultrasonic as lego_ultra

from .maze.graph import GraphNode
from .maze.graph import HazardNode

import brickpi3
import queue

class Robot:
    def __init__(self):
        # The ultrasonic ports for the right and the left.
        self.r_ultra = 5
        self.l_ultra = 6

        # Keeps track of the distance from either ultrasonic to the wall of the maze when the bot is exactly between the two walls
        self.CENTER_DIST = 12

        # The IMU object
        self.imu_obj = imu.init()

        # the sensor port for the IR sensor.
        self.ir_port = 4
        
        self.yellow_pin = 3
        self.green_pin = 2

        # Everything that we need for the motors
        self.bp = brickpi3.BrickPi3()
        self.r_motor = self.bp.PORT_C
        self.l_motor = self.bp.PORT_B

        self.dps = 300
        
        # Initialize the motors, which offsets the motor encoders and then set the motor limits.
        motor.init_motors(self.bp, self.r_motor, self.l_motor)
        motor.set_limits(self.bp, self.r_motor, self.l_motor, 100, self.dps)
        
        # Lego ultrasonic stuff.
        self.f_ultra = self.bp.PORT_3
        lego_ultra.init(self.bp, self.bp.PORT_3)

        # List to store all of the hazards we've accumulated.
        self.hazards_list = []

        # Stuff that we need to keep track of for the PID system.
        self.e_prev = 0

        self.KP = 0.2
        self.KI = 2
        self.KD = 5
        self.dt = 0.05

        self.P = 0
        self.I = 0
        self.D = 0

        # Stores variables that we need to keep track of for maze traversal
        self.root = GraphNode(0) # This is the first node of the maze
        self.cur_node = self.root
        self.node_number = 0
        self.navigated = False # VERY IMPORTANT. This variable tracks whether or not we have finished the maze

        self.cur_orientation = 0

        # These deal with backtracking
        self.is_backtracking = False # Stores whether or not we're in backtracking mode
        self.back_queue = queue.Queue() # Stores the backtracking queue.

    def get_orientation(self):
        return self._cur_orientation

    def set_orientation(self, new_orient):
        self._cur_orientation = (new_orient % 4)

    cur_orientation = property(get_orientation, set_orientation)


