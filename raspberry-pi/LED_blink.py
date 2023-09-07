import board #type:ignore
import digitalio #type:ignore
import time
import time.sleep #type:ignore
led = digitalio.DigitalInOut(board.LED) 
led.direction = digitalio.Direction.OUTPUT 
led.value = True

while True:
 led.value = False 
 time.sleep(.5)
 led.value = True
 time.sleep(.5)