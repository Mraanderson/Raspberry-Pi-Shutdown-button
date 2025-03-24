#!/usr/bin/env python3
from gpiozero import Button
import os

#Button 3 = Pin 5+Gnd (also acts as a reset button to bring up again)

Button(3).wait_for_press()
os.system("sudo poweroff")
#os.system("sudo reboot")