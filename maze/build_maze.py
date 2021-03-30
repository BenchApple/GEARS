# Project 3: GEARS Robot
# File: build_maze.py
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
# Takes the data structure from maze navigation and rebuilds the maze into graphical output. Optionally returns the optimal path through the maze.
# Inputs: Global Location Data, Maze Navigation Data
# Outputs: Maze Data Structure

from .graph import GraphNode

# Takes the head of the graph structure created and builds the coordinate system that stores the actual output map.
def build_maze(root):
    # First we need to determine how big the output graph needs to be.
    pass


# Uses the root and an inorder traversal to get the dimensions of the maze.
def get_maze_size(root):
    pass

# Gets the dimensions of the maze from this node on. Uses pre-order traversal.
def _maze_size(node, length, max_right, max_left):

