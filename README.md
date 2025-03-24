# Raspberry-Pi-Shutdown-button
Bookworm

Prerequisite software:
$ sudo apt update && sudo apt install python3-gpiozero

Reboot/Shutdown button:
* Connect a momentary switch to GPIO pins 9 (or any Gnd GPIO pin) and 5
* Grab the shutdown.py script
* In terminal enter **crontab -e**
* Add **@reboot python /home/pi/shutdown.py**
* CTRL+x to exit, Y to save changes then enter to accept the filename
* Reboot the Pi

Change the last line of shutdown.py to suit
the required action (shutdown or restart).

Once powered off, pressing the button will bring the Raspberry Pi back up.

---

Credit for the code will be added as they are discovered. I did not create the intial Python scripts.
