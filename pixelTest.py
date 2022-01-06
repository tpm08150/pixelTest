import time
import board
import neopixel
import RPi.GPIO as GPIO
from pynput import keyboard


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
    np[i] = (0, 255, 255)
    np.show()
end = time.time()
print(end-start)

def on_press(key):
    charKeys = ['z', 'x']
    x = 0
    try:
            
        if key.char == charKeys[0]:
            r += 1
        if key.char == charKeys[1]:
            r -= 1
            
        for i in range(50):
            np[i] = (r, 0, 0)
            np.show()
end = time.time()
            
    except:
        pass
    

def on_release(key):
    global oct

    if key == keyboard.Key.esc:
        # Stop listener
        return False
    if key == keyboard.Key.up:
        pass
    if key == keyboard.Key.down:
        pass
    if key == keyboard.Key.space:
        pass
        

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()