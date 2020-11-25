# This script is used to manage PWT by adafruit_servokit module.
# The Write class used for string-to-servomotor's angles translation in purpose to drow lines
# Used with PWT module connected to Raspberry Pi and matched mechanical design.    

import time
from adafruit_servokit import ServoKit

t_delay=0.3
x_l = 20
y_l = 20
x_init = 180
y_init = 150


class Write():
    def __init__(self,x=8,y=15,z=0):
        self.x=x
        self.y=y
        self.z=z
        self.cox = x_init
        self.coy = y_init
        self.coz = 25
        self.kit = ServoKit(channels=16)
        self.alfabet ={
                        'א': self.alef,
                        'ב': self.bet,
                        'ג': self.gimel,
                        'ד': self.dalet,
                        'ה': self.he,
                        'ו': self.vav,
                        'ז': self.zayin,
                        'ח': self.chet,
                        'ט': self.tet,
                        'י': self.yod,
                        'כ': self.kaf,
                        'ך': self.kafend,
                        'ל': self.lamed,
                        'מ': self.mem,
                        'ם': self.memend,
                        'נ': self.nun,
                        'ו': self.nunend,
                        'ס': self.samech,
                        'ע': self.ayin,
                        'פ': self.pe,
                        'ף': self.peend,
                        'צ': self.tsade,
                        'ץ': self.tsadeend,
                        'ק': self.qof,
                        'ר': self.resh,
                        'ש': self.shin,
                        'ת': self.tav
                        }    
 
    def resetall(self):
        self.kit.servo[self.x].angle = self.cox
        self.kit.servo[self.y].angle = self.coy
        self.kit.servo[self.z].angle = self.coz 
    def resetxy(self,x,y):
        self.kit.servo[self.x].angle = x
        self.kit.servo[self.y].angle = y
        self.kit.servo[self.z].angle = self.coz + 6
    def up(self):
        self.kit.servo[self.z].angle = self.coz + 6    
    def down(self):
        self.kit.servo[self.z].angle = self.coz - 5
    def hline(self,l):        
        time.sleep(t_delay)
        self.kit.servo[self.x].angle = l
    def vline(self,h):        
        time.sleep(t_delay)
        self.kit.servo[self.y].angle = h
        
    
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
        self.resetxy(self.cox,self.coy)
        self.down()
        self.hline(self.cox - x_l)
        time.sleep(t_delay)
        # |
        self.vline(self.coy - y_l)
        time.sleep(t_delay)
        # # ->
        self.hline(self.cox)
        time.sleep(t_delay)
        self.up()
        self.resetxy(self.cox - x_l - 5,self.coy + 10)
        time.sleep(t_delay)
        self.down()
        self.vline(self.coy - y_l)
        time.sleep(t_delay)
        self.up()
        time.sleep(t_delay)
        self.cox = self.cox - x_l - 5 - 15
        time.sleep(t_delay)
        self.up()
        time.sleep(t_delay)
    def bet(self):
        print('Starting write: Bet')
        # bet
        # <-
        self.resetxy(self.cox - x_l - 2,self.coy)
        self.down()
        self.hline(self.cox)
        time.sleep(t_delay)
        # |
        self.vline(self.coy - y_l)
        time.sleep(t_delay)
        # # ->
        self.hline(self.cox - x_l - 2)
        time.sleep(t_delay)
        self.up()
        time.sleep(t_delay)
        self.resetxy(self.cox - x_l - 10,self.coy + 10)
        time.sleep(t_delay)
        self.cox = self.cox - x_l - 15
        time.sleep(t_delay)
        self.up()
        time.sleep(t_delay)
    def gimel(self):
        print('Starting write: gimel')
        # gimel
        # TBD 
    def dalet(self):
        print('Starting write: dalet')
        # dalet
        # TBD
    def he(self):
        print('Starting write: he')
        # he
        # TBD
    def vav(self):
        print('Starting write: vav')
        # vav
        # TBD
    def zayin(self):
        print('Starting write: zayin')
        # zayin
        # TBD
    def chet(self):
        print('Starting write: chet')
        # chet
        # TBD
    def tet(self):
        print('Starting write: tet')
        # tet
        # TBD
    def yod(self):
        print('Starting write: yod')
        # yod
        # TBD
    def kaf(self):
        print('Starting write: kaf')
        # kaf
        # TBD
    def kafend(self):
        print('Starting write: kafend')
        # kafend
        # TBD
    def lamed(self):
        print('Starting write: lamed')
        # lamed
        # TBD
    def mem(self):
        print('Starting write: Mem')
        # mem      
        self.resetxy(self.cox - x_l + 5,self.coy - y_l)
        self.down()
        # ->
        self.hline(self.cox)
        time.sleep(t_delay)
        # |
        self.vline(self.coy)
        time.sleep(t_delay)
        # <-
        self.hline(self.cox - x_l)
        time.sleep(t_delay)        
        self.resetxy(self.cox - x_l,self.coy + 3)
        time.sleep(t_delay)
        self.down()
        time.sleep(t_delay)
        self.vline(self.coy - y_l)
        time.sleep(t_delay)
        self.vline(self.coy + 3 )
        time.sleep(t_delay)
        self.up()
        time.sleep(t_delay)
        self.cox = self.cox - x_l - 15
        time.sleep(t_delay)
    def memend(self):
        print('Starting write: memend')
        # memend
        # TBD
    def nun(self):
        print('Starting write: nun')
        # nun
        # TBD
    def nunend(self):
        print('Starting write: nunend')
        # nunend
        # TBD
    def samech(self):
        print('Starting write: samech')
        # samech
        # TBD
    def ayin(self):
        print('Starting write: ayin')
        # ayin
        # TBD
    def pe(self):
        print('Starting write: pe')
        # pe
        # TBD
    def peend(self):
        print('Starting write: peend')
        # peend
        # TBD
    def tsade(self):
       print('Starting write: tsade')
        # tsade
        # TBD
    def tsadeend(self):
        print('Starting write: tsadeend')
        # tsadeend
        # TBD
    def qof(self):
        print('Starting write: qof')
        # qof
        # TBD 
    def resh(self):
        print('Starting write: resh')
        # resh
        # TBD
    def shin(self):
        print('Starting write: shin')
        # shin
        # TBD
    def tav(self):
        print('Starting write: tav')
        # tav
        # TBD
    def new_line(self):
        print('Starting new line')
        self.up()
        self.cox = x_init
        self.coy = self.coy - y_l - 10 - 10
        self.up()

    def word(self,wstr):
        # the function is used for 
        print('Writing word: '+ wstr)        
        for letter in wstr:
            self.alfabet[letter]()

def main(sentence):
    # init write class:
    w=Write()
    print('Start write')
    w.resetall()
    words = sentence.split(' ')
    for ws in words:
        w.word(ws)
        w.new_line()   
    print('End write')
    w.resetall()   
  
    
if __name__=='__main__':
    # This part of code is used for module debugging 
    sentence = 'אבא אמא' # example of recognized string
    main(sentence)

