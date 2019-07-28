#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Zubayr
Student Number: ISMMOG007
Prac: 1
Date: 28/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
switch_1 = 36
switch_2 = 38
led1 = 11
led2 = 13
led3 = 15

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)

GPIO.setup(switch_1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(switch_2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

global onoff
onoff = 0
# function definition: threaded callback
def callback1(channel):
    global onoff
    if  onoff == 0:
        GPIO.output(led1, GPIO.HIGH)
        onoff = 1
    else:
        GPIO.output(led1, GPIO.LOW)
        onoff = 0
def callback2(channel):
    print("Switch 2")


# Logic that you write
def main():
    GPIO.add_event_detect(switch_1, GPIO.RISING, callback = callback1,bouncetime=200)
    GPIO.add_event_detect(switch_2, GPIO.RISING, callback = callback2,bouncetime=200)
    while(1):
        x=1


    print("write your logic here")
# Under a falling-edge detection, regardless of current execution
# callback function will be called


# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
