""" EE 250L Lab 02: GrovePi Sensors

Name: Drew Ruderman

Repository: git@github.com:usc-ee250-fall2019/GrovePi-EE250.git

"""

"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi
from grove_rgb_lcd import * # imports all LCD stuff

"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
if __name__ == '__main__':

    rangefinder_port = 4    # D4 - Rangefinder in digital port
    potentiometer_port = 0   # A0 - Potentiometer in analog port
    # LCD connected to I2C, no need to set this
    setRBG(0, 255, 0) # set LCD to blue initially

    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        time.sleep(0.2)
        
        threshold = grovepi.analogRead(potentiometer_port) # read the potentiometer's value and set it to threshold
        distance = grovepi.digitalRead(rangefinder_port) # read the rangefinder's value and set it to distance

        if (distance < threshold): # only display error if rangefinder is less than the threshold
            obj_error = "OBJ PRES" # output error that object is in the way
            set RBG(255, 0, 0) # set LCD to red to say there is an error
        else:
            obj_error = "        " # clear obj pres if no object in the way
            set RBG(0, 0, 255) # set LCD to green for a good reading

        setText_norefresh(str(threshold) + "cm " + obj_error + "\n" + str(distance) + "cm") # output threshold and error message (if needed) on first line and distance on second line