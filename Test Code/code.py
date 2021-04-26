import board
import digitalio
import time
from digitalio import DigitalInOut, Direction
 
led = DigitalInOut(board.D1)
led.direction = Direction.OUTPUT
 
while True:
    led.value = True
