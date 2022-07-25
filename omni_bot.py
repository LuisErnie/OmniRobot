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

if __name__ == '__main__':
	try:
		controller.listen()
	except (KeyboardInterrupt, SystemExit) as exErr:
		motorError()
		sys.exit(0)