import RPi.GPIO as IO

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
  
  sensor_1_old = False
  sensor_2_old = False
  sensor_3_old = False

  while True:
    # IO.input(x) returns true if path is clear
    # Set sensor_x to true if path is blocked
    sensor_1 = not IO.input(11)
    sensor_2 = not IO.input(13)
    sensor_3 = not IO.input(15)

    if sensor_1 != sensor_1_old:
        if sensor_1:
            print("Sensor 1 activated")
        else:
            print("Sensor 1 deactivated")

    if sensor_2 != sensor_2_old:
        if sensor_2:
            print("Sensor 2 activated")
        else:
            print("Sensor 2 deactivated")

    if sensor_3 != sensor_3_old:
        if sensor_3:
            print("Sensor 3 activated")
        else:
            print("Sensor 3 deactivated")

    sensor_1_old = sensor_1
    sensor_2_old = sensor_2
    sensor_3_old = sensor_3


if __name__ == "__main__":
  main()


