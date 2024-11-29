# Raspberry-Pi-Shutdown-button
Reboot/Shutdown button:
* Connect a momentary switch to GPIO pins 9 (or any Gnd GPIO pin) and 11
* Grab the Shutdown.py script
* In terminal enter **sudo nano /etc/rc.local**
* Add **python /home/pi/Shutdown.py &** before  **exit 0** (see image example)
* CTRL+x to exit, Y to save changes then enter to accept the filename
* Reboot the Pi

Change the last line of Shutdown.py to suit
the required action

![image](https://github.com/Mraanderson/Raspberry-Pi-Shutdown-button/assets/25564127/d7672b3a-ff1c-43f5-99a6-028757580ebb)

OS versions up to Bullseye can use falling_edge
**shutdown.py**

import RPi.GPIO as GPIO
import os
channel=11
GPIO.setmode(GPIO.BOARD)
#Pin 11 & Gnd
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(channel, GPIO.FALLING)
os.system("sudo shutdown -h now")

---

Credit for the code will be added as they are discovered. I did not create the intial Python scripts.
