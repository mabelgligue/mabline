from gpiozero import LED, Button
from signal import pause

from gpiozero import LED
from time import sleep

led = LED(18)
led2 = LED(17)
led3 = LED(27)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    led.off()
    
    led2.on()
    sleep(1)
    led2.off()
    sleep(1)
    led.off()
    
    led3.on()
    sleep(1)
    led3.off()
    sleep(1)
    led.off()