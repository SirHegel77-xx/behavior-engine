from Behavior import *
from quick2wire.gpio import pins, Out


class blinkBehavior(behavior):
    def __init__(self, frequency):
        behavior.__init__(self)
        self.sleepDelay = 1 / frequency            

    def takeControl(self):
        return True;

    def run(self):
        self.isRunning = True
        with pins.pin(0, direction=Out) as pin:
            while self.shouldStop == False:
                pin.value = pin.value - 1
                sleep(self.sleepDelay)
            self.isRunning = False
