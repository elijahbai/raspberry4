#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import RPi.GPIO as GPIO
import time

#每一位数码管的总阴级连接的树莓派接口
BIT0 = 16
BIT1 = 20
BIT2 = 21
BIT3 = 26

segCode = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x07, 0x7f, 0x6f]  # 0~9
pins = [23,25,13,5,22,24,19,6,16,20,21,26]#全部接口
bits = [BIT0, BIT1, BIT2, BIT3]


def print_msg():
    print('Program is running...')
    print('Please press Ctrl+C end the program...')


def digitalWriteByte(val):
    GPIO.output(23, ~val & (0x01 << 0))#GPIO.output设置某个针脚输出状态，1or0
    GPIO.output(25, ~val & (0x01 << 1))#由上往下是a\b\c\d\e\f\g\dp
    GPIO.output(13, ~val & (0x01 << 2))
    GPIO.output(5, ~val & (0x01 << 3))
    GPIO.output(22, ~val & (0x01 << 4))
    GPIO.output(24, ~val & (0x01 << 5))
    GPIO.output(19, ~val & (0x01 << 6))
    GPIO.output(6, ~val & (0x01 << 7))


def display_1():
    #GPIO.output(BIT0, GPIO.LOW)# 设置BIT0针脚为低电平（0V）
    for bit in bits:
        GPIO.output(bit, GPIO.HIGH)#设置所有BIT高电平(3.3V)
    for i in range(10):
        digitalWriteByte(segCode[i])
        time.sleep(0.5)


def display_2():
    for bit in bits:
        GPIO.output(bit, GPIO.LOW)#设置所有BITA为低电平
    '''for i in range(10):
        digitalWriteByte(segCode[i])
        time.sleep(0.5)'''

def bitkz(bit,num):
    GPIO.output(bit, GPIO.HIGH)
    digitalWriteByte(segCode[num])
    time.sleep(0.002)
    GPIO.output(bit, GPIO.LOW)

def display_3(num):
    b0 = int(num / 1 % 10)
    b1 = int(num / 10 % 10)
    b2 = int(num / 100 % 10)
    b3 = int(num / 1000 % 10)
    #print("千位：{} 百位：{} 十位：{} 个位：{}".format(b3,b2,b1,b0))
    if num < 10:
        bitkz(BIT3,b0)
    elif num >= 10 and num < 100:
        bitkz(BIT3,b0)
        bitkz(BIT2,b1)
    elif num >= 100 and num < 1000:
        bitkz(BIT3, b0)
        bitkz(BIT2, b1)
        bitkz(BIT1,b2)
    elif num >= 1000 and num < 10000:
        bitkz(BIT3, b0)
        bitkz(BIT2, b1)
        bitkz(BIT1, b2)
        bitkz(BIT0, b3)
    else:
        print('Out of range, num should be 0~9999 !')


def setup():
    GPIO.setmode(GPIO.BCM)  # 按BCM编码位置对gipo进行编号
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)  # 设置所有针脚为输出模式
        GPIO.output(pin, GPIO.HIGH)  #  设置所有针脚为高电平（3.3V）

def loop():
    while True:
        print_msg()
        display_1()
        time.sleep(1)
        display_2()
        time.sleep(1)

        tmp = int(input('Please input a num(0~9999):'))
        for i in range(500):
            display_3(tmp)
        time.sleep(1)


def destroy():  # 程序结束时，执行该功能。
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)  # 设置所有针脚为低电平（0V）
        GPIO.setup(pin, GPIO.IN)  # 设置所有插脚输入模式


if __name__ == '__main__':  # 程序从这里开始
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
#————————————————
#版权声明：本文为CSDN博主「二流君子」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
#原文链接：https://blog.csdn.net/weixin_43673399/article/details/94437423
