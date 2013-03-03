import threading
from time import sleep
from BehaviorEngine import *
import signal

class behavior(threading.Thread):
    def __init__(self, engine):
        threading.Thread.__init__(self)
        self.shouldStop = False;
        self.isRunning = False;
        self.engine = engine
        
    def takeControl(self):
        return False;

    def startWork(self):
        print(self.typeName() + " starting work")        
        self.start()        
        
    def stopWork(self):
        self.shouldStop = True

    def typeName(self):
        return self.__class__.__name__


class idleBehavior(behavior):
    def __init__(self, engine):
        behavior.__init__(self, engine)        
            
    def takeControl(self):
        return True;

    def run(self):
        self.isRunning = True
        print("Starting to idle...")
        while self.shouldStop == False:            
            sleep(self.sleepDelay)
        self.isRunning = False        
        


