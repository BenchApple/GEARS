# Project 3: GEARS Robot
# File: graph.py
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
# This is the file for the main data structure used in maze navigation and building. 
# This is basically just the structuring of how all that stuff works efficiently.

class GraphNode(object):
    def __init__(self, _orientation, _parent = None):
        # Orientation refers to which direction the node is oritented when first going through it. 
        # 0 means aligned with maze entrance, 1 is 90 degrees right, 2 is backwards aligned with entrance, 3 is backwards to 1.
        self.orientation = _orientation

        # When backtracking, parent node represents the node this node stemmed from
        # NOTE Backtracking will effectively have to go back to the parent node and work from there.
        self.parent = _parent

        # Initialize all children to None
        self.child_front = None
        self.child_left = None
        self.child_right = None

        # Keeps track of whether or not the paths have been explored.
        self.explored_front = False
        self.explored_right = False
        self.explored_left = False

        # Keeps track of whether paths exist out of each of the directions.
        self.exists_right = False
        self.exists_left = False
        self.exists_front = False

        # Length refers to the amount of standard units long that this node is. for example, a hall 40 cm long will have length 1.
        self.length = 1

    def __str__(self):
        return "Orientation: %d; Length: %d; Explored: Right - %d, Front - %d, Left - %d; Exists: Right - %d, Front - %d, Left - %d" % \
                (self.orientation, self.length, self.explored_right, self.explored_front, self.explored_left, self.exists_right, self.exists_front, self.exists_left)

    # Prints the inorder traversal with the current node as the root
    def print_preorder(self):
        print(self)
        print("")
        
        if self.get_right() != None:
            self.get_right().print_preorder()
        
        if self.get_front() != None:
            self.get_front().print_preorder()

        if self.get_left() != None:
            self.get_left().print_preorder()



    # Returns the orientation of the node.
    def get_orientation(self):
        return self.orientation

    # Sets the length of the current node to whatever is passed into it
    def set_length(self, new_len):
        if isinstance(new_len, int):
            self._length = new_len
        else:
            raise Exception("Error: Invalid data type for setting the length of the current node.")

    def get_length(self):
        return self._length

    # Since there should be no need to set exists to false once it's been set to true, we won't even need a boolean argument.
    # Dir specifies which direction is getting set 'f' and 'front' work for front, same for the other directions.
    # These keep track of which paths explore coming out of this node.
    # NOTE: These explored values are for the current node.
    def set_exists(self, direc):
        if direc == "f" or direc == "front":
            self.exists_front = True
            return self.get_exists()
        elif direc == "r" or direc == "right":
            self.exists_right = True
            return self.get_exists()
        elif direc == "l" or direc == "left":
            self.exists_left = True
            return self.get_exists()
        else:
            raise Exception("Error: Invalid direction for setting exists values.")

    def get_exists(self):
        return (self.exists_right, self.exists_front, self.exists_left)

    # Since there should be no need to set explored to false once it's been set to true, we won't even need a boolean argument.
    # Dir specifies which direction is getting set 'f' and 'front' work for front, same for the other directions.
    # NOTE: These explored values are for the current node, not the parent of the current node.
    def set_explored(self, direc):
        if direc == "f" or direc == "front":
            self.explored_front = True
            return self.get_explored()
        elif direc == "r" or direc == "right":
            self.explored_right = True
            return self.get_explored()
        elif direc == "l" or direc == "left":
            self.explored_left = True
            return self.get_explored()
        else:
            raise Exception("Error: Invalid direction for setting explored values.")

    # Returns a tuple of the exploration status of each of the directions.
    # 0 - right, 1 - front, 2 - left
    def get_explored(self):
        return (self.explored_right, self.explored_front, self.explored_left)

    # Returns the parent of the current node.
    def get_parent(self):
        return self.parent

    def set_front(self, new_child):
        if isinstance(new_child, GraphNode) or new_child == None:
            self._child_front = new_child
        else:
            raise Exception("Error: Attempted to put non-GraphNode object as front child")

    def get_front(self):
        return self._child_front

    def set_right(self, new_child):
        if isinstance(new_child, GraphNode) or new_child == None:
            self._child_right = new_child
        else:
            raise Exception("Error: Attempted to put non-GraphNode object as right child")

    def get_right(self):
        return self._child_right

    def set_left(self, new_child):
        if isinstance(new_child, GraphNode) or new_child == None:
            self._child_left = new_child
        else:
            raise Exception("Error: Attempted to put non-GraphNode object as left child")

    def get_left(self):
        return self._child_left

    ## Class attributes
    # When going through a path for the first time, the child nodes represent those on the other side.
    # a value of None means the child doesn't exists, GraphNode object means it has already been explored.
    child_front = property(get_front, set_front)
    child_left = property(get_left, set_left)
    child_right = property(get_right, set_right)

    # Stores whether or not each of the child nodes have been explored yet
    explored_front = False
    explored_left = False
    explored_right = False

    # Length refers to the amount of standard units long that this node is. for example, a hall 40 cm long will have length 1.
    length = property(get_length, set_length)


def main():
    head = GraphNode(0)

    print(head.get_orientation())
    print(head.get_explored())
    print(head.get_length())
    print(head.set_explored("r"))
    sub = GraphNode(1, head)
    head.set_front(sub)
    print(head.get_front())
    print(sub.get_parent)


if __name__ == "__main__":
    main()