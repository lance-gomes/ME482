import RPi.GPIO as IO
from adafruit_servokit import ServoKit
import time


# Pin Layout #
#    1 2     #
#    3 4     #
#    5 6     #
#    7 8     #
#    9 10    #
#   11 12    #
#   13 14    #
#   15 16    #
#   17 18    #
#   19 20    #
#   21 22    #
#   23 24    #
#   25 26    #
#   27 28    #
#   29 30    #
# Pin Layout #

# Pin Setup
IO.setmode(IO.BOARD)
IO.setup(11,IO.IN)
IO.setup(13,IO.IN)
IO.setup(15,IO.IN)

def main():
    #Initilize

    COLD_VALVE_SERVO = 0
    HOT_VALVE_SERVO = 1
    kit = ServoKit(channels=16)

    # ensure water valves are off, soap line off and water directed towards fauct 
    set_cold_valve_angle(0)
    set_hot_valve_angle(0)
    three_way(False)
    two_way(False)

    isOffState = True 

    while True:
        # IO.input(x) returns true if path is clear

        # either IR sensor detects a hand, run hand washer
        while not IO.input(11) or not IO.input(13):
            isOffState=False
            # direct 3-way valve to hand wash line
            three_way(True)
            print("directed towards hand washer")

            # turn on water
            # run for a bit to get hands wet
            water_on()
            print("first rinse")
            time.sleep(2)

            # apply soap cycle 
            soap()

            # final rinse
            print("final rinse")
            time.sleep(5)

        # run regular faucet - our setup only allows one or the other so we can just to elif here 
        while not IO.input(15):
            isOffState=False
            print("Sensor 3 active")
            three_way(False)
            water_on(True)
        
        if isOffState == False:
            # turn on the stuff
            # cut water
            water(False)

            isOffState = True 

def set_cold_valve_angle(degrees):
  kit.servo[COLD_VALVE_SERVO].angle = degrees

def set_hot_valve_angle(degrees):
  kit.servo[HOT_VALVE_SERVO].angle = degrees

def water_on(bool):
    # CONFIRM ANGLES
    if bool: # confirm that these don't keep turning they stop at 90 degree 
        set_cold_valve_angle(90)
        set_hot_valve_angle(90)
    else:
        set_cold_valve_angle(0)
        set_hot_valve_angle(0)

# Direct to the either soap line or regular line 
def three_way(bool):
    if bool:
        # direct flow to hand washer
    else:
        # direct flow to main

# Turn on and off the system  
def two_way(bool):
    if bool:
        # open 2-way
    else:
        #close 2-way

# Soap Cycle
def soap():
    pump(True)
    print("soap cycle")
    two_way(False)

# Turn on and off pump 
def pump():
    return x

if __name__ == "__main__":
    main()
