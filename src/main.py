import RPi.GPIO as IO
import time
import Encoder
from adafruit_servokit import ServoKit

class Encoder(object):
    """
    Encoder class allows to work with rotary encoder
    which connected via two pin A and B.
    """
    def __init__(self, A, B):
        if IO.getmode() != IO.BCM:
          IO.setmode(IO.BCM)
        IO.setup(A, IO.IN)
        IO.setup(B, IO.IN)
        self.A = A
        self.B = B
        self.pos = 0
        self.state = 0
        if IO.input(A):
            self.state |= 1
        if IO.input(B):
            self.state |= 2
        IO.add_event_detect(A, IO.BOTH, callback=self.__update)
        IO.add_event_detect(B, IO.BOTH, callback=self.__update)

    """
    update() calling every time when value on A or B pins changes.
    It updates the current position based on previous and current states
    of the rotary encoder.
    """
    def __update(self, channel):
        state = self.state & 3
        if IO.input(self.A):
            state |= 4
        if IO.input(self.B):
            state |= 8

        self.state = state >> 2

        if state == 1 or state == 7 or state == 8 or state == 14:
            self.pos += 1
        elif state == 2 or state == 4 or state == 11 or state == 13:
            self.pos -= 1
        elif state == 3 or state == 12:
            self.pos += 2
        elif state == 6 or state == 9:
            self.pos -= 2


    """
    read() simply returns the current position of the rotary encoder.
    """
    def read(self):
        return self.pos

def main():
    #Initilize
    # IO.setmode(IO.BCM)

    # IO.setup(17,IO.IN) # sensor 1 - hand washer
    # IO.setup(27,IO.IN) # sensor 2 - hand washer 
    # IO.setup(22,IO.IN) # base sensor
    # IO.setup(4, IO.IN)

    # IO.setup(10, IO.OUT) # two way
    # IO.setup(9, IO.OUT) # three way
    # IO.setup(11, IO.OUT) # pump

    # three_way(False)
    # water(True)

    isOffState = True 

    # HIGH == OFF
    # IO.output(11, IO.HIGH) # pump
    # IO.output(10, IO.HIGH) # pump
    # IO.output(9, IO.HIGH) # pump

    kit = ServoKit(channels=16)
    enc = Encoder(21, 20)
    enc_pos = enc.read()

    cold_opening = 90
    hot_opening = 0

    kit.servo[12].angle = cold_opening
    kit.servo[15].angle = hot_opening

    # no noise from the 3 way (since its normally on the hand washer)
    # 2 way click 
    # nothing happens for 3 sec

    # soap / pump turns on for 1 sec and then stops 

    # then water continues to run 
    #2 way clicks 

    while True:
        # IO.input(x) returns true if path is clear
        # print(IO.input(27) == 0)
        # either IR sensor detects a hand, run hand washer
        # print("Not in")
        # while IO.input(4) != 0:
        #     print("first rinse")
        #     print("it is in now ")
            # direct 3-way valve to hand wash line
            # three_way(False)
            # time.sleep(3) # we need to wait 6 sec until the 3way turns NOOOO
            # print("directed towards hand washer")

            # # turn on water
            # # run for a bit to get hands wet
            # water(True)
            # time.sleep(5)

            # # apply soap cycle 
            # soap()

            # # final rinse
            # print("final rinse")
            # time.sleep(5)

        # run regular faucet - our setup only allows one or the other so we can just to elif here
        # while IO.input(27) == 0:
        #     three_way(True)
        #     print("Sensor 3 active")
        #     isOffState=False
        #     # three_way(True)
        #     # time.sleep(6) # we need to wait 6 sec until the 3way turns NOOOO
        #     water(True)
        #     time.sleep(1) #sensor buggy just make it wait 3 seconds
        prev_pos = enc.read()
        print(prev_pos)
        if enc_pos != prev_pos:

            if prev_pos > enc_pos:
                cold_opening -= 2
                hot_opening += 2
            else:
                cold_opening += 2
                hot_opening -= 2

            
            if cold_opening <= 0:
                cold_opening = 0
            elif cold_opening > 90:
                cold_opening = 90

            if hot_opening <= 0:
                hot_opening = 0
            elif hot_opening > 90:
                hot_opening = 90

            kit.servo[12].angle = cold_opening
            kit.servo[15].angle = hot_opening
            enc_pos = enc.read()

        

# Two way controls the water on and off 
def water(input):
    # CONFIRM ANGLES
    if not input: # confirm that these don't keep turning they stop at 90 degree 
        IO.output(10, IO.HIGH)
    else:
        IO.output(10, IO.LOW)

# Direct to the either soap line or regular line 
# false -> hand washer  
# true -> main line
# time to switch is ~ 6sec
def three_way(input):
    if not input:
        # direct to the handwasher 
        IO.output(9, IO.HIGH)
    else:
        # direct flow to main
        IO.output(9, IO.LOW)

# Soap Cycle
def soap():
    pump(True)
    print("soap cycle")
    time.sleep(5)
    pump(False)

# Turn on and off pump 
def pump(input):
    if not input:
        IO.output(11, IO.HIGH)
    else:
        IO.output(11, IO.LOW)

def set_cold_valve_angle(kit, degrees):
  kit.servo[12].angle = degrees

def set_hot_valve_angle(kit, degrees):
  kit.servo[15].angle = degrees

if __name__ == "__main__":
    main()
