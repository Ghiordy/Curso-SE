# -*- coding: utf-8 -*-
"""
Created on Tue Mar  11:28:24 2019

@author: Ghiordy F. Contreras
"""

#pip install webio

#realizar un contador de 0 a 99


import RPi.GPIO as GPIO
import time 

GPIO.setwarnings(False)

pin = 21
n = 2
delay = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)

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
