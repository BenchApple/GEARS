# Project 3: GEARS Robot
# File: hazard_output.py
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
# Outputs the location and type of each hazard.
# Inputs: Hazard Location and Type
# Outputs: Formal Hazard Output

def output_hazards(robot):
    output = open("GEARS/team70_hazards.csv")

    output.write("Team: 70\nMap: 0\nNotes: This may have slight errors, and it has no actual parameter values.\n")
    output.write("\nReseource Type, Parameter of Interest, Paramter, Resource X Coordinate, Resource Y Coordinate\n")

    for hazard in robot.hazards_list:
        output.write(str(hazard))
        output.write("\n")