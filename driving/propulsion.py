# Project 3: GEARS Robot
# File: propulsion.py
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
# Communicates with motor interfacing to engage the motors in potentially more complex maneuvers. 
# Tells the motor interfacing what to do. Most driving code should at least go through here.
# Inputs: Motor Data, Caller's Data
# Outputs: Driving the Bot

from ..interfacing import motor as m 
from . import turning
import math
import time
from .. import constants as r
from . import between_walls as bw

# This loop should move the robot one unit forward while using PID to keep the robot between the walls.
def forward_with_robot(robot):
    m.set_dps(robot.bp, robot.l_motor, 0)
    m.set_dps(robot.bp, robot.r_motor, 0)

    WHEEL_RADIUS = 4.08
    DISTANCE = 40

    driveTime = ((DISTANCE / (2 * math.pi * WHEEL_RADIUS)) * 360) / robot.dps

    start_time = time.time()

    m.set_dps(robot.bp, robot.l_motor, robot.dps)
    m.set_dps(robot.bp, robot.r_motor, robot.dps)
    while time.time() - start_time <= driveTime:
        bw.pid_one_loop(robot)
        time.sleep(robot.dt)

    m.set_dps(robot.bp, robot.l_motor, 0)
    m.set_dps(robot.bp, robot.r_motor, 0)
    


# Drive the GEARS bot one maze unit forward (40 cm)
def forward(bp, left_motor_port, right_motor_port, dps):
    m.set_dps(bp, left_motor_port, 0)
    m.set_dps(bp, right_motor_port, 0)
    
    WHEEL_RADIUS = 4.08
    DISTANCE = 40
    
    driveTime = ((DISTANCE / (2 * math.pi * WHEEL_RADIUS)) * 360) / dps
    
    m.set_dps(bp, left_motor_port, dps)
    m.set_dps(bp, right_motor_port, dps)
    
    time.sleep(driveTime)
    
    m.set_dps(bp, left_motor_port, 0)
    m.set_dps(bp, right_motor_port, 0)
    
    return

def main():
    robot = r.Robot()

    try:
        forward_with_robot(robot)
    except KeyboardInterrupt:
        robot.bp.reset_all()
 

if __name__ == "__main__":
    main()
