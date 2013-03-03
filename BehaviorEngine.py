class behaviorEngine(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.behaviors = []
        self.currentBehavior = None
        self.shouldStop = False
        self.isRunning = False
        
    def run(self):
        print("Starting work...")
        self.isRunning = True
        while self.shouldStop == False:
            if self.currentBehavior.isWorking == False:
                self.currentBehavior = None
            for b in self.behaviors:
                if self.currentBehavior != b:
                    if b.takeControl():
                        self.stopCurrent()
                        self.currentBehavior = b                        
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