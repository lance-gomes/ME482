import RPi.GPIO as IO
import time

IO.setmode(IO.BCM)
IO.setup(10, IO.OUT)
IO.setup(9, IO.OUT)


def main():
  while True:
      IO.output(10, IO.HIGH) 
      IO.output(9, IO.HIGH)

      time.sleep(10)

      IO.output(10, IO.LOW)
      IO.output(9, IO.LOW)

      time.sleep(10)


if __name__ == "__main__":
  main()
