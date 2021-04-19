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
from .misc import cargo_release as cargo
from .walls import wall_sensing
from . import constants as r

# This is the main loop of the robot.
def main():
    robot = r.Robot()
    CELL_DIST = 40

    while not robot.navigated:
        # First we move forward 1 unit. This might have to be changed to account for 
        # getting to the center of an intersection.
        forward.forward_with_robot(robot, CELL_DIST)

        # Now we take the sensor readings
        walls = wall_sensing.senseWalls(robot)

        # Now deal with how the sensors read the hazards. We can now use this to change the walls
        # variable to deal with hazards and stuff.

        # Now we navigate the maze using the graph structure.
        prev_node = robot.cur_node # Stores the current node of the robot so we can compare.

        # I'm only going to worry about the standard case for now, no need to worry about the backtracking case for a bit.
        # Run the navigation step to update the new node.
        navigate.navigation_step(robot, walls[0], walls[1], walls[2])

        # Now we check to see if we're backtracking and act accordingly.
        if not robot.is_backtracking :
            # Compare the old node to the previous node to determine where to turn.
            if (prev_node.get_orientation() + 1) % 4 == robot.cur_node.get_orientation():
                # Turn 90 degrees clockwise.
                turn.turn_90_degrees(robot.bp, robot.l_motor, robot.r_motor, robot.dps, "CW")

                # Update the orientation of the robot.
                robot.set_orientation(robot.cur_node.get_orientation() + 1)
            
            elif (prev_node.get_orientation() - 1) % 4 == robot.cur_node.get_orientation():
                # Turn 90 degrees counterclockwise.
                turn.turn_90_degrees(robot.bp, robot.l_motor, robot.r_motor, robot.dps, "CCW")
                
                # Update the orientation of the robot.
                robot.set_orientation(robot.cur_node.get_orientation() - 1)
            # This handles both a new node in front as well as a non-new node that's front.
            else:
                # Do nothing because nothing needs to be done. Orientation stays the same and we don't turn.
                pass



if __name__ == "__main__":
    main()