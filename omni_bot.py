#!/usr/bin/env python3
#---------------------------------------------------------------------------------
# Remote control of omnidirectional robot using PS4 controller
#---------------------------------------------------------------------------------
#
# Written by Luis Erneto Fernandez
# Universidad Autónoma de Querétaro, July 2022
# 
# This code relys in the qwiic and the ps4drv python libraries for using the Auto
# Phat from Sparkfun.
#
# More information on qwiic is at https://www.sparkfun.com/qwiic
# sudo pip3 install sparkfun-qwiic
# sudo pip3 install --upgrade sparkfun-qwiic-scmd
#
# More information on ps4drv is at https://github.com/ArturSpirin/pyPS4Controller
# sudo pip install pyPS4Controller
#
#================================================================================


from pyPS4Controller.controller import Controller

from CustomController import ControllerConfig

# from __future__ import print_function
import time
import sys
import math
import qwiic_scmd

# Initialization of the motor driver
myMotorF = qwiic_scmd.QwiicScmd(0x5D)
myMotorB = qwiic_scmd.QwiicScmd(0x5E)

R_MTR = 0
L_MTR = 1
FWD = 1
BWD = 0

ON_Motor = 0


controller = ControllerConfig(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60)


"""
def drive():
	print("Motor Test.")
	R_MTR = 0
	L_MTR = 1
	FWD = 0
	BWD = 1

	if myMotorF.connected == False and myMotorB.connected == False:
		print("Motor Driver not connected. Check connections.", \
			file=sys.stderr)
		return
	myMotorF.begin()
	myMotorB.begin()
	print("Motors initialized.")
	time.sleep(.250)

	# Zero Motor Speeds
	myMotorF.set_drive(0,0,0)
	myMotorF.set_drive(1,0,0)
	myMotorB.set_drive(0,0,0)
	myMotorB.set_drive(1,0,0)

	myMotorF.enable()
	myMotorB.enable()
	print("Motors enabled")
	time.sleep(.250)


	while True:
		speed = 20
		for speed in range(20,255):
			print(speed)
			myMotorF.set_drive(R_MTR,FWD,speed)
			myMotorF.set_drive(L_MTR,BWD,speed)
			myMotorB.set_drive(R_MTR,FWD,speed)
			myMotorB.set_drive(L_MTR,BWD,speed)
			time.sleep(.05)
		for speed in range(254,20, -1):
			print(speed)
			myMotorF.set_drive(R_MTR,FWD,speed)
			myMotorF.set_drive(L_MTR,BWD,speed)
			myMotorB.set_drive(R_MTR,FWD,speed)
			myMotorB.set_drive(L_MTR,FWD,speed)
			time.sleep(.05)

if __name__ == '__main__':
	try:
		runExample()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("Ending example.")
		myMotorF.disable()
		myMotorB.disable()
		sys.exit(0)

"""