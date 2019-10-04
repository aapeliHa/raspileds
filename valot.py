import RPi.GPIO as GPIO
import time
import sys
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
count = 0
while True:
    y = input('1, 2 tai 3:' )
    a = int(y)
    if 2 == a:
        while count < 10:
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(25,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(25,GPIO.LOW)
            GPIO.output(23,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(23,GPIO.LOW)
            count += 1
    elif 1 == a:
        while count < 10:
                GPIO.output(18,GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(18,GPIO.LOW)
                GPIO.output(23,GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(23,GPIO.LOW)
                GPIO.output(25,GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(25,GPIO.LOW)
                count += 1
    elif 3 == a:
        while count < 10:
                GPIO.output(25,GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(25,GPIO.LOW)
                GPIO.output(23,GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(23,GPIO.LOW)
                GPIO.output(18,GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(18,GPIO.LOW)
                count += 1
    elif 123 == a:
        while count < 5:
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(23,GPIO.HIGH)
            GPIO.output(25,GPIO.HIGH)
            time.sleep(0.05)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(23,GPIO.LOW)
            GPIO.output(25,GPIO.LOW)
            time.sleep(0.15)
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(25,GPIO.HIGH)
            time.sleep(0.05)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(25,GPIO.LOW)
            GPIO.output(23,GPIO.HIGH)
            time.sleep(0.05)
            GPIO.output(23,GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(25,GPIO.HIGH)
            time.sleep(0.05)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(25,GPIO.LOW)
            time.sleep(0.05)
            GPIO.output(23,GPIO.HIGH)
            time.sleep(0.05)
            GPIO.output(23,GPIO.LOW)
            time.sleep(0.05)
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(25,GPIO.HIGH)
            time.sleep(0.05)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(25,GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(23,GPIO.HIGH)
            time.sleep(0.05)
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(25,GPIO.HIGH)
            GPIO.output(23,GPIO.LOW)
            time.sleep(0.05)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(25,GPIO.LOW)
            time.sleep(0.15)
            count +=1
    else:
        sys.exit(0)
    count = 0
