# -*- coding: utf-8 -*-
"""
Created on Mon Mar  06:32:24 2019
@author: Ghiordy F. Contreras
"""

import RPi.GPIO as GPIO
import time
import numpy as np

#rebote = 0.3

def configurar(entrada,pare,salida):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(entrada,GPIO.IN)
    GPIO.setup(pare,GPIO.IN)
    GPIO.setup(salida,GPIO.OUT)
    #estados = [0,1,2,3]
    estado = 0
    return estado

def leer(pin):
    return GPIO.input(pin)

def decoSalida(estado,salida):
    if estado == 0:
        GPIO.output(salida,0)
    if estado == 1:
        GPIO.output(salida,1)
    return estado == 1

def decoEstado(entrada,estado,rebote):
    i = leer(entrada)
    time.sleep(rebote)
    if estado == 0:
        if i:
            estado = 1
        else:
            estado = 0
    if estado == 1:
        if i:
            estado = 0
        else:
            estado = 1
    return estado

def main(entrada,salida,rebote,pare):
    print('Instante: ',time.strftime("%c"))
    estado = configurar(entrada,pare,salida)
    aciertos = 0
    while(leer(pare) != 0):
        print('ESTADO: S',estado)
        so = decoSalida(estado,salida)
        if so:
            print('Secuencia detectada',so)
            aciertos =+1
        else:
            print('Por favor ingrese 101',so)
        estado = decoEstado(entrada,estado,rebote)
    print('Se han logrado ',aciertos,' detecciones')
    return aciertos

main(2,3,0.4,4)
    
