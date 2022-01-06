import time
import board
import neopixel
import RPi.GPIO as GPIO


LED_COUNT = 1000
LED_PIN = board.D18  # GPIO pin
LED_BRIGHTNESS = 0.1  # LED brightness
LED_ORDER = neopixel.RGB  # order of LED colours. May also be RGB, GRBW, or RGBW
# The colour selection selected for this project: red, blue, yellow, green, pink, and silver respectively


# Create NeoPixel object with appropriate configuration.
np = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)

x = 0
start = time.time()
for i in range(50):
    np[i] = (0, 0, 255)
    np.show()
end = time.time()
print(end-start)

