# -*- coding: utf-8 -*-
"""
Created on Mon Mar  21:40:24 2019
@author: Ghiordy F. Contreras
"""

import RPi.GPIO as GPIO
import time
import numpy as np

#rebote = 0.3

def configurar(entrada,salida,pare,habilita):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(entrada,GPIO.IN)
    GPIO.setup(habilita,GPIO.IN)
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
        GPIO.output(salida,0)
    if estado == 2:
        GPIO.output(salida,0)
    if estado == 3:
        GPIO.outpu(salida,1)
    return estado == 3

def decoEstado(habilita,entrada,estado,rebote):
    s = leer(habilita)
    i = leer(entrada)
    time.sleep(rebote)
    if s:
        if estado == 0 and i:
            estado = 1
        if estado == 1 and not(i):
            estado = 2
        elif estado == 1 and i:
            estado = 1
        if estado == 2 and i:
            estado = 3
        elif estado == 2 and not(i):
            estado = 1
        if estado == 3 and not(i):
            estado = 2
        elif estado == 3 and i:
            estado = 1
    return estado

def main(entrada,habilita,salida,rebote,pare):
    print('Instante: ',time.strftime("%c"))
    estado = configurar(entrada,salida,pare,habilita)
    aciertos = 0
    while(leer(pare) != 1):
        estado = decoEstado(habilita,entrada,
                            estado,rebote)
        print('ESTADO: S',estado)
        so = decoSalida(estado,salida)
        if so:
            print('Secuencia detectada')
            aciertos =+1
        else:
            print('Por favor ingrese 101')
    print('Se han logrado ',aciertos,' detecciones')
    return aciertos

main(2,3,4,0.3,14)
    
