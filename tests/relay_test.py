import RPi.GPIO as IO
import time

IO.setmode(IO.BOARD)
IO.setup(19, IO.OUT)
IO.setup(21, IO.OUT)


def main():
  while True:
      IO.output(19, IO.HIGH) 
      IO.output(21, IO.HIGH)

      time.sleep(2)

      IO.output(19, IO.LOW)
      IO.output(21, IO.LOW)

      time.sleep(2)


if __name__ == "__main__":
  main()
