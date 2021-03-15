import RPi.GPIO as IO
import time

class Encoder(object):
    """
    Encoder class allows to work with rotary encoder
    which connected via two pin A and B.
    """
    def __init__(self, A, B):
        IO.setmode(IO.BCM)
        IO.setup(A, IO.IN)
        IO.setup(B, IO.IN)
        self.A = A
        self.B = B
        self.pos = 0
        self.state = 0
        if IO.input(A):
            self.state |= 1
        if IO.input(B):
            self.state |= 2
        IO.add_event_detect(A, IO.BOTH, callback=self.__update)
        IO.add_event_detect(B, IO.BOTH, callback=self.__update)

    """
    update() calling every time when value on A or B pins changes.
    It updates the current position based on previous and current states
    of the rotary encoder.
    """
    def __update(self, channel):
        state = self.state & 3
        if IO.input(self.A):
            state |= 4
        if IO.input(self.B):
            state |= 8

        self.state = state >> 2

        if state == 1 or state == 7 or state == 8 or state == 14:
            self.pos += 1
        elif state == 2 or state == 4 or state == 11 or state == 13:
            self.pos -= 1
        elif state == 3 or state == 12:
            self.pos += 2
        elif state == 6 or state == 9:
            self.pos -= 2


    """
    read() simply returns the current position of the rotary encoder.
    """
    def read(self):
        return self.pos


def main():
  enc = Encoder(21, 20)
  while True:
      time.sleep(0.25)
      print(enc.read())

if __name__ == "__main__":
  main()


