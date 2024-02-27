from time import sleep
from threading import Thread
MAXCHANNEL = 16


class HardwareManager(Thread):
    def __init__(self):
        print("start manager")
        self.channels = [ServoChannel(x) for x in range(0,MAXCHANNEL)]
    
    def run(self):
        while True:
            sleep(1)
            # 


    def setchannel(self,value):
        c,p,s = value
        self.channels[c].move(p,s)

    def setchannels(self,values):
        for value in values:
            self.setchannel(value)
    def printstate(self):
        for channel in self.channels:
            print(channel)

    def update(self):
        for channel in self.channels:
            channel.step()


class ServoChannel:
    def __init__(self, channel):
        self.channel  =channel
        self.posistion = 0
        self.target = 0
        self.stepsize = 0
    
    def move(self, target, stepsize):
        self.target = target
        self.stepsize = stepsize
    
    def __str__(self) -> str:
        return f"{self.channel}:{self.posistion}->{self.target}, ({self.stepsize}, {abs(self.target - self.posistion)})"

    def check(self):
        return True if(abs(self.target - self.posistion)) else False
    
    def step(self):
        if(abs(self.target - self.posistion) > self.stepsize):
            self.posistion += self.stepsize if (self.posistion < self.target) else -self.stepsize
        elif (abs(self.target - self.posistion) <= self.stepsize):
            self.posistion = self.target

if __name__ == "__main__":
    manager = HardwareManager()
