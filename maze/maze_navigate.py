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
from .graph import HazardNode

def navigate():
    maze_file = open("GEARS/maze/maze2.txt", 'r')

    root = GraphNode(0)
    cur_node = root
    node_number = 0

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
        sense = maze_file.readline()
        sense = sense.split()
        print(sense)
        for i in range(0, len(sense)):
            sense[i] = int(sense[i])
        #sense = get_sensors()

        # Do all of the hazards stuff.
        if sense[0] == 2:
            # Then we have a heat source.
            new_hazard = HazardNode("heat", \
                                    "This is a heat hazard with attributes of fire and heat", \
                                    cur_node, (cur_node.get_orientation() + 1) % 4)
            cur_node.set_right(new_hazard)
            print("Setting Right Hazard")
        elif sense[0] == 3:
            new_hazard = HazardNode("magnet", \
                                    "This is a magnet hazard with attributes of magneticy and fucking up your laptop.", \
                                    cur_node, (cur_node.get_orientation() + 1) % 4)
            cur_node.set_right(new_hazard)
            print("Setting Right Hazard")
        print(cur_node.get_right())

        # now for the front.
        if sense[1] == 2:
            # Then we have a heat source.
            new_hazard = HazardNode("heat", \
                                    "This is a heat hazard with attributes of fire and heat", \
                                    cur_node, cur_node.get_orientation())
            cur_node.set_front(new_hazard)
            print("Setting Front Hazard")
        elif sense[1] == 3:
            new_hazard = HazardNode("magnet", \
                                    "This is a magnet hazard with attributes of magneticy and fucking up your laptop.", \
                                    cur_node, cur_node.get_orientation())
            cur_node.set_front(new_hazard)
            print("Setting Front Hazard")
        print(cur_node.get_front())

        # Now for the left
        if sense[2] == 2:
            # Then we have a heat source.
            new_hazard = HazardNode("heat", \
                                    "This is a heat hazard with attributes of fire and heat", \
                                    cur_node, (cur_node.get_orientation() - 1) % 4)
            cur_node.set_left(new_hazard)
            print("Setting Left Hazard")
        elif sense[2] == 3:
            new_hazard = HazardNode("magnet", \
                                    "This is a magnet hazard with attributes of magneticy and fucking up your laptop.", \
                                    cur_node, (cur_node.get_orientation() - 1) % 4)
            cur_node.set_left(new_hazard)
            print("Setting Left Hazard")
        print(cur_node.get_left())

        # All of these are maze navigation oriented. They do not care about hazards.
        # Hazards are effectively impassable for them.
        if sense[1] == 4:
            print("We have traversed the maze!")
            cur_node.set_end()
            navigated = True
        elif sense[0] == 1 or sense[2] == 1:
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
                new_node = GraphNode((cur_node.get_orientation() + 1) % 4, cur_node, _number=node_number)
                cur_node.set_explored("r")
                cur_node.set_right(new_node)
                print("Setting right child.")
            elif sense[1] == 1:
                new_node = GraphNode(cur_node.get_orientation(), cur_node, _number=node_number)
                cur_node.set_explored("f")
                cur_node.set_front(new_node)
                print("Setting front child.")
            elif sense[2] == 1:
                new_node = GraphNode((cur_node.get_orientation() - 1) % 4, cur_node, _number=node_number)
                cur_node.set_explored("l")
                cur_node.set_left(new_node)
                print("Setting left child.")

            # Increment the node number lol
            node_number += 1
            
            cur_node = new_node
        # Since the previous if would have already caught the other cases, we only need to check this.
        elif sense[1] == 1: # We have == 1 here so that we can catch when we're at the end of the maze
            # If forward is the only one available, just increment the length.
            print("Incrementing current node length")
            cur_node.set_length(cur_node.get_length() + 1)
        # Equivalent to asking if all of them are false
        elif not(sense[0] == 1 and sense[1 == 1] and sense[2] == 1):
            # Then we need to initiate backtracking. 
            # Backtracking looks for the first parent that has an existent unexplored child.
            cur_node = backtrack(cur_node)
            print(cur_node)
            print("Backtracked node: " + str(cur_node))

            # Now that we have the node we backtracked to, we choose the next direction to go in
            exists = cur_node.get_exists()
            explored = cur_node.get_explored()

            # This should never be entered, but i'd rather have it here than not.
            if exists[0] and not explored[0]:
                new_node = GraphNode((cur_node.get_orientation() + 1) % 4, cur_node, _number=node_number)
                cur_node.set_explored("r")
                cur_node.set_right(new_node)
                print("Setting right child.")
            elif exists[1] and not explored[1]:
                new_node = GraphNode(cur_node.get_orientation(), cur_node, _number=node_number)
                cur_node.set_explored("f")
                cur_node.set_front(new_node)
                print("Setting front child.")
            elif exists[2] and not explored[2]:
                new_node = GraphNode((cur_node.get_orientation() - 1) % 4, cur_node, _number=node_number)
                cur_node.set_explored("l")
                cur_node.set_left(new_node)
                print("Setting left child.")

            # Increment the node number lol
            node_number += 1
            
            # Set the current node to the new node
            cur_node = new_node
        
        print(cur_node)
        print(cur_node.get_parent())
        print("")
        #input("Enter to Continue")

    return root

# Return the first node in the parent chain that has an unexplored existing child. 
def backtrack(cur_node):
    if cur_node.get_parent() != None:
        # Set the current node to be the parent of the current node.
        cur_node = cur_node.get_parent()

        # Get the current node's existence and explored
        exists = cur_node.get_exists()
        explored = cur_node.get_explored()

        #print(cur_node)
        print(exists)
        print(explored)
        print(exists[1] and not explored[1])
        print("")

        # If any of the paths both exist and are not explored, return the current node.
        if (exists[0] and not explored[0]) or (exists[1] and not explored[1]) or (exists[2] and not explored[2]):
            print(cur_node)
            return (cur_node)
        else:
            # If not, repeat the process with the next parent.
            return backtrack(cur_node)

# Returns a tuple which references the openness of the 
def get_sensors():
    right = int(input("Enter right openness: "))
    front = int(input("Enter front openness: "))
    left = int(input("Enter left openness: "))

    return (right, front, left)

def main():
    root = navigate()

    print("Pre-order traversal of the created tree.")
    root.print_preorder()

if __name__ == "__main__":
    main()
    