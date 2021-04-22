# Project 3: GEARS Robot
# File: external_comms.py
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
# Handles all external communication to make sure target groups understand the pacifistic nature of GEARS.
# Inputs: Cargo Status?
# Outputs: External Signals

import time
import grovepi

def activate_yellow(yellow_port): 
    grovepi.pinMode(yellow_port, "OUTPUT")

    grovpei.digitalWrite(yellow_port,1)		# Send HIGH to switch on LED

def deactivate_yellow(yellow_port):
    grovpei.digitalWrite(yellow_port,0)		# Send low to switch on LED

def activate_green(green_port):
    grovepi.pinMode(green_port, "OUTPUT")

    grovepi.digitalWrite(green_port, 1)

def deactivate_green(green_port):
    grovepi.digitalWrite(green_port, 0)

def greenLed(digitalPort): #green led blink input digital port it will be plugged into
    grovpei.pinMode(digitalPort,"OUTPUT")
    time.sleep(1)
        #Blink the LED
    grovpei.digitalWrite(digitalPort,1)		# Send HIGH to switch on LED
    time.sleep(1)

    grovpei.digitalWrite(digitalPort,0)		# Send LOW to switch off LED
    time.sleep(1)


def yellowLed(digitalPort): #yellow led blink input digital port it will be plugged into
    grovpei.pinMode(digitalPort,"OUTPUT")
    time.sleep(1)
        #Blink the LED
    grovpei.digitalWrite(digitalPort,1)		# Send HIGH to switch on LED
    time.sleep(1)

    grovpei.digitalWrite(digitalPort,0)		# Send LOW to switch off LED
    time.sleep(1)
