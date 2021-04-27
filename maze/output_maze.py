# Project 3: GEARS Robot
# File: output_maze.py
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
# Outputs the graphical representation of the maze
# Inputs: Final Map
# Outputs: Final Map

def output_maze(maze_map, origin):
    output = open("GEARS/team70_map.csv", "w")

    output.write("Team: 70\nMap: 0\nUnit Length: 40\nUnit: cm\nOrigin: (%d, %d)\n" % (origin[0], origin[1]))
    output.write("Notes: There are likely slight inaccuracies.")

    for i in range(0, len(maze_map)):
        for j in range(0, len(maze_map[i])):
            output.write(str(maze_map[i][j]))
            if j != len(maze_map[i]) - 1:
                output.write(", ")
        output.write("\n")
