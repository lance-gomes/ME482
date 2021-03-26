import RPi.GPIO as IO
import time

IO.setmode(IO.BOARD)
IO.setup(19, IO.OUT)
IO.setup(21, IO.OUT)
IO.setup(23, IO.OUT)

def main():
  while True:
    print("Hello")
    IO.output(21, IO.LOW)
    IO.output(19, IO.LOW)
    IO.output(23, IO.HIGH)

    # time.sleep(5)

    # IO.output(23, IO.LOW)

    # time.sleep(2)

    # IO.output(23, IO.HIGH)

    # time.sleep(5)


if __name__ == "__main__":
    main()