#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from time import sleep

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT)      #bcm 13
GPIO.output(13,GPIO.HIGH)
sleep(5)
GPIO.output(13,GPIO.LOW)
