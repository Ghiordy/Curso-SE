# -*- coding: utf-8 -*-
"""
Created on Mon Mar  23:17:24 2019
@author: Ghiordy F. Contreras
"""

import RPi.GPIO as GPIO
import time
import numpy as np

# Parametros de trabajo
# entradas = [2,3]
# rebote = 1
# pare = 14
# estados = [0,1,2,3,4,5,6,7]

# palancas.................
# [x1,x2,x3] = [17,27,22]
# salidas
# [C,D]= [23,24]

def configurar(entradaA,entradaB,x,C,D,pare,estados):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(entradaA,GPIO.IN)
    GPIO.setup(entradaB,GPIO.IN)
    GPIO.setup(pare,GPIO.IN)
    GPIO.setup(x[0],GPIO.OUT)
    GPIO.setup(x[1],GPIO.OUT)
    GPIO.setup(x[2],GPIO.OUT)
    GPIO.setup(C,GPIO.OUT)
    GPIO.setup(D,GPIO.OUT)
    estado = estados[0]
    return estado

def decoSalida(estado,estados,C,D,a,b):
    if estado == estados[0]:
        if a:
            GPIO.output(C,1)
            GPIO.output(D,0)
	    print('Ficha sale por C')
        elif b:
            GPIO.output(C,1)
            GPIO.output(D,0)
	    print('Ficha sale por D')
    elif estado == estados[1]:
        if a:
            GPIO.output(C,1)
            GPIO.output(D,0)
	    print('Ficha sale por C')
        elif b:
            GPIO.output(C,1)
            GPIO.output(D,0)
	    print('Ficha sale por C')
    elif estado == estados[2]:
        if a:
            GPIO.output(C,1)
            GPIO.output(D,0)
	    print('Ficha sale por C')
        elif b:
            GPIO.output(C,0)
            GPIO.output(D,1)
	    print('Ficha sale por D')
    elif estado == estados[3]:
        if a:
            GPIO.output(C,1)
            GPIO.output(D,0)
	    print('Ficha sale por C')
        elif b:
            GPIO.output(C,0)
            GPIO.output(D,1)
	    print('Ficha sale por D')
    elif estado == estados[4]:
        if a:
            GPIO.output(C,0)
            GPIO.output(D,1)
	    print('Ficha sale por D')
        elif b:
            GPIO.output(C,0)
            GPIO.output(D,1)
	    print('Ficha sale por D')
    elif estado == estados[5]:
        if a:
            GPIO.output(C,0)
            GPIO.output(D,1)
	    print('Ficha sale por D')
        elif b:
            GPIO.output(C,0)
            GPIO.output(D,1)
	    print('Ficha sale por D')
    elif estado == estados[6]:
        if a:
            GPIO.output(C,1)
            GPIO.output(D,0)
	    print('Ficha sale por C')
        elif b:
            GPIO.output(C,0)
            GPIO.output(D,1)
	    print('Ficha sale por D')
    elif estado == estados[7]:
        if a:
            GPIO.output(C,1)
            GPIO.output(D,0)
	    print('Ficha sale por C')
        elif b:
            GPIO.output(C,1)
            GPIO.output(D,0)
	    print('Ficha sale por C')
    return 'Reiniciando...'

def decoEstado(entradaA,entradaB,estado,rebote,estados):
    a = GPIO.input(entradaA)
    b = GPIO.input(entradaB)
    time.sleep(rebote)
    if estado == estados[0]:
        if a:
            estado = estados[7]
        elif b:
            estado = estados[2]
    elif estado == estados[1]:
        if a:
            estado = estados[6]
        elif b:
            estado = estados[3]
    elif estado == estados[2]:
        if a:
            estado = estados[5]
        elif b:
            estado = estados[3]
    elif estado == estados[3]:
        if a:
            estado = estados[4]
        elif b:
            estado = estados[1]
    elif estado == estados[4]:
        if a:
            estado = estados[0]
        elif b:
            estado = estados[6]
    elif estado == estados[5]:
        if a:
            estado = estados[1]
        elif b:
            estado = estados[4]
    elif estado == estados[6]:
        if a:
            estado = estados[2]
        elif b:
            estado = estados[7]
    elif estado == estados[7]:
        if a:
            estado = estados[3]
        elif b:
            estado = estados[5]
    return [estado,a,b]

def canicasFSMmealy(entrada,x,rebote,pare,estados,salida):
    print('Instante: ',time.strftime("%c"))
    estado = configurar(entrada[0],entrada[1],x,salida[0],salida[1],pare,estados)
    [aciertos,a,b] = [0,0,0]
    while(GPIO.input(pare) != 0):
        print('ESTADO: S',estado)
        so = decoSalida(estado,estados,salida[0],salida[1],a,b)
        [estado,a,b] = decoEstado(entrada[0],entrada[1],estado,rebote,estados)
    print('Se han logrado ',aciertos,' detecciones')
    return aciertos

# funcion     -entradas-palancas-       -estados--------salidas-
canicasFSMmealy([2,3],[17,27,22],1,14,[0,1,2,3,4,5,6,7],[23,24])
