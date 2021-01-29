import RPi.GPIO as IO

IO.setmode(IO.BCM)

# Connect GPIO to pin #5
# Connect Power to 3.3 V, GND to GND
IO.setup(3,IO.IN)

while True:
    if IO.input(3):
        print("Path Clear!")
    else:
        print("Obstacle Detected")

