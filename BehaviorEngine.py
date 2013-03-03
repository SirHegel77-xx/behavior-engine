from Behavior import *


class main:
    def main(self):
        print("Starting engine...")
        self.be = behaviorEngine()
        self.be.start()
        try:
            while True:
                sleep(1)
        except KeyboardInterrupt:
            self.be.stop()
            while self.be.isRunning == True:
                print("Waiting for the engine to stop...")
                sleep(1)
            print("Engine stopped")
            

        

m = main()
m.main()
