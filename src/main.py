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
    return 

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
