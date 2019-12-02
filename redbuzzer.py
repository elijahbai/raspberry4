
from gpiozero import MotionSensor, Buzzer
from time import sleep
pir = MotionSensor(17)
buz = Buzzer(21)

while True:
    pir.wait_for_motion()
    print('motion')
    buz.off()
    sleep(1)
    buz.on()
    pir.wait_for_no_motion()
    
