import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN)      #光敏电阻 AD 不接，VCC 3.3V,GND,DO 接BCM 23
GPIO.setup(22,GPIO.OUT)     #LED + 接BCM22 ,GND
 
GPIO.output(22,GPIO.LOW)
for i in range(0,20):
    if GPIO.input(23)==1:
        GPIO.output(22,GPIO.HIGH)
    else:
        GPIO.output(22,GPIO.LOW)
 
    time.sleep(1)
    
    print GPIO.input(23)
