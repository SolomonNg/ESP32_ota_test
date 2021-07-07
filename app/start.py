from machine import Pin
import time


print('Version 2 installed using USB')

p0 = Pin(2, Pin.OUT)    # create output pin on GPIO0
while True:
    p0.on()                 # set pin to "on" (high) level
    time.sleep(1)
    p0.off()                # set pin to "off" (low) level
    time.sleep(1)
