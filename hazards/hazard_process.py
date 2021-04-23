# Project 3: GEARS Robot
# File: hazard_process.py
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
# Determines where and of what type the given hazard is. Turns into usable data for the final hazard outputting.
# Inputs: Global Location, Hazard Data
# Outputs: Hazard Location and Type

# This class stores the information for the hazards.
class Hazard:
    # Initialize the Hazard Object
    def __init__(self, _type, _parameter, _value):
        self.type = _type

        self.parameter = _parameter

        self.value = _value

        self.x_coord = -1
        self.y_coord = -1

    def __str__(self):
        return "%s, %s, %s, %d cm, %d cm" % (self.type, self.parameter, self.value, self.x_coord, self.y_coord)

    def set_x_coord(self, newx):
        self.x_coord = newx

    def set_y_coord(self, newy):
        self.y_coord = newy

def main():
    h = Hazard("Your Mom", "Kilograms (kg)", 400)
    print(h)
    h.set_x_coord(500)
    h.set_y_coord(600)
    print(h)

if __name__ == "__main__":
    main()