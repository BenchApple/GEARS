# Project 3: GEARS Robot
# File: maze_navigate.py
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
# Responsible for actually navigating the maze. Will most likely implement DFS with Backtracking. 
# At any given location, takes corridor existences and creates data structures to store the form of the maze. 
# Also outputs the next direction/set of instructions for the GEARS to properly navigate the maze. 
# Still need to determine if this is what handles backtracking.
# Inputs: Relative Wall Data, Hazard Data, Path Existence
# Outputs: Maze Navigation, Maze Data Structure.

from .graph import GraphNode

def navigate():
    root = GraphNode(0)
    cur_node = root

    navigated = False

    # Navigate the maze. The loop goes as follows
    # Check the current sensors
    # if either of the non-front sensors are open, end the current node and create a new one.
    #   then travel down the path of the node that was just opened
    #   make sure to set the paths explored and existence values.
    # if only the front sensor is open, increase the current node length by 1
    # if none of the sensors are open, initiate backtracking.
    #   backtracking recursively searches for the first parent node that has both existent and
    #   unexplored paths remaining. If this doesn't return, then the maze should have already been sovled.
    while not navigated:
        sense = get_sensors()

        if sense[0] == 1 or sense[2] == 1:
            # Set the existence of paths.
            if sense[0] == 1:
                cur_node.set_exists("r")
            if sense[1] == 1:
                cur_node.set_exists("f")
            if sense[2] == 1:
                cur_node.set_exists("l")

            # Check to see which ones are open and travel down the first one.
            if sense[0] == 1:
                # Then choose the right one and travel down it.
                new_node = GraphNode((cur_node.get_orientation() + 1) % 4, cur_node)
                cur_node.set_right(new_node)
            # TODO finish this while loop and test it.

    return root

# Returns a tuple which references the openness of the 
def get_sensors():
    right = input("Enter right openness: ")
    front = input("Enter front openness: ")
    left = input("Enter left openness: ")

    return (right, front, left)

def main():
    root = navigate()

if __name__ == "__main__":
    main()
    