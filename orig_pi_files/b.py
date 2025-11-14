#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

for i in range(2):
    
    GPIO.output(17, False); GPIO.output(27, True); GPIO.output(22, True)
    time.sleep(1)
    
    GPIO.output(17, True); GPIO.output(27, False); GPIO.output(22, True)
    time.sleep(1)
    
GPIO.cleanup()
