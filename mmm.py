from gpiozero import LED, buttom
from signal import pause

led = LED(18)
lights = TrafficLights(2, 3, 4)
lights.on()
lights.off()
lights.blink()
lights.green.on()
lights.red.on(
    