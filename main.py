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

# This is the main loop of the robot.
def main():
    robot = 

    # First we move forward 1 unit. This might have to be changed to account for 
    # getting to the center of an intersection.

if __name__ == "__main__":
    main()