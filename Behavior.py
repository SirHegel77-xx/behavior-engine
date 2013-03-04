from threading import *
from time import sleep
from BehaviorEngine import *
import signal

class Behavior:
    """ Base class for behaviors. """
    def __init__(self, engine):        
        self._should_stop = False;
        self._engine = engine

    def engine(self):
        """ Returns the hosting behavior engine. """
        return self._engine

    def is_running(self):
        """ Returns True if this behavior is currently running. """
        if self._thread != None:
            if self._thread.is_alive():
                return True
        return False
    
    def take_control(self):
        """ 
        Returns True if this behavior should take control.
        The engine calls this method for each behavior
        to check if some of the behaviors would like to 
        take control. Inheriting classes should implement
        this method to determine when the behavior should start.
        """
        return False;

    def should_stop(self):
        """ 
        Returns True if this behavior should stop.
        The behavior implementation should call this function
        in the behavior loop and return as soon as possible
        if should_stop returns True. By default this function
        returns True if stop() method has been called. 
        Inheriting classes can override this method if some
        other logic is requred. However, _should_stop value
        should always be obeyed.
        """
        return self._should_stop

    def start(self):
        """ 
        Starts this behavior. A new thread is started
        to run the behavior code. Inheriting classes should 
        implement run() method to do actual work.
        """
        self._thread = Thread(target = self.run)
        self._thread.start()

    def stop(self):
        """  Stops this behavior and waits for the thread to end. """
        self._should_stop = True
	self._thread.join()
        self._thread = None	
        self._should_stop = False

    def get_type_name(self):
        """  Returns the typename of this behavior for debuggin purposes.  """
        return self.__class__.__name__

class IdleBehavior(Behavior):
    """  Implements behavior, which does nothing. """
    def __init__(self, engine):
        Behavior.__init__(self, engine)        
            
    def take_control(self):
        """ Takes control only if no other behavior is running. """
        if self.engine().current_behavior() == None:
            return True
        return False

    def run(self):      
        """ Runs until requested to stop. """
        while self.should_stop() == False:            
            sleep(0.1)
        


