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
import itertools

GPIO.setmode(GPIO.BOARD)
switch_1 = 36
switch_2 = 40
led1 = 11
led2 = 13
led3 = 15

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)

GPIO.setup(switch_1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(switch_2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.output(led1, GPIO.LOW)
GPIO.output(led2, GPIO.LOW)
GPIO.output(led3, GPIO.LOW)

global count
count = 0
lst = list(itertools.product([0, 1], repeat=3))
# function definition: threaded callback
def countUp(up):
    global count
    count += 1  
    print(count)
    #print(lst[1][2])
    #print(lst)
    print("up pushed")
    if count > 7:
        count = 0
        
    
    GPIO.output(led1,lst[count][0])
    GPIO.output(led2,lst[count][1])
    GPIO.output(led3,lst[count][2])
    #GPIO.remove_event_detect(switch_1)
    time.sleep(0.3)
    

    
def countDown(down):
    global count
    count -= 1
    print("Down pushed")
    print(count)
    if count < 0:
        count = 7
       
    
    GPIO.output(led1,lst[count][0])
    GPIO.output(led2,lst[count][1])
    GPIO.output(led3,lst[count][2])
    
    time.sleep(0.3)
    

    

    


# Logic that you write
def main():
    GPIO.add_event_detect(switch_1, GPIO.RISING, callback = countUp,bouncetime=500)
    GPIO.add_event_detect(switch_2, GPIO.RISING, callback = countDown,bouncetime=500)
    
    #GPIO.remove_event_detect(switch_2)
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
