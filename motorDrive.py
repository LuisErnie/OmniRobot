from __future__ import print_function
import time
import sys
import math
import qwiic_scmd

# Quad motor driver required for omni directional drive. Default address 0x5D, secondary address 0x5E.
# Power jumper in EXT-MTR required for secondary driver with no USB PD power provided, two supplys result in short due to hardware error.
MotorF = qwiic_scmd.QwiicScmd(0x5D)
MotorB = qwiic_scmd.QwiicScmd(0x5E) # Address range 0x58 to 0x61

def motorError():
	print("Ending example.")
	MotorF.disable()
	MotorB.disable()

def motorDrive(self, direcction, speed):
	R_MTR = 0
	L_MTR = 1
	FWD = 1
	BWD = 0
	
	print("Motor Ortogonal Drive Test.")

	if MotorF.connected == False and MotorB.connected == False:
		print("Motor Driver not connected. Check connections.", \
			file=sys.stderr)
		return

	MotorF.begin()
	MotorB.begin()
	print("Motors initialized.")
	time.sleep(.250)

	# Zero Motor Speeds
	MotorF.set_drive(0,0,0)
	MotorF.set_drive(1,0,0)
	MotorB.set_drive(0,0,0)
	MotorB.set_drive(1,0,0)

	# Motor driver enabled
	MotorF.enable()
	MotorB.enable()
	print("Motors enabled")
	time.sleep(.250) # time out required to ensure driver is enabled

	while True:
		if direcction == 1:
			MotorF.set_drive(R_MTR,FWD,speed)
			MotorF.set_drive(L_MTR,BWD,speed)
			MotorB.set_drive(R_MTR,FWD,speed)
			MotorB.set_drive(L_MTR,BWD,speed)
			time.sleep(.05)
		elif direcction == 2:
			MotorF.set_drive(R_MTR,FWD,speed)
			MotorF.set_drive(L_MTR,BWD,speed)
			MotorB.set_drive(R_MTR,FWD,speed)
			MotorB.set_drive(L_MTR,BWD,speed)
			time.sleep(.05)
		elif direcction == 3:
			MotorF.set_drive(R_MTR,FWD,speed)
			MotorF.set_drive(L_MTR,BWD,speed)
			MotorB.set_drive(R_MTR,FWD,speed)
			MotorB.set_drive(L_MTR,BWD,speed)
			time.sleep(.05)
		elif direcction == 4:
			MotorF.set_drive(R_MTR,FWD,speed)
			MotorF.set_drive(L_MTR,BWD,speed)
			MotorB.set_drive(R_MTR,FWD,speed)
			MotorB.set_drive(L_MTR,BWD,speed)
			time.sleep(.05)
		else:
			print("Direction not Valid. Check controller.", \
				file=sys.stderr)
			return