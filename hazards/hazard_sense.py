# Project 3: GEARS Robot
# File: hazard_sense.py
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
# Senses hazards, outputs to hazard processing.
# Inputs: IR Data
# Outputs: Magnet Data

from ..interfacing import magnet_sensor as mag
from ..interfacing import ir_sensor as ir
from . import hazard_process as h

# Tells us whether or not there is a hazard ahead of us and returns its hazard object.
def get_hazards(robot):
    return_hazard = None

    mag_direction = mag.checkMag(robot.imu_obj, robot.bp, robot.l_motor, robot.r_motor, robot.dps)

    if mag_direction != None:
        return_hazard = h.Hazard("Magnet", "uT", 400)
        dir = mag_direction
    elif ir.ir_exists(robot.ir_port):
        return_hazard = h.Hazard("Heat", "J", 3600)
        dir = None

    print("Hazard is " + str(return_hazard))

    return [return_hazard, dir]
