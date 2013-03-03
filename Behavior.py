from threading import *
from time import sleep
from BehaviorEngine import *
import signal

# Base class for behaviors.
class Behavior:
    def __init__(self, engine):        
        self._should_stop = False;
        self._engine = engine

    # Returns the hosting behavior engine.
    def engine(self):
        return self._engine

    # Returns True if this behavior is currently running.
    def is_running(self):
        if self._thread != None:
            if self._thread.is_alive():
                return True
        return False
    
    # Returns True if this behavior should take control.
    def take_control(self):
        return False;

    # Returns True if this behavior should stop.
    def should_stop(self):
        return self._should_stop

    # Starts this behavior. A new thread is started
    # to do actual work.
    def start(self):        
        self._thread = Thread(target = self.run)
        self._thread.start()

    # Stops this behavior and waits for the thread to end.
    def stop(self):
        self._should_stop = True
	self._thread.join()
        self._thread = None	
        self._should_stop = False

    # Returns the typename of this behavior for debuggin purposes.
    def get_type_name(self):
        return self.__class__.__name__

# Implements behavior, which does nothing.
class IdleBehavior(Behavior):
    def __init__(self, engine):
        Behavior.__init__(self, engine)        
            
    # Takes control only if no other behavior is running.
    def take_control(self):
        if self.engine().current_behavior() == None:
            return True
        return False

    # Runs until requested to stop.
    def run(self):      
        while self.should_stop() == False:            
            sleep(0.1)
        


