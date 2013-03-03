from Behavior import *
from quick2wire.gpio import pins, In, Out

# Behavior for blinking a led in an output pin.
class BlinkBehavior(Behavior):
    def __init__(self, engine, pin, frequency):
        Behavior.__init__(self, engine)
        self._sleep_delay = 1 / frequency            
        self._pin = pin

    def run(self):      
        with pins.pin(self._pin, direction=Out) as outPin:
            while self.should_stop() == False:
                outPin.value = outPin.value - 1
                sleep(self._sleep_delay)
