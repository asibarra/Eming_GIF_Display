# GPIO Pin 23 for sleep button

import RPi.GPIO as GPIO
import os
import time

# configure GPIO
GPIO.setmode(GPIO.BCM)
button_pin = 23 # GPIO Pin for the wake-up button
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def power_button(pin):
    if GPIO.input(button_pin) == GPIO.LOW: # Button is pressed
        print("Button pressed, shutting down...")
        os.system("sudo rtcwake -m standby -s 10") # Command to put the pi into sleep mode

    else: # Button is released
        print("Waking up...")
        # add any wake-up procedures here

# Setup event detection
GPIO.add_event_detect(button_pin, GPIO.BOTH, callback=power_button, bouncetime=200)

try:
    while True:
        time.sleep(1)
finally:
    GPIO.cleanup()

