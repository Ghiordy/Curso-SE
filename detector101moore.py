# -*- coding: utf-8 -*-
"""
Created on Mon Mar  21:40:24 2019
@author: Ghiordy F. Contreras
"""

import RPi.GPIO as GPIO
import time
import numpy as np

rebote = 0.3

def setup(entrada,salida,habilita):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(entrada,GPIO.IN)
    GPIO.setup(habilita,GPIO.IN)
    GPIO.setup(salida,GPIO.OUT)
    estados = [0,1,2,3]
    estado = 0
    return estado

def leer(entrada,rebote):
    return GPIO.input(entrada)

def decoSalida(estado,salida):
    if estado == 0:
        GPIO.output(salida,0)
    if estado == 1:
        GPIO.output(salida,0)
    if estado == 2:
        GPIO.output(salida,0)
    if estado == 3:
        GPIO.outpu(salida,1)
    return estado == 3

def decoEstado(habilita,entrada,estado,salida):
    s = leer(habilita)
    print('senal: ',s,' tipo ',type(s))
    i == leer(entrada)
    print('entrada: ',i,' tipo ',type(i))
    time.sleep(rebote)
    if senal:
        if estado == 0 and i
    return False
