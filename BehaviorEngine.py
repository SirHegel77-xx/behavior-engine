from threading import *
from time import sleep 

class BehaviorEngine:
    """ Base class for behavior engines. """
    def __init__(self):
        self._behaviors = []
        self._current_behavior = None
        self._should_stop = False    
        self._thread = None    

    def add_behavior(self, behavior):
        """ Adds a behavior instance to the engine. """
        self._behaviors.append(behavior)

    def current_behavior(self):
        """ Returns the currently running behavior. """
        return self._current_behavior

    def start(self):
        """ Starts the behavior engine. """
        self._thread = Thread(target = self._run)
        self._thread.start()

    def _run(self):
        """ Thread function. """
        while self._should_stop == False:
            if self._current_behavior != None:
                if self._current_behavior.is_running() == False:
                    self._current_behavior = None
            for b in self._behaviors:
                if self._current_behavior != b:
                    if b.take_control():
                        self._stop_current()
                        self._current_behavior = b                        
                        b.start()
                        break
        self._stop_current()

    def _stop_current(self):        
        """ Stops the current behavior. """
        if self._current_behavior != None:            
            self._current_behavior.stop()

    def stop(self):
        """ Stops the engine and waits for the thread to exit. """
        if self._thread == None:
            return
        if self._thread.is_alive():
            self._should_stop = True
            self._thread.join()
        self._thread = None
        self._should_stop = False
