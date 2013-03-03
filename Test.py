from Behavior import *
from BlinkBehavior import *
import curses

class myBehaviorEngine(behaviorEngine):
    def __init__(self):
        behaviorEngine.__init__(self)
        self.behaviors.append(blinkBehavior(self, 1))
        self.behaviors.append(idleBehavior(self))

def main():
    stdscr = curses.initscr()
    curses.cbreak()
    stdscr.keypad(1)
    stdscr.addstr(0,10,"Hit 'q' to quit")
    stdscr.refresh()

    be = myBehaviorEngine()
   
    print("Starting engine...")
    be.start()
    key = ''
    while key != ord('q'):
        key = stdscr.getch()
        stdscr.refresh()
    curses.endwin()
    print ("Stopping engine...")
    be.stop()
    while be.isRunning:
        sleep(1)
    
        
main()
