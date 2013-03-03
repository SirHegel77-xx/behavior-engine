from Behavior import *
from BlinkBehavior import *

class myBehaviorEngine(behaviorEngine):
    def __init__(self):
        behaviorEngine.__init__(self)
        self.behaviors.append(blinkBehavior(self, 1))
        self.behaviors.append(idleBehavior())

def main():
    be = myBehaviorEngine()
    try:
        print("Starting engine...")
        be.start()
        while True:
            sleep(1) 
    except KeyboardInterrupt:
        print ("Stopping engine...")
        be.stop()
        while be.isRunning:
            sleep(1)
        
main()
