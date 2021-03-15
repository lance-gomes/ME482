from adafruit_servokit import ServoKit
import RPi.GPIO as IO
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

# Constants
COLD_VALVE_SERVO = 0
HOT_VALVE_SERVO = 1

kit = ServoKit(channels=16)

def set_cold_valve_angle(degrees):
  kit.servo[COLD_VALVE_SERVO].angle = degrees

def set_hot_valve_angle(degrees):
  kit.servo[HOT_VALVE_SERVO].angle = degrees

def main():

  print(IO.getmode())

  while True:
    set_cold_valve_angle(0)
    set_hot_valve_angle(0)

    time.sleep(2)

    set_cold_valve_angle(90)
    set_hot_valve_angle(90)

    time.sleep(2)

if __name__ == "__main__":
  main()
