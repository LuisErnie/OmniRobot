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
from motorDrive import motorError

import sys

controller = ControllerConfig(interface="/dev/input/js0", connecting_using_ds4drv=False)


#diagonal sequences callback functions
def diagonal_ul():
	controller.ort_dir = 5
	print("Diagonal sequence detected!{0}".format(controller.ort_dir))
def diagonal_ur():
	controller.ort_dir = 6
	print("Diagonal sequence detected!{0}".format(controller.ort_dir))
def diagonal_dl():
	controller.ort_dir = 7
	print("Diagonal sequence detected!{0}".format(controller.ort_dir))
def diagonal_dr():
	controller.ort_dir = 8
	print("Diagonal sequence detected!{0}".format(controller.ort_dir))

def my_sequences():
    return [
        {"inputs": ['up','left'], "callback": diagonal_ul},
		{"inputs": ['left','up'], "callback": diagonal_ul},
		{"inputs": ['up','right'], "callback": diagonal_ur},
		{"inputs": ['right','up'], "callback": diagonal_ur},
		{"inputs": ['down','left'], "callback": diagonal_dl},
		{"inputs": ['left','down'], "callback": diagonal_dl},
		{"inputs": ['down','right'], "callback": diagonal_dr},
		{"inputs": ['right','down'], "callback": diagonal_dr}
    ]


# Remote controller execution
if __name__ == '__main__':
	try:
		controller.listen(timeout=60, on_sequence=my_sequences())

	except (KeyboardInterrupt, SystemExit) as exErr:
		motorError()
		sys.exit(0)