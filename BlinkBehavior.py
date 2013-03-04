from Behavior import *
from quick2wire.gpio import pins, In, Out

class BlinkBehavior(Behavior):
    """ 
    Sample behavior for blinking a led in an output pin.
    Note that take_control() is not implemented, so
    this behavior does not start unless take_control is 
    implemented in an inherited class.
    """
    def __init__(self, engine, pin, frequency):
        Behavior.__init__(self, engine)
        self._sleep_delay = 1 / frequency            
        self._pin = pin

    def run(self):      
        with pins.pin(self._pin, direction=Out) as outPin:
            while self.should_stop() == False:
                outPin.value = outPin.value - 1
                sleep(self._sleep_delay)
