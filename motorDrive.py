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

def motorDrive(self, ort_dir, velocity, gas, motor_start):
	R_MTR = 1
	L_MTR = 0
	FWD = 0
	BWD = 1

	if motor_start == 0:
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

	if gas == 1:
		# Motor driver enabled
		MotorF.enable()
		MotorB.enable()
		print("Motors enabled")
		time.sleep(.250) # time out required to ensure driver is enabled

		if ort_dir == 1:
			MotorF.set_drive(R_MTR,FWD,velocity)
			MotorF.set_drive(L_MTR,BWD,velocity)
			MotorB.set_drive(R_MTR,FWD,velocity)
			MotorB.set_drive(L_MTR,BWD,velocity)
			time.sleep(.250)
		elif ort_dir == 2:
			MotorF.set_drive(R_MTR,BWD,velocity)
			MotorF.set_drive(L_MTR,FWD,velocity)	
			MotorB.set_drive(R_MTR,BWD,velocity)
			MotorB.set_drive(L_MTR,FWD,velocity)
			time.sleep(.250)
		elif ort_dir == 3:
			MotorF.set_drive(R_MTR,FWD,velocity)
			MotorF.set_drive(L_MTR,FWD,velocity)
			MotorB.set_drive(R_MTR,BWD,velocity)
			MotorB.set_drive(L_MTR,BWD,velocity)
			time.sleep(.250)
		elif ort_dir == 4:
			MotorF.set_drive(R_MTR,BWD,velocity)
			MotorF.set_drive(L_MTR,BWD,velocity)
			MotorB.set_drive(R_MTR,FWD,velocity)
			MotorB.set_drive(L_MTR,FWD,velocity)
			time.sleep(.250)
		else:
			print("Direction not Valid. Check controller.", \
				file=sys.stderr)
			return
	else:
		MotorF.set_drive(0,0,0)
		MotorF.set_drive(1,0,0)
		MotorB.set_drive(0,0,0)
		MotorB.set_drive(1,0,0)