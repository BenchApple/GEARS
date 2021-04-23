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
from ..interfacing import grove_ultrasonic as ultra
from ..walls import wall_sensing as wall
from . import turning
import math
import time
from .. import constants as r
from . import between_walls as bw

# This loop should move the robot one unit forward while using PID to keep the robot between the walls.
def forward_with_robot(robot, distance):
    m.set_dps(robot.bp, robot.l_motor, 0)
    m.set_dps(robot.bp, robot.r_motor, 0)

    WHEEL_RADIUS = 4.08
    DISTANCE = distance

    driveTime = ((DISTANCE / (2 * math.pi * WHEEL_RADIUS)) * 360) / robot.dps

    start_time = time.time()
    print(start_time)

    m.set_dps(robot.bp, robot.l_motor, robot.dps)
    m.set_dps(robot.bp, robot.r_motor, robot.dps)

    # Keeps track of whether or not a wall has been dropped.
    # None means no walls have dropped, "r" means right dropped
    # "l" means left dropped.
    dropped_wall = None

    # This loop is what actually keeps the robot along the desired line.
    while time.time() - start_time <= driveTime:
        wall_status = wall.senseWalls(robot)
        print(wall_status)

        # If the front wall is too close (ie exists), stop moving.
        if wall_status[1] == 0:
            print("Front Wall Detected Abort")
            break
        # If both of the side walls have dropped, go without PID for the rest of the cell.
        elif wall_status[0] == 1 and wall_status[2] == 1:
            pass # Just do nothing because no PID
        # If just the right wall has dropped, just use the left aligned PID.
        # If the left wall has dropped, use the right aligned PID.
        elif wall_status[0] == 1 or wall_status[2] == 1:
            if dropped_wall != "r" and wall_status[0] == 1:
                print("\nRight wall dropped\n")
                dropped_wall = "r"
            elif dropped_wall != "l" and wall_status[2] == 1:
                print("\nLeft wall dropped\n")
                dropped_wall = "l"

            print("Following wall opposite of " + dropped_wall)
            bw.pid_missing_wall(robot, dropped_wall)
        # In all other cases just use the normal PID.
        else:
            if dropped_wall != None:
                dropped_wall = None
            bw.pid_one_loop(robot)

        time.sleep(robot.dt)

    # Reset the integral gain value of the robot to 0.
    robot.I = 0

    print("went far enough")
    m.set_dps(robot.bp, robot.l_motor, 0)
    m.set_dps(robot.bp, robot.r_motor, 0)

@DeprecationWarning
def forward_with_robot_old(robot, distance):
    m.set_dps(robot.bp, robot.l_motor, 0)
    m.set_dps(robot.bp, robot.r_motor, 0)

    WHEEL_RADIUS = 4.08
    DISTANCE = distance

    driveTime = ((DISTANCE / (2 * math.pi * WHEEL_RADIUS)) * 360) / robot.dps

    start_time = time.time()

    m.set_dps(robot.bp, robot.l_motor, robot.dps)
    m.set_dps(robot.bp, robot.r_motor, robot.dps)
    while time.time() - start_time <= driveTime:
        bw.pid_one_loop(robot)
        time.sleep(robot.dt)

    m.set_dps(robot.bp, robot.l_motor, 0)
    m.set_dps(robot.bp, robot.r_motor, 0)
    
def test_missing_wall(robot, side):
    m.set_dps(robot.bp, robot.l_motor, 0)
    m.set_dps(robot.bp, robot.r_motor, 0)

    WHEEL_RADIUS = 4.08
    DISTANCE = 150

    driveTime = ((DISTANCE / (2 * math.pi * WHEEL_RADIUS)) * 360) / robot.dps

    start_time = time.time()

    m.set_dps(robot.bp, robot.l_motor, robot.dps)
    m.set_dps(robot.bp, robot.r_motor, robot.dps)
    while time.time() - start_time <= driveTime:
        bw.pid_missing_wall(robot, side)
        time.sleep(robot.dt)

    m.set_dps(robot.bp, robot.l_motor, 0)
    m.set_dps(robot.bp, robot.r_motor, 0)

# Tests the PID when there are no missing walls.
def test_PID(robot):
    m.set_dps(robot.bp, robot.l_motor, 0)
    m.set_dps(robot.bp, robot.r_motor, 0)

    WHEEL_RADIUS = 4.08
    DISTANCE = 100

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
        test_missing_wall(robot, "left")
        #test_PID(robot)
        #forward_with_robot(robot, 40)
    except KeyboardInterrupt:
        robot.bp.reset_all()

    robot.bp.reset_all()

if __name__ == "__main__":
    main()
