# Connect momentary switch to GPIO3 (AKA Pin 5) and GND
# Not for Bookworm. Falling Edge removed.

import RPi.GPIO as GPIO
import os
channel=5
GPIO.setmode(GPIO.BOARD)
#Pin 11 & Gnd
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(channel, GPIO.FALLING)
os.system("sudo reboot")
#os.system("sudo poweroff")

# Add the line below to /ect/rc.local just above "exit 0"
# python ~/reboot.py & 
