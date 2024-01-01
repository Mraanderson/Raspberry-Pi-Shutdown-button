# Raspberry-Pi-Shutdown-button
Reboot/Shutdown button:
* Connect a momentary switch to GPIO pins 9 and 11
* Grab the shutdown.py script
* In terminal enter sudo nano /etc/rc.local
* Add python /home/pi/shutdown.py & before the exit 0 text (see image example)
* CTRL+x to exit, Y to save then enter to accept the filename


![image](https://github.com/Mraanderson/Raspberry-Pi-Shutdown-button/assets/25564127/d7672b3a-ff1c-43f5-99a6-028757580ebb)


shutdown.py

import RPi.GPIO as GPIO
import os
channel=11
GPIO.setmode(GPIO.BOARD)
#Pin 11 & Gnd

GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(channel, GPIO.FALLING)
os.system("sudo shutdown -h now")
