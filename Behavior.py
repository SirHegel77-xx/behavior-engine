from threading import *
from time import sleep
from BehaviorEngine import *
import signal

class behavior:
    def __init__(self, engine):        
        self.shouldStop = False;
        self.engine = engine

    def isRunning(self):
        if self.thread != None:
            if self.thread.is_alive():
                return True
        return False
        
    def takeControl(self):
        return False;

    def startWork(self):
        print(self.typeName() + " starting work")        
        self.thread = Thread(target = self.run)
        self.thread.start()

    def stopWork(self):
        self.shouldStop = True
	self.thread.join()
        self.thread = None	
        self.shouldStop = False

    def typeName(self):
        return self.__class__.__name__


class idleBehavior(behavior):
    def __init__(self, engine):
        behavior.__init__(self, engine)        
            
    def takeControl(self):
        if self.engine.currentBehavior == None:
            return True
        return False

    def run(self):
        print("Starting to idle...")
        while self.shouldStop == False:            
            sleep(0.1)
        


