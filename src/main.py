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

    while True:
        # IO.input(x) returns true if path is clear

        # either IR sensor detects a hand, run hand washer
        while not IO.input(11) or not IO.input(13):

            # direct 3-way valve to hand wash line
            three_way(True)
            print("directed towards hand washer")

            # turn on water
            # run for a bit to get hands wet
            water_on()
            print("first rinse")
            time.sleep(2)

            # open soap valve
            # cycle and then end with water
            two_way(True)
            print("first soap cycle")
            time.sleep(2)
            two_way(False)
            time.sleep(2)
            two_way(True)
            print("second soap cycle")
            time.sleep(2)
            two_way(False)

            # final rinse
            print("final rinse")
            time.sleep(5)

            # cut water
            water(False)

        # hand removed    
        else:
            print("Sensor 1 and 2 deactivated")
            # ensure everything is off
            two_way(False)
            three_way(False)
            water(False)
        
        # run regular faucet
        while not IO.input(15):
            print("Sensor 3 active")
            three_way(False)
            water_on(True)
        else:
            print("Sensor 3 deactivated")
            water_on(False)

def set_cold_valve_angle(degrees):
  kit.servo[COLD_VALVE_SERVO].angle = degrees

def set_hot_valve_angle(degrees):
  kit.servo[HOT_VALVE_SERVO].angle = degrees

def water_on(bool):
    # CONFIRM ANGLES
    if bool:
        set_cold_valve_angle(90)
        set_hot_valve_angle(90)
    else:
        set_cold_valve_angle(0)
        set_hot_valve_angle(0)

# false == main line, true == hand washer
def three_way(bool):
    if bool:
        # direct flow to hand washer
    else:
        # direct flow to main

def two_way(bool):
    if bool:
        # open 2-way
    else:
        #close 2-way


if __name__ == "__main__":
    main()
