from Behavior import *
from quick2wire.gpio import pins, In, Out


class blinkBehavior(behavior):
    def __init__(self, engine, frequency):
        behavior.__init__(self, engine)
        self.sleepDelay = 1 / frequency            

    def takeControl(self):
	result = False
        with pins.pin(7, direction=In) as pin:
            if pin.value == 1:
		 result = True
        return result

    def run(self):
        print("Starting to blink...")        
        inPin = pins.pin(7, direction=In)
        outPin = pins.pin(0, direction=Out)
        with inPin, outPin:
            while inPin.value == True and self.shouldStop == False:
                outPin.value = outPin.value - 1
                sleep(self.sleepDelay)
