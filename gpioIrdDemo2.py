#!/usr/bin/python

#  Muxall Active IR Detector RPi  Example.
#
#  This sketch reads the output from the IRD
#  and lights the LED.
#
#  Flashig LED indicates weak detection and objects
#  far away.  Solid LED indicates good detection and
#  objects close up.
#
#  Depending on your application, you may need
#  to add debounce code or capacitor.
#
#  For the best performance, use 
#  "chrt --rr 99 ./gpioIrdDemo2.py" 
#  to run the script. This gives it 
#  the highest running priority in Raspbian.
#

import RPi.GPIO as GPIO		# Raspbian GPIO Library
import time					# Needed for sleep()


ttlGpio   = 19    # GPIO 19 - RPi PCB Pin 35
vsGpio    = 26    # GPIO 26 -  RPi PCB Pin 37
#gndGpio  = n/a   # RPi PCB Pin 39
ledGpio   = 27    # GPIO 27 -  RPi PCB Pin 13

#Set the pin numbering to use Broadcom's GPIO numbers.
GPIO.setmode(GPIO.BCM)

print "Powering ON the IRD...",
GPIO.setup(vsGpio, GPIO.OUT, initial=GPIO.HIGH)     # 3.3V power OUT for IRD, then turn IRD ON.
print "Done!"

GPIO.setup(ttlGpio, GPIO.IN)                        # 3.3V TTL IN from IRD output.

GPIO.setup(ledGpio, GPIO.OUT, initial=GPIO.LOW)     # LED GPIO set to output, then start with LED OFF.

# This try/except catches ctrl-C to exit the loop but not the program so we 
# can run the GPIO.cleanup routine before exiting.
try:
    while True:
        val = GPIO.input(ttlGpio)                       # Read the TTL GPIO value
        led = GPIO.input(ledGpio)                       # Read the LED GPIO value

        # If val is LOW then the IRD has a detection event.       
        if val == GPIO.LOW:
            if led == GPIO.LOW:                               
                GPIO.output(ledGpio, GPIO.HIGH)               # Light the LED when IRD triggers an event.
                print ("IRD Detector Triggered!")             # Tell someone.
		# Else, if val is HIGH then there is no detection event
        else:
            if led == GPIO.HIGH:                              # If LED is ON
                GPIO.output(ledGpio, GPIO.LOW)                # Turn OFF the LED.
                print ("End of IR Detector Event.\n")         # Tell someone.

        time.sleep(.005)                                      # 5ms sleep: Don't hog all the CPU.

except KeyboardInterrupt:                                     # Catch ctrl-C
    pass                                                      # Continue on.

print ""
print "GPIO IRD Demo script is exiting!  Cleaning up GPIO...",
GPIO.cleanup()
print "Done!"

