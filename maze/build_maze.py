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
from .graph import HazardNode
from .maze_navigate import navigate

# Takes the head of the graph structure created and builds the coordinate system that stores the actual output map.
def build_maze(root):
    # First we need to determine how big the output graph needs to be.
    maze_size = get_maze_size(root)

    # we need the length and width, so we do this.
    length = maze_size[0] - 1
    print(maze_size[2])
    print(maze_size[3])

    width = maze_size[2] + maze_size[3] + 2

    # Initialize the maze map to a bunch of 0s, since that indicates nothing regions.
    maze_map = [[0 for i in range(0, length)] for j in range(0, width)]
    col = 0
    row = maze_size[3] + 1
    coords = [row, col]

    print("Print maze pre-order traversal")
    root.print_preorder()

    print(length)
    print(width)
    for i in range(0, width):
        print(maze_map[i])
    print(coords)

    # Now taht we've printed everything we can actually fill the list with stuff.
    # This will get more complex as we add functionality to assist in making sure we know the maze entrance and exit.
    print("\n\nRebuilding Maze\n\n")
    maze_map = fill_map(root, maze_map, coords)
    print("\nFinal Map:")
    print("Exits the map at: " + str(coords))
    for i in range(0, width):
        print(maze_map[i])
    

# Fills out the mazes map given the root of the graph, the current maze map, and the current coordinates.
# The coords are listed as [row, col] 
def fill_map(node, maze_map, coords):
    if node != None:
        print(node)

        tracker = 0
        has_entered = False

        # Place the hazard in the correct spot.
        # Check to see if the current node is a hazard node.
        if isinstance(node, HazardNode):
            # Move to the proper coords.
            if node.get_orientation() == 0:
                coords[1] += 1
            elif node.get_orientation() == 1:
                coords[0] += 1
            elif node.get_orientation() == 2:
                coords[1] -= 1
            elif node.get_orientation() == 3:
                coords[0] -= 1

            if node.get_htype() == "heat":
                maze_map[coords[0]][coords[1]] = 2
            elif node.get_htype() == "magnet":
                maze_map[coords[0]][coords[1]] = 3

            # Make sure this doesn't enter the while loop.
            tracker = node.get_length()
            has_entered = True
        else:
            # Since we want to enter the loop once for all entries
            while tracker < node.get_length() or not has_entered:
                # Set the entry position to 2
                if node.get_parent() == None and not has_entered:
                    maze_map[coords[0]][coords[1]] = 2
                    tracker += 1

                    # If the root node was only of length 1, break the loop.
                    if node.get_length() == 1:
                        break

                # Now set the tracker to let us know it's already entered.
                has_entered = True

                # Move to the proper position
                if node.get_orientation() == 0:
                    coords[1] += 1
                elif node.get_orientation() == 1:
                    coords[0] += 1
                elif node.get_orientation() == 2:
                    coords[1] -= 1
                elif node.get_orientation() == 3:
                    coords[0] -= 1

                # Set the current position to having been occupied.
                maze_map[coords[0]][coords[1]] = 1

                # If the current position is the end of the maze indicate that.
                if tracker == node.get_length() - 1 and node.get_end():
                    maze_map[coords[0]][coords[1]] = 4

                print("Coords: " + str(coords))
                for i in range(0, len(maze_map)):
                    print(maze_map[i])

                assert(coords[1] >= 0)
                assert(coords[1] < len(maze_map[0]))
                assert(coords[0] >= 0)
                assert(coords[0] < len(maze_map))

                # Actually increment the tracker so we don't go forever.
                tracker += 1
                input("Enter to continue")

            print("Coords: " + str(coords))
            # Stores the coords locally so we can reset coords to the right value.
            local_coords = coords.copy()
            print("At Node: " + str(node))
            print("Traversing Right")
            maze_map = fill_map(node.get_right(), maze_map, coords)

            # Update the coords to the local
            print("At Node: " + str(node))
            print("Traversing Front")
            coords = local_coords.copy()
            maze_map = fill_map(node.get_front(), maze_map, coords)

            # Update the coords to the local
            print("At Node: " + str(node))
            print("Traversing Left")
            coords = local_coords.copy()
            maze_map = fill_map(node.get_left(), maze_map, coords)
        
    return maze_map

# Uses the root and an inorder traversal to get the dimensions of the maze.
def get_maze_size(root):
    return _maze_size(root, 1, 1, 1, 1)

# Gets the dimensions of the maze from this node on. Uses pre-order traversal.
# Node is the root of the current subtree. Length keeps track of how long the maze is (forward/backwards)
# Width keeps track of the position to the right and left of the starting row (0 means it's in the starting row)
# max_right and max_left keep track of the maximum displacements to the right and left of center.
# Returns a tuple of each of the non-node parameters in the below order.
def _maze_size(node, length, width, max_right, max_left):
    if node != None:
        # Get the orientation and adjust values accordingly
        if node.get_orientation() == 0:
            length += node.get_length()
        elif node.get_orientation() == 1:
            width += node.get_length()
        #elif node.get_orientation() == 2:
        #    length -= node.get_length()
        elif node.get_orientation() == 3:
            width -= node.get_length()

        # Now adjust the max_right and max_left values accordingly.
        if width > max_right:
            max_right = width
        if width < -max_left:
            max_left = -width

        # Now that we've adjusted those values, it's time to do our traversal.
        # Find the maze size from the right node.
        data = _maze_size(node.get_right(), length, width, max_right, max_left)
        length = data[0]
        width = data[1]
        max_right = data[2]
        max_left = data[3]

        # Find the maze size from the front node.
        data = _maze_size(node.get_front(), length, width, max_right, max_left)
        length = data[0]
        width = data[1]
        max_right = data[2]
        max_left = data[3]
            
        # find the maze size from the left node.
        data = _maze_size(node.get_left(), length, width, max_right, max_left)
        length = data[0]
        width = data[1]
        max_right = data[2]
        max_left = data[3]

    # Now that we have either traversed or ignored whatever was here, we return.
    return (length, width, max_right, max_left)
        
def main():
    root = navigate()
    build_maze(root)

if __name__ == "__main__":
    main()

