import RPi.GPIO as GPIO
import os
channel=11
GPIO.setmode(GPIO.BOARD)
#Pin 11 & Gnd

GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(channel, GPIO.FALLING)
os.system("sudo shutdown -h now")
