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

def motorDrive(self, ort_dir, velocity, gas, motor_start, motor_invert):
	if motor_invert == 0:
		R_MTR = 1
		L_MTR = 0
		FWD = 0
		BWD = 1
	elif motor_invert == 1:
		R_MTR = 1
		L_MTR = 0
		FWD = 1
		BWD = 0
	else:
		print("Motor Driver direction wrong. Check configuration.", \
				file=sys.stderr)
		return

	# Single execution motor driver initialization
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

		# Motor driver enabled
		MotorF.enable()
		MotorB.enable()
		print("Motors enabled")
		time.sleep(.250) # time out required to ensure driver is enabled

	# Trottle activated to move robot
	if gas == 1:
		if ort_dir == 1: # Forward
			MotorF.set_drive(R_MTR,FWD,velocity)
			MotorF.set_drive(L_MTR,BWD,velocity)
			MotorB.set_drive(R_MTR,FWD,velocity)
			MotorB.set_drive(L_MTR,BWD,velocity)
		elif ort_dir == 2: #Backward
			MotorF.set_drive(R_MTR,BWD,velocity)
			MotorF.set_drive(L_MTR,FWD,velocity)	
			MotorB.set_drive(R_MTR,BWD,velocity)
			MotorB.set_drive(L_MTR,FWD,velocity)
		elif ort_dir == 3: #Left
			MotorF.set_drive(R_MTR,FWD,velocity)
			MotorF.set_drive(L_MTR,FWD,velocity)
			MotorB.set_drive(R_MTR,BWD,velocity)
			MotorB.set_drive(L_MTR,BWD,velocity)
		elif ort_dir == 4: # Right
			MotorF.set_drive(R_MTR,BWD,velocity)
			MotorF.set_drive(L_MTR,BWD,velocity)
			MotorB.set_drive(R_MTR,FWD,velocity)
			MotorB.set_drive(L_MTR,FWD,velocity)
		elif ort_dir == 5: # Forward-Left
			MotorF.set_drive(R_MTR,FWD,velocity)
			MotorF.set_drive(L_MTR,BWD,0)
			MotorB.set_drive(R_MTR,FWD,0)
			MotorB.set_drive(L_MTR,BWD,velocity)
		elif ort_dir == 6: # Forward-Right
			MotorF.set_drive(R_MTR,FWD,0)
			MotorF.set_drive(L_MTR,BWD,velocity)
			MotorB.set_drive(R_MTR,FWD,velocity)
			MotorB.set_drive(L_MTR,BWD,0)
		elif ort_dir == 7: # Backward-Left
			MotorF.set_drive(R_MTR,BWD,0)
			MotorF.set_drive(L_MTR,FWD,velocity)	
			MotorB.set_drive(R_MTR,BWD,velocity)
			MotorB.set_drive(L_MTR,FWD,0)
		elif ort_dir == 8: # Backward-Right
			MotorF.set_drive(R_MTR,BWD,velocity)
			MotorF.set_drive(L_MTR,FWD,0)	
			MotorB.set_drive(R_MTR,BWD,0)
			MotorB.set_drive(L_MTR,FWD,velocity)
		else:
			print("Direction not Valid. Check controller.", \
				file=sys.stderr)
			return
		#time.sleep(.250)
	else:
		MotorF.set_drive(0,0,0)
		MotorF.set_drive(1,0,0)
		MotorB.set_drive(0,0,0)
		MotorB.set_drive(1,0,0)