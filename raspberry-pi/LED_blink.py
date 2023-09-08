import board #type:ignore
import digitalio #type:ignore
import time #imports the variable time so I can use time.sleep
import time.sleep #type:ignore
led = digitalio.DigitalInOut(board.LED) #assigning "led" to mean the LED on the bpard
led.direction = digitalio.Direction.OUTPUT #says LED is an output 
led.value = True

while True: #loop
 led.value = False #sets led to off
 time.sleep(.5) #delay
 led.value = True #led on
 time.sleep(.5)