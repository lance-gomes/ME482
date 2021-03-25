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
COLD_VALVE_SERVO = 12 # 0 for port 12 is closed 
HOT_VALVE_SERVO = 15 # 90 for port 15 is closed

kit = ServoKit(channels=16)

def set_cold_valve_angle(degrees):
  kit.servo[COLD_VALVE_SERVO].angle = degrees

def set_hot_valve_angle(degrees):
  kit.servo[HOT_VALVE_SERVO].angle = degrees

def main():
  IO.setup(10, IO.OUT) # two way
  IO.setup(10, IO.LOW) # two way

  while True:
    set_cold_valve_angle(0)
    set_hot_valve_angle(90)

    time.sleep(10)

    set_cold_valve_angle(90)
    set_hot_valve_angle(0)

    time.sleep(2)

if __name__ == "__main__":
  main()
