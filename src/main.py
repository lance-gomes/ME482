import RPi.GPIO as IO
import time

# Pin Setup
IO.setmode(IO.BCM) # Remove after we import servo_kit

IO.setup(17,IO.IN) # sensor 1 - hand washer
IO.setup(27,IO.IN) # sensor 2 - hand washer 
IO.setup(22,IO.IN) # base sensor 

IO.setup(10, IO.OUT) # two way
IO.setup(9, IO.OUT) # three way

def main():
    #Initilize
    three_way(False)
    water(False)

    isOffState = True 

    while True:
        # IO.input(x) returns true if path is clear

        # either IR sensor detects a hand, run hand washer
        while IO.input(17) == 0 or IO.input(27) == 0:
            isOffState=False
            # direct 3-way valve to hand wash line
            three_way(False)
            time.sleep(6) # we need to wait 6 sec until the 3way turns NOOOO
            print("directed towards hand washer")

            # turn on water
            # run for a bit to get hands wet
            water(True)
            print("first rinse")
            time.sleep(2)

            # apply soap cycle 
            soap()

            # final rinse
            print("final rinse")
            time.sleep(5)

        # run regular faucet - our setup only allows one or the other so we can just to elif here 
        while IO.input(22) == 0:
            isOffState=False
            print("Sensor 3 active /n")
            three_way(True)
            time.sleep(6) # we need to wait 6 sec until the 3way turns NOOOO
            water(True)
            time.sleep(3) #sensor buggy just make it wait 3 seconds 
        
        if isOffState == False:
            # cut water
            water(False)
            isOffState = True 

# Two way controls the water on and off 
def water(input):
    # CONFIRM ANGLES
    if not input: # confirm that these don't keep turning they stop at 90 degree 
        IO.output(10, IO.HIGH)
    else:
        IO.output(10, IO.LOW)

# Direct to the either soap line or regular line 
# false -> hand washer  
# true -> main line
# time to switch is ~ 6sec
def three_way(input):
    if not input:
        # direct to the handwasher 
        IO.output(9, IO.HIGH)
    else:
        # direct flow to main
        IO.output(9, IO.LOW)

# Soap Cycle
def soap():
    pump(True)
    print("soap cycle")
    pump(False)

# Turn on and off pump 
def pump(input):
    if input:
        # turn on pump
        return
    else:
        # turn off pump 
        return  

if __name__ == "__main__":
    main()
