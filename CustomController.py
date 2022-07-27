from pyPS4Controller.controller import Controller
from motorDrive import motorDrive, motorTurn


class ControllerConfig(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        self.velocity = 100
        self.ort_dir = 1
        self.gas = 0
        self.turn = 0
        self.motor_start = 0
        self.invert = 0

    # Drive controls
    def _on_x_press(self):
        self.gas = 1
        self.invert = 0
        #print("Pedal to the metal")

    def _on_x_release(self):
        self.gas = 0
        self.invert = 0
        self.velocity = 0
        motorDrive(self, self.ort_dir, self.velocity, self.gas, self.motor_start, self.invert)
        self.motor_start = 1
        #print("Brake!!!")
    
    def _on_triangle_press(self):
        pass
    
    def _on_triangle_release(self):
        pass
    
    def _on_circle_press(self):
        self.gas = 1
        self.invert = 1
        #print("Back to the Future")
    
    def _on_circle_release(self):
        self.gas = 0
        self.invert = 1
        self.velocity = 0
        motorDrive(self, self.ort_dir, self.velocity, self.gas, self.motor_start, self.invert)
        self.motor_start = 1
        #print("Brake!!!")
    
    def _on_square_press(self):
        pass
    
    def _on_square_release(self):
        pass

    def _on_up_arrow_press(self):
        self.ort_dir=1
        #print("Forward")
        

    def _on_down_arrow_press(self):
        self.ort_dir=2
        #print("Backward")
    
    def _on_up_down_arrow_release(self):
        self.velocity = 0
        motorDrive(self, self.ort_dir, self.velocity, self.gas, self.motor_start, self.invert)
        self.motor_start = 1
        #print ("No Direction")
    
    def _on_left_arrow_press(self):
        self.ort_dir=3
        #print("Left")

    def _on_right_arrow_press(self):
        self.ort_dir=4
        #print("Right")

    def _on_left_right_arrow_release(self):
        self.velocity = 0
        motorDrive(self, self.ort_dir, self.velocity, self.gas, self.motor_start, self.invert)
        self.motor_start = 1
        #print ("No Direction")

    def _on_L1_press(self):
        self.turn = 1
        #print ("Turn Left")

    def _on_L1_release(self):
        self.velocity = 0
        motorTurn(self, self.velocity, self.gas, self.turn, self.motor_start, self.invert)
        self.motor_start = 1

    def _on_L2_press(self, value):
        self.velocity = int((float (value) / float(255) + 127)/2)
        #print("value: {0}, velocity: {1}".format(value, self.velocity))

        motorDrive(self, self.ort_dir, self.velocity, self.gas, self.motor_start, self.invert)
        
        motorTurn(self, self.velocity, self.gas, self.turn, self.motor_start, self.invert)        
        self.motor_start = 1
        #print("on_L2_press: {}".format(value))

    def _on_L2_release(self):
        self.velocity = 0
        motorDrive(self, self.ort_dir, self.velocity, self.gas, self.motor_start, self.invert)
        self.motor_start = 1
    
    def _on_R1_press(self):
        self.turn = 2
        #print ("Turn Right")

    def _on_R1_release(self):
        self.velocity = 0
        motorTurn(self, self.velocity, self.gas, self.turn, self.motor_start, self.invert)
        self.motor_start = 1

    def _on_R2_press(self, value):
        self.velocity = int((float (value) / float(255) + 127)/2)
        #print("value: {0}, velocity: {1}".format(value, self.velocity))

        motorDrive(self, self.ort_dir, self.velocity, self.gas, self.motor_start, self.invert)
        self.motor_start = 1
        #print("on_R2_press: {}".format(self.velocity))

    def _on_R2_release(self):
        self.velocity = 0
        motorDrive(self, self.ort_dir, self.velocity, self.gas, self.motor_start, self.invert)
        self.motor_start = 1

    def _on_L3_up(self, value):
        print("on_L3_up: {}".format(value))

    def _on_L3_down(self, value):
        print("on_L3_down: {}".format(value))

    def _on_L3_left(self, value):
        print("on_L3_left: {}".format(value))

    def _on_L3_right(self, value):
        print("on_L3_right: {}".format(value))

    def _on_L3_y_at_rest(self):
        """L3 joystick is at rest after the joystick was moved and let go off"""
        print("on_L3_y_at_rest")

    def _on_L3_x_at_rest(self):
        """L3 joystick is at rest after the joystick was moved and let go off"""
        print("on_L3_x_at_rest")

    def _on_L3_press(self):
        """L3 joystick is clicked. This event is only detected when connecting without ds4drv"""
        print("on_L3_press")

    def _on_L3_release(self):
        """L3 joystick is released after the click. This event is only detected when connecting without ds4drv"""
        print("on_L3_release")

    def _on_R3_up(self, value):
        print("on_R3_up: {}".format(value))

    def _on_R3_down(self, value):
        print("on_R3_down: {}".format(value))

    def _on_R3_left(self, value):
        print("on_R3_left: {}".format(value))

    def _on_R3_right(self, value):
        print("on_R3_right: {}".format(value))

    def _on_R3_y_at_rest(self):
        """R3 joystick is at rest after the joystick was moved and let go off"""
        print("on_R3_y_at_rest")

    def _on_R3_x_at_rest(self):
        """R3 joystick is at rest after the joystick was moved and let go off"""
        print("on_R3_x_at_rest")

    def _on_R3_press(self):
        """R3 joystick is clicked. This event is only detected when connecting without ds4drv"""
        print("on_R3_press")

    def _on_R3_release(self):
        """R3 joystick is released after the click. This event is only detected when connecting without ds4drv"""
        print("on_R3_release")

    def _on_options_press(self):
        pass

    def _on_options_release(self):
        pass

    def _on_share_press(self):
        pass  # this event is only detected when connecting without ds4drv

    def _on_share_release(self):
        pass  # this event is only detected when connecting without ds4drv