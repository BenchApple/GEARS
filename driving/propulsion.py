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

# This version of the function follows the heuristic that for any 40 cm move, there will be
# at msot one wall status change. This method takes advantage of that by moving until that wall status
# is changed and then moving 20 cm, or moving all 40 cm if there is no wall change
# NOTE: This could run into issues with a bad PID where it detects a wall change where there is none
# due to the robot going too far to one side of the hallway.
# This should be able to eliminate that issue due to its ability to properly eliminate an amount
# of error from the robot.
def forward_with_robot(robot, distance, going_half=False):
    m.set_dps(robot.bp, robot.l_motor, 0)
    m.set_dps(robot.bp, robot.r_motor, 0)

    WHEEL_RADIUS = 4.08
    DISTANCE = distance

    driveTime = ((DISTANCE / (2 * math.pi * WHEEL_RADIUS)) * 360) / robot.dps

    start_time = time.time()
    print(start_time)

    m.set_dps(robot.bp, robot.l_motor, robot.dps)
    m.set_dps(robot.bp, robot.r_motor, robot.dps)

    have_walls_changed = False
    orig_wall_status = wall.senseWalls(robot)
    dropped_wall = None

    # move forward either until we've moved distance or we have come to a change in the walls.
    while time.time() - start_time <= driveTime and not have_walls_changed:
        # Get the current wall status.
        cur_wall_status = wall.senseWalls(robot)

        have_walls_changed = detect_wall_change(robot, orig_wall_status, cur_wall_status)
        if have_walls_changed:
            break

        # Step the PID once
        dropped_wall = step_pid(robot, cur_wall_status, dropped_wall)

        # If there is a front wall, stop moving
        if dropped_wall == -1:
            # If we're catching a wall super early in a move foward, 
            # we want to take one length away from the current node
            if time.time() - start_time <= (driveTime / 4) and not robot.is_backtracking:
                robot.cur_node.set_length(robot.cur_node.get_length() - 1)
            break

    # If we have detected a wall change, enter this.
    if have_walls_changed and not going_half:
        print("\nEntering Second Phase\n")
        '''
        m.set_dps(robot.bp, robot.l_motor, 0)
        m.set_dps(robot.bp, robot.r_motor, 0)
        input("press a button to conitune")
        m.set_dps(robot.bp, robot.l_motor, robot.dps)
        m.set_dps(robot.bp, robot.r_motor, robot.dps)
        '''
        # This recursive call style should work in theory, but there's no guarentee it will for sure
        # This needs to be tested for sure so we can be sure of it actually working.
        # NOTE In the case where this is a lot of error, there is a chance that normal PID operation
        # will result in the loss of a wall. While our normal stuff can handle that will good accuracy
        # this solution has the chance to completely throw off everything.
        forward_with_robot(robot, robot.HALF_DIST, going_half=True)


# Steps the PID once
# Returns the current dropped wall,  -1 if we need to stop moving forward.
def step_pid(robot, wall_status, dropped_wall):
    # If the front wall is too close, stop
    if wall_status[1] == 0:
        print("Front Wall Detected. Stopping.")
        return -1
    # If both of the side walls have dropped, go without PID for the rest of the cell.
    elif wall_status[0] == 1 and wall_status[2] == 1:
        pass # Just do nothing because no PID
    # If just the right wall has dropped, just use the left aligned PID.
    # If the left wall has dropped, use the right aligned PID.
    # All of this stays here just so that we can keep the alignment PIDs working.
    elif wall_status[0] == 1 or wall_status[2] == 1:
        if wall_status[0] == 1 and dropped_wall != "r":
            print("\nRight wall dropped\n")
            dropped_wall = "r"
        elif wall_status[2] == 1 and dropped_wall != "l":
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
    return dropped_wall

# Returns whether or not the wall status has changed taking a new reading of the walls.
# A true return means the walls have changed.
def detect_wall_change(robot, orig_walls, cur_walls):
    print(orig_walls)
    print(cur_walls)
    # Check to see if any of the wall statuses are different from before.
    if cur_walls[0] != orig_walls[0] or cur_walls[1] != orig_walls[1] or cur_walls[2] != orig_walls[2]:
        return True
    return False

# This loop should move the robot one unit forward while using PID to keep the robot between the walls.
@DeprecationWarning
def forward_with_robot_2(robot, distance):
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
