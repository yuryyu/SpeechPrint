import time
from adafruit_servokit import ServoKit

# define axes

class write():
    def __init__(self,x=8,y=15,z=0):
        self.x=x
        self.y=y
        self.z=z
        self.kit = ServoKit(channels=16)    
    
    def resetall(self):
        self.kit.servo[self.x].angle = 180
        self.kit.servo[self.y].angle = 0
        self.kit.servo[self.z].angle = 45
    
    def up(self):
        self.kit.servo[self.z].angle = 45
    
    def down(self):
        self.kit.servo[self.z].angle = 10

    def hline(self,l=45):
        self.down()
        time.sleep(1)
        self.kit.servo[self.x].angle = l
        time.sleep(1)
        self.up() 
    
    def vline(self,h=45):
        self.down()
        time.sleep(1)
        self.kit.servo[self.y].angle = h
        time.sleep(1)
        self.up()
    
    def hhalf(self,l):
        self.up()
        self.kit.servo[self.x].angle = l+22
        
    def hquar(self,l):
        self.up()
        self.kit.servo[self.x].angle = l+11
    
    def hspace(self,l):
        self.up()
        self.kit.servo[self.x].angle = l+45
 
    def alef(self):
        print('Starting write: Alef')
        # alef
        # <-
        self.hline()
        time.sleep(1)
        # |
        self.vline()
        time.sleep(1)
        # ->
        self.hline(0)
        time.sleep(1)

    def bet(self):
        print('Starting write: Bet')
        # bet
        # <-
        self.hline()
        time.sleep(1)
        # |
        self.vline()
        time.sleep(1)
        # ->
        self.hline(0)
        time.sleep(1)
            
    def word(self,wstr):
        print('Writing word: '+wstr)
        self.alef()
        self.bet()
        self.alef()
        
#         kit.continuous_servo[8].throttle = 1
#         time.sleep(1)
#         kit.continuous_servo[8].throttle = -1
#         time.sleep(1)
#         kit.servo[1].angle = 0
#         kit.continuous_servo[8].throttle = 0

def main():
    w=write()
    print('Start write')
    w.resetall()    
    w.word('ABA')    
    print('End write')
    w.resetall()
    
    
    
if __name__=='__main__':
    main()
    
    
    
    
