from Behavior import *
from BlinkBehavior import *
import curses
from time import sleep
from quick2wire.gpio import pins, In

# Sample behavior implementation
class MyBehavior(BlinkBehavior):
    def __init__(self, engine):
        BlinkBehavior.__init__(self, engine, 0, 1)
        # Variables for detecting rising edges
        self._can_take_control = False
        self._can_stop = False

    # Custom implementation of takeControl method.
    # Takes control if the current behavior is idleBehavior
    # and the rising edge of input pin is detected.
    def take_control(self):
        result = False
        if isinstance(self.engine().current_behavior(), IdleBehavior):
            with pins.pin(7, direction=In) as pin:
                if pin.value == 0:
                    self._can_take_control = True #to detect rising edge
                elif self._can_take_control == True and pin.value == 1:
                    self._can_take_control = False
                    result = True
        return result

    # Custom implementation of shouldStop method.
    # Stops the behavior if rising edge of input pin is detected.
    def should_stop(self):
        result = Behavior.should_stop(self)
        if result == True: 
            return True
        with pins.pin(7, direction=In) as pin:
            if pin.value == 0:
                self._can_stop = True #to detect rising edge
            elif self._can_stop == True and pin.value == 1:
                result = True
                self._can_stop == False
        return result

# Custom behavior engine with 2 behaviors.
class MyBehaviorEngine(BehaviorEngine):
    def __init__(self):
        BehaviorEngine.__init__(self)
        self.add_behavior(MyBehavior(self))
        self.add_behavior(IdleBehavior(self))

# Initializes curses and starts the behavior engine.
def main():
    stdscr = curses.initscr()
    stdscr.keypad(1)
    curses.noecho()
    stdscr.addstr(0, 0, "Hit 'q' to quit")
    stdscr.addstr(1, 0, "Current behavior:")
    stdscr.refresh()
    stdscr.nodelay(1)    
    try:
        #Initialize and start behavior engine
        be = MyBehaviorEngine()
        be.start()
        key = ''
        b = None
        while key != ord('q'):
            key = stdscr.getch()
            #Display current behavior on screen
            if be.current_behavior() != b:
               b = be.current_behavior()
               if b == None:
                   stdscr.addstr(2, 0, "No behavior")
                   stdscr.clrtoeol()
               else:
                   stdscr.addstr(2, 0, b.get_type_name())
                   stdscr.clrtoeol()
               stdscr.refresh
    except Exception as ex:
        raise
    finally:
       curses.nocbreak()
       stdscr.keypad(0)
       curses.echo()
       curses.endwin()
    #Stop the engine
    print("Stopping engine...")
    be.stop()
        
# Entry point       
main()
