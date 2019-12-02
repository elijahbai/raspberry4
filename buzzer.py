
from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(17)
buzzer.off()    #buzzer低电压触发
sleep(2)
buzzer.on()
