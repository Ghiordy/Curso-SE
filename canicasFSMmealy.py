# -*- coding: utf-8 -*-
"""
Created on Mon Mar  23:17:24 2019
@author: Ghiordy F. Contreras
"""

import RPi.GPIO as GPIO
import time
import numpy as np

# Parametros de trabajo
# entradaA = 2
# entradaB = 3
# rebote = 1
# pare = 14
# estados = [0,1,2,3,4,5,6,7]

# palancas.................
# [x1,x2,x3] = [17,27,22]
# salidas
# [C,D]= [23,24]

def configurar(entradaA,entradaB,x1,x2,x3,C,D,pare):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pulsador0,GPIO.IN)
    GPIO.setup(pulsador1,GPIO.IN)
    GPIO.setup(pare,GPIO.IN)
    GPIO.setup(x1,GPIO.OUT)
    GPIO.setup(x2,GPIO.OUT)
    GPIO.setup(x3,GPIO.OUT)
    GPIO.setup(C,GPIO.OUT)
    GPIO.setup(D,GPIO.OUT)
    estado = estados[0]
    return estado

def leer(pin):
    return GPIO.input(pin)

def decoSalida(estado,salida,p1):
    deteccion = False
    if estado == 0:
        GPIO.output(salida,0)
    if estado == 1:
        GPIO.output(salida,0)
    if estado == 2 :
        if p1 == 1:
            GPIO.output(salida,1)
            deteccion = True
        elif p1 == 0:
            GPIO.output(salida,0)
    return deteccion

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
            estado = estados[1]
    return [estado,p1]

def main([entradaA,entradaB],[x1,x2,x3],rebote,pare,estados,[C,D]):
    print('Instante: ',time.strftime("%c"))
    estado = configurar(entradaA,entradaB,x1,x2,x3,pare)
    aciertos = 0
    p1 = 0
    while(leer(pare) != 0):
        print('ESTADO: S',estado)
        so = decoSalida(estado,salida,p1)
        if so:
            print('Secuencia detectada')
            aciertos =+1
        else:
            print('Por favor ingrese 101')
        [estado,p1] = decoEstado(pulsador0,pulsador1,estado,rebote,estados)
    print('Se han logrado ',aciertos,' detecciones')
    return aciertos

main([2,3],[17,27,22],1,14,[0,1,2,3,4,5,6,7],[23,24])
    
