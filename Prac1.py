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

#Setting pi pinout convention and assigning pin numbers
GPIO.setmode(GPIO.BOARD)
switch_1 = 36
switch_2 = 40
led1 = 11
led2 = 13
led3 = 15

#Setting up led pins as outputs 
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)

#Setting push button pins as inputs
GPIO.setup(switch_1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(switch_2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.output(led1, GPIO.LOW)
GPIO.output(led2, GPIO.LOW)
GPIO.output(led3, GPIO.LOW)
#creating a global variable
global count
count = 0
#Creating a list containing binary values 
lst = list(itertools.product([0, 1], repeat=3))

# function definition: threaded callback

def countUp(up):
    global count
    count += 1  
    print(count)
    print("up pushed")
    if count > 7:
        count = 0
        
#setting logic to pins     
    GPIO.output(led1,lst[count][0])
    GPIO.output(led2,lst[count][1])
    GPIO.output(led3,lst[count][2])
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
    #Creating interrupt detection
    GPIO.add_event_detect(switch_1, GPIO.RISING, callback = countUp,bouncetime=500)
    GPIO.add_event_detect(switch_2, GPIO.RISING, callback = countDown,bouncetime=500)
    
    #GPIO.remove_event_detect(switch_2)
    while(1):
        x=1

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
