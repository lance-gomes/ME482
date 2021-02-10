import RPi.GPIO as IO

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

# Pin Setup
IO.setmode(IO.BOARD)
IO.setup(5,IO.IN)

is_hand_present = False
has_printed = False

while True:

    if IO.input(5) and is_hand_present:
        is_hand_present = False
        has_printed = False
    elif not IO.input(5) and not is_hand_present:
        is_hand_present = True
        has_printed = False


    if not has_printed:
        if is_hand_present:
            print("Hand Detected!")
        else:
            print("Hand Removed!")
        print("")

        has_printed = True

