b11cycle.py:

#!/usr/bin/env python2.7

from time import sleep
import subprocess
import RPi.GPIO as GPIO

CHANNEL = 17 # GPIO channel 17 is on pin 11 of connector P1
# it will work on any GPIO channel

GPIO.setmode(GPIO.BCM)
GPIO.setup(CHANNEL, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# setup the channel as input with a 50K Ohm pull up. A push button will ground the pin,
# creating a falling edge.

def system_action(CHANNEL):
    print('Button press = negative edge detected on channel %s'%CHANNEL)
    button_press_timer = 0
    while True:
            if (GPIO.input(CHANNEL) == False) : # while button is still pressed down
                button_press_timer += 1 # keep counting until button is released
            else: # button is released, figure out for how long
                if (button_press_timer > 7) : # pressed for > 7 seconds
                    print "long press > 7 : ", button_press_timer
                    # do what you need to do before halting
                    subprocess.call(['shutdown -h now "System halted by GPIO action" &'], shell=True)
                elif (button_press_timer > 2) : # press for > 2 < 7 seconds
                    print "short press > 2 < 7 : ", button_press_timer
                    # do what you need to do before a reboot
                    subprocess.call(['sudo reboot &'], shell=True)
                button_press_timer = 0
            sleep(1)

GPIO.add_event_detect(CHANNEL, GPIO.FALLING, callback=system_action, bouncetime=200)
# setup the thread, detect a falling edge on channel 17 and debounce it with 200mSec

# assume this is the main code...
try:
    while True:
        # do whatever
        # while "waiting" for falling edge on port 17
        sleep (2)

except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
GPIO.cleanup()           # clean up GPIO on normal exit
