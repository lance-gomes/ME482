import RPi.GPIO as IO
import time

def main():
    #Initilize

    IO.setmode(IO.BOARD)

    IO.setup(11,IO.IN) # sensor 1 - hand washer
    IO.setup(13,IO.IN) # sensor 2 - hand washer 
    IO.setup(15,IO.IN) # base sensor 

    IO.setup(19, IO.OUT) # two way
    IO.setup(21, IO.OUT) # three way
    IO.setup(23, IO.OUT) # pump