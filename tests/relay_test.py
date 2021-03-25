import RPi.GPIO as IO
import time

IO.setmode(IO.BOARD)
IO.setup(19, IO.OUT)
IO.setup(21, IO.OUT)


def main():
  IO.output(19, IO.HIGH) 
  IO.output(21, IO.HIGH)
  time.sleep(1)

  while True:
      IO.output(21, IO.HIGH)
      IO.output(19, IO.LOW) 
      time.sleep(10)

      IO.output(21, IO.LOW)
      time.sleep(10)



if __name__ == "__main__":
  main()
