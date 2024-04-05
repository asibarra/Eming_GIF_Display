import RPi.GPIO as GPIO
import time

# Set GPIO Mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO Pin
button_pin = 15

# Setup the GPIO pin as input with pull-up resistor
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
   print("Push the button to test...")
   count = 0
   while True:
      # check if the button is pressed
      if GPIO.input(button_pin) == GPIO.LOW:
         # Add code or actions here when the button is pressed
         count += 1
         print("Button presses: ", count)
         time.sleep(0.2) # debounce delay

except KeyboardInterrupt:
   print("Exiting...")

finally:
   # Clean up GPIO on exit
   GPIO.cleanup()
