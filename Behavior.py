import threading
from time import sleep
import signal



class behavior(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.shouldStop = False;
        self.isRunning = False;
        
    def takeControl(self):
        return False;

    def startWork(self):
        print(self.typeName() + " starting work")        
        self.start()        
        
    def stopWork(self):
        self.shouldStop = True

    def typeName(self):
        return self.__class__.__name__


class blinkBehavior(behavior):
    def __init__(self, frequency):
        behavior.__init__(self)
        self.sleepDelay = 1 / frequency
            

    def takeControl(self):
        return True;

    def run(self):
        self.isRunning = True
        while self.shouldStop == False:
            print("Blink!")
            sleep(self.sleepDelay)
        self.isRunning = False


class behaviorEngine(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.behaviors = []
        self.behaviors.append(blinkBehavior(1))
        self.currentBehavior = None
        self.shouldStop = False
        self.isRunning = False
        
    def run(self):
        print("Starting work...")
        self.isRunning = True
        while self.shouldStop == False:
            for b in self.behaviors:
                if self.currentBehavior != b:
                    if b.takeControl():
                        self.stopCurrent()
                        self.currentBehavior = b
                        print
                        b.startWork()
        self.stopCurrent()
        self.isRunning = False

    def stopCurrent(self):        
        if self.currentBehavior != None:
            print("Stopping current behavior...")
            self.currentBehavior.stopWork()
            while self.currentBehavior.isRunning:
                sleep(0.1)
        
        
    def stop(self):
        print("Stopping work...")
        self.shouldStop = True
        


