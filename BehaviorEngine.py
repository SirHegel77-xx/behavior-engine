from threading import *
from time import sleep 

# Base class for behavior engines
class BehaviorEngine:
    def __init__(self):
        self._behaviors = []
        self._current_behavior = None
        self._should_stop = False    
        self._thread = None    

    # Adds a behavior instance to the engine.
    def add_behavior(self, behavior):
        self._behaviors.append(behavior)

    # Returns the currently running behavior.
    def current_behavior(self):
        return self._current_behavior

    # Starts the behavior engine.
    def start(self):
        self._thread = Thread(target = self._run)
        self._thread.start()

    # Thread function
    def _run(self):
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

    # Stops the current behavior.
    def _stop_current(self):        
        if self._current_behavior != None:            
            self._current_behavior.stop()
        
    # Stops the engine and waits for the thread to exit.
    def stop(self):
        if self._thread == None:
            return
        if self._thread.is_alive():
            self._should_stop = True
            self._thread.join()
        self._thread = None
        self._should_stop = False
