#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
from time import sleep
from gpiozero import MotionSensor
GPIO.setmode(GPIO.BCM)
#pir = MotionSensor(17)

GPIO.setup(4,GPIO.OUT)

from gpiozero import MotionSensor

pir = MotionSensor(17)

while True:
    pir.wait_for_motion()
    print('you moved')
    GPIO.output(4,GPIO.HIGH)
    sleep(10)
    GPIO.output(4,GPIO.LOW)
    pir.wait_for_no_motion()