import RPi.GPIO as IO
import Adafruit_PCA9685
import time
from __future__ import division

# Pin Layout #
#    1 2     #
#    3 4     #
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

# Constants
SERVO_SDA_PORT = 3
SERVO_SCE_PORT = 5
SERVO_MAX = [ 600, 600 ]
SERVO_MIN = [ 150, 150 ]
SERVO_COUNT = 2

COLD_VALVE_SERVO = 0
HOT_VALVE_SERVO = 1

# State variables
is_hand_present = False
has_printed = False

pwm = Adafruit_PCA9685.PCA9685()

def set_cold_valve(opening):
  pwm.set_pwm(COLD_VALVE_SERVO, 0, opening)

def set_hot_valve(opening):
  pwm.set_pwm(HOT_VALVE_SERVO, 0, opening)

def main():
  

if __name__ == "__main__":
    main()