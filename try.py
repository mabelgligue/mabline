from gpiozero import LED
from time import sleep

 led = LED(18)

 led.on(1)
 sleep(5)
 led.off()
    