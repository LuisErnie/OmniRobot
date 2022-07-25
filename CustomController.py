from pyPS4Controller.controller import Controller
from motorDrive import *


class ControllerConfig(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        self.velocity = 100

    # Drive controls
    def on_x_press(self):
        ON_Motor = 1
        print("Pedal to the metal")

    def on_x_release(self):
        ON_Motor = 0
        print("Brake!!!")
    
    def on_triangle_press(self):
        pass
    
    def on_triangle_release(self):
        pass
    
    def on_circle_press(self):
        pass
    
    def on_circle_release(self):
        pass
    
    def on_square_press(self):
        pass
    
    def on_square_release(self):
        pass

    def on_up_arrow_press(self):
        motorDrive(self, 1, self.velocity)
        print("Forward")
        

    def on_down_arrow_press(self):
        motorDrive(self, 2, self.velocity)
        print("Backward")
    
    def on_up_down_arrow_release(self):
        print ("No Direction")
    
    def on_left_arrow_press(self):
        motorDrive(self, 3, self.velocity)
        print("Left")

    def on_right_arrow_press(self):
        motorDrive(self, 4, self.velocity)
        print("Right")

    def on_left_right_arrow_release(self):
        print ("No Direction")

    def on_L1_press(self):
        pass

    def on_L1_release(self):
        pass

    def on_L2_press(self, value):
        print("on_L2_press: {}".format(value))

    def  on_L2_release(self):
        pass
    
    def on_R1_press(self):
        pass

    def on_R1_release(self):
        pass

    def on_R2_press(self, value):
        print("on_R2_press: {}".format(value))

    def on_R2_release(self):
        pass

    def on_L3_up(self, value):
        print("on_L3_up: {}".format(value))

    def on_L3_down(self, value):
        print("on_L3_down: {}".format(value))

    def on_L3_left(self, value):
        print("on_L3_left: {}".format(value))

    def on_L3_right(self, value):
        print("on_L3_right: {}".format(value))

    def on_L3_y_at_rest(self):
        """L3 joystick is at rest after the joystick was moved and let go off"""
        print("on_L3_y_at_rest")

    def on_L3_x_at_rest(self):
        """L3 joystick is at rest after the joystick was moved and let go off"""
        print("on_L3_x_at_rest")

    def on_L3_press(self):
        """L3 joystick is clicked. This event is only detected when connecting without ds4drv"""
        print("on_L3_press")

    def on_L3_release(self):
        """L3 joystick is released after the click. This event is only detected when connecting without ds4drv"""
        print("on_L3_release")

    def on_R3_up(self, value):
        print("on_R3_up: {}".format(value))

    def on_R3_down(self, value):
        print("on_R3_down: {}".format(value))

    def on_R3_left(self, value):
        print("on_R3_left: {}".format(value))

    def on_R3_right(self, value):
        print("on_R3_right: {}".format(value))

    def on_R3_y_at_rest(self):
        """R3 joystick is at rest after the joystick was moved and let go off"""
        print("on_R3_y_at_rest")

    def on_R3_x_at_rest(self):
        """R3 joystick is at rest after the joystick was moved and let go off"""
        print("on_R3_x_at_rest")

    def on_R3_press(self):
        """R3 joystick is clicked. This event is only detected when connecting without ds4drv"""
        print("on_R3_press")

    def on_R3_release(self):
        """R3 joystick is released after the click. This event is only detected when connecting without ds4drv"""
        print("on_R3_release")

    def on_options_press(self):
        pass

    def on_options_release(self):
        pass

    def on_share_press(self):
        pass  # this event is only detected when connecting without ds4drv

    def on_share_release(self):
        pass  # this event is only detected when connecting without ds4drv
