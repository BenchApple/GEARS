# Project 3: GEARS Robot
# File: main.py
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
# This file holds the main loop of the robot. Imports everything, outputs a working robot.

from .driving import propulsion as forward
from .driving import turning as turn
from .hazards import hazard_process
from .hazards import hazard_sense
from .maze import graph
from .maze import maze_navigate as navigate
from .maze import build_maze as build
from .maze import maze_instructions as instruct
from .misc import cargo_release as cargo
from .walls import wall_sensing
from . import constants as r
import queue

def testing_walls():
    walls = [0,0,0]

    walls[0] = int(input("Enter right wall status: "))
    walls[1] = int(input("Enter front wall status: "))
    walls[2] = int(input("Enter left wall status: "))

    return walls

# This is the main loop of the robot.
def main():
    robot = r.Robot()
    CELL_DIST = 40

    while not robot.navigated:
        # First we move forward 1 unit. This might have to be changed to account for 
        # getting to the center of an intersection.
        forward.forward_with_robot(robot, CELL_DIST)

        # Now we take the sensor readings
        #walls = wall_sensing.senseWalls(robot)
        walls = testing_walls()

        # Now deal with how the sensors read the hazards. We can now use this to change the walls
        # variable to deal with hazards and stuff.

        # Now we navigate the maze using the graph structure.
        prev_node = robot.cur_node # Stores the current node of the robot so we can compare.

        # I'm only going to worry about the standard case for now, no need to worry about the backtracking case for a bit.
        # Run the navigation step to update the new node.
        navigate.navigation_step(robot, walls[0], walls[1], walls[2])

        # Now we check to see if we're backtracking and act accordingly.
        if not robot.is_backtracking:
            instruct.standard_intersection(robot, prev_node)
            print("Robot orientation is " + str(robot.cur_orientation))
        else:
            # Handle the backtracking here. This will suck, yes I know
            # Remember that cur_node becomes the next node that we will go to. 
            # The pre-inntersection node is not included in the FIFO queue either.
            # TODO Test to see if the FIFO queue is working correctly.
            temp_queue = queue.Queue()
            while not robot.back_queue.empty():
                val = robot.back_queue.get()
                temp_queue.put(val)
                print(val)

            # TODO next step is to write the instructional code that handles actually leading the 
            # robot back through the maze

            # Now that we're done with backtracking, we just need to reset the backtracking tracker
            robot.is_backtracking = False

if __name__ == "__main__":
    main()