# Project 3: GEARS Robot
# File: maze_instructions.py
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
# Turns the output from Maze Navigation into actually usable navigational instructions for propulsion. 
# Should be in simple to understand forms, likely through the use of a more complex data structure. 
# Most complex part will be backtracking and the simplest part will be forward navigation.
# Inputs: Wall Data, Maze Navigation Decisions.
# Outputs: Maze Instructions

from ..driving import turning as turn
from .. import constants as r

# This function turns the robot based on where it needs to go
# This takes the previous node and the robot object (assuming it's been updated to a new node)
# compares the orientations, and turns apprpriately.
def standard_intersection(robot, prev_node):
    # Compare the old node to the previous node to determine where to turn.
    if (prev_node.get_orientation() + 1) % 4 == robot.cur_node.get_orientation():
        # Turn 90 degrees clockwise.
        turn.turn_90_degrees(robot.bp, robot.l_motor, robot.r_motor, robot.dps, "CW")

        # Update the orientation of the robot.
        robot.set_orientation(robot.cur_node.get_orientation())
    
    elif (prev_node.get_orientation() - 1) % 4 == robot.cur_node.get_orientation():
        # Turn 90 degrees counterclockwise.
        turn.turn_90_degrees(robot.bp, robot.l_motor, robot.r_motor, robot.dps, "CCW")
        
        # Update the orientation of the robot.
        robot.set_orientation(robot.cur_node.get_orientation())
    # This handles both a new node in front as well as a non-new node that's front.
    else:
        # Do nothing because nothing needs to be done. Orientation stays the same and we don't turn.
        pass
