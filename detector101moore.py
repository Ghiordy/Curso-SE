# -*- coding: utf-8 -*-
"""
Created on Mon Mar  21:40:24 2019
@author: Ghiordy F. Contreras
"""

import RPi.GPIO as GPIO
import time
import numpy as np

# Parametros de trabajo
# pulsador0 = 2
# pulsador1 = 3
# rebote = 1
# pare = 14
# estados

def configurar(pulsador0,pulsador1,pare,salida):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pulsador0,GPIO.IN)
    GPIO.setup(pulsador1,GPIO.IN)
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
        GPIO.output(salida,1)
    return estado == 3

def decoEstado(pulsador0,pulsador1,estado,rebote,estados):
    p0 = leer(pulsador0)
    p1 = leer(pulsador1)
    time.sleep(rebote)
    if estado == estados[0]:
        if p0 == 1:
            estado = estados[0]
        elif p1 == 1:
            estado = estados[1]
    elif estado == estados[1]:
        if p0 == 1:
            estado = estados[2]
        elif p1 == 0:
            estado = estados[1]
    elif estado == estados[2]:
        if p0 == 1:
            estado = estados[0]
        elif p1 == 1:
            estado = estados[3]
    elif estado == estados[3]:
        if p0 == 1:
            estado = estados[2]
        elif p1 == 1:
            estado = estados[1]
    return estado

def main(pulsador0,pulsador1,salida,rebote,pare,estados):
    print('Instante: ',time.strftime("%c"))
    estado = configurar(pulsador0,pulsador1,pare,salida)
    aciertos = 0
    while(leer(pare) != 0):
        print('ESTADO: S',estado)
        so = decoSalida(estado,salida)
        if so:
            print('Secuencia detectada')
            aciertos =+1
        else:
            print('Por favor ingrese 101')
        estado = decoEstado(pulsador0,pulsador1,estado,rebote,estados)
    print('Se han logrado ',aciertos,' detecciones')
    return aciertos

main(2,3,4,1,14,[0,1,2,3])



    
