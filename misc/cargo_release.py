# Project 3: GEARS Robot
# File: cargo_release.py
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
# If implemented, releases the cargo to the target group.
# Inputs: None
# Outputs: Cargo Released

import time
from ..interfacing import motor
from .. import constants as r

def release_cargo():
    robot = r.Robot()
    motor.set_dps(robot.bp, robot.bp.PORT_D, -300)
    motor.set_dps(robot.bp, robot.r_motor, robot.dps)
    motor.set_dps(robot.bp, robot.l_motor, robot.dps)
    time.sleep(0.5)
    motor.set_dps(robot.bp, robot.bp.PORT_D, 0)
    motor.set_dps(robot.bp, robot.r_motor, 0)
    motor.set_dps(robot.bp, robot.l_motor, 0)

def main():
    release_cargo()

if __name__ == "__main__":
    main()