# -*- coding: utf-8 -*-
"""
Created on Tue Mar  16:14:24 2019

@author: Ghiordy F. Contreras
"""

#pip install webio

#realizar un contador de 0 a 99


import RPi.GPIO as GPIO
import time 

GPIO.setwarnings(False)

display1 = np.array([0])
display1 = np.array([0])
numero = np.array([[1,1,1,1,1,1,0,0],  # 0
                   [0,1,1,0,0,0,0,0],  # 1
                   [1,1,0,1,1,0,1,0],  # 2
                   [1,1,1,1,0,0,1,0],  # 3
                   [0,1,1,0,0,1,1,0],  # 4
                   [1,0,1,1,0,1,1,0],  # 5
                   [0,0,1,1,1,1,1,0],  # 6
                   [1,1,1,0,0,0,0,0],  # 7
                   [1,1,1,1,1,1,1,0],  # 8
                   [1,1,1,0,0,1,1,0]]) #9

pin = 21
n = 2
delay = 2


GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)


def  setupDisplay(display1,display2):
    for i in range(len(display1)):
        GPIO.setup(display1[i],GPIO.OUT)
        GPIO.setup(display2[i],GPIO.OUT)

def encenderLed(pin,n,delay):
    print("Hello world: Ejecutado ",n,
          " veces por ",delay*n," segundos")
    while (n > 0):
        GPIO.output(pin,True)
        time.sleep(delay)
        GPIO.output(pin,False)
        time.sleep(delay)
        n = n - 1
        print("Queda ",n*delay," segundos ...")
    print("Finalizado")

encenderLed(pin,2,delay)
