import RPi.GPIO as IO
import time

IO.setmode(IO.BOARD)
IO.setup(19, IO.OUT)
IO.setup(21, IO.OUT)

def main():
  while True:
    print("Hello")
    IO.output(21, IO.HIGH)
    IO.output(19, IO.HIGH)
    time.sleep(5)


if __name__ == "__main__":
    main()