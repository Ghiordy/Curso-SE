# -*- coding: utf-8 -*-
"""
Created on Tue Mar  16:14:24 2019
@author: Ghiordy F. Contreras
"""

import RPi.GPIO as GPIO
import time
import numpy as np

momento = time.strftime("%c")
print('Contador de 0 a 99 iniciado con fecha y hora: ',
      momento)
print('Cargando variables...')

GPIO.setwarnings(False)

display1 = [25,8,7,12,16,20,21]
display2 = [2,3,4,17,27,22,10]
comun = [19,26]
numero = [[1,1,1,1,1,1,0,0],   # 0           
           [0,1,1,0,0,0,0,0],  # 1
           [1,1,0,1,1,0,1,0],  # 2
           [1,1,1,1,0,0,1,0],  # 3
           [0,1,1,0,0,1,1,0],  # 4
           [1,0,1,1,0,1,1,0],  # 5
           [1,0,1,1,1,1,1,0],  # 6
           [1,1,1,0,0,0,0,0],  # 7
           [1,1,1,1,1,1,1,0],  # 8
           [1,1,1,0,0,1,1,0]]  # 9

#digitos = 2
cuenta = 0
retraso = 0.1
veces = 1
pulsador =  2

print('Definiendo funciones...')

def configurarDisplay(display1,display2):
    GPIO.setmode(GPIO.BCM)
    for i in range(len(display1)):
        GPIO.setup(display1[i],GPIO.OUT)
        GPIO.setup(display2[i],GPIO.OUT)
        GPIO.output(display1[i],False)
        GPIO.output(display2[i],False)
    for i in range(len(comun)):
        GPIO.setup(comun[i],GPIO.OUT)
        GPIO.output(comun[i],True)
    print('Configuración de pines completada!')

def configurarPulsador(pin):
    GPIO.setup(pulsador,GPIO.IN)
    print('Pulsador configurado')
    return True

def leerPulsador(pulsador):
    return GPIO.input(pulsador)

def cargaNumero(display,n,retraso):
    for i in range(len(display)):
        GPIO.output(display[i],n[i])
    time.sleep(retraso*20)
    print('Número ',n,' cargado correctamente.')

def cargaNumero2(display,numero,valor,retraso,comun):
    prese = numero[valor]
    GPIO.output(comun,False)
    for i in range(len(display)):
        GPIO.output(display[i],prese[i])
    time.sleep(retraso)
    GPIO.output(comun,True)
    #print('Número ',valor,' cargado correctamente.')
    return 'Cargado'
    
def incremento():
    return False

def secuencia(cuenta):
    if(cuenta < 9):
        cuenta = cuenta + 1
        print('Contando ... ',cuenta,' , ')
    else:
        print('Reiniciando cuenta...')
        cuenta = 0
        print('Cuenta reiniciada!')
    return(cuenta)

def secuencia2(cuenta):
    if(cuenta < 100):
        cuenta = cuenta + 1
    else:
        print('Reiniciando cuenta...')
        cuenta = 0
        print('Cuenta reiniciada!')
    return cuenta

def decisor2(cuenta,display1,display2,numero,retraso,comun):
    if(cuenta < 10):
        cargaNumero2(display2,numero,cuenta,retraso,comun)
    else:
        cargaNumero2(display1,numero,cuenta//10,retraso,comun)
        cargaNumero2(display2,numero,cuenta%10,retraso,comun)
    cuenta = secuencia2(cuenta)
    print('Numero: ',cuenta)
    return cuenta

def contador0a9(cuenta,display2,numero,retraso,veces):
    if(veces > 0):
        while(cuenta < 9):
            cargaNumero(display2,numero[cuenta],retraso)
            cuenta = secuencia(cuenta)
        veces = veces - 1
        print('Quedan ',veces,' veces.')
    return("Conteo finalizado!")

def contador0a99(cuenta,display1,display2,numero,retraso,veces):
    if (veces > 0):
        while(cuenta < 100):
            cuenta = decisor2(cuenta,display1,display2,numero,retraso,comun)
        veces = veces - 1
        print('Quedan ',veces,' veces.')
    return ('Conteo finalizado')

def contadorPulsado(cuenta,display2,numero):
    while(cuenta < 9):
        cargaNumero(display2,numero[cuenta],retraso)
        if(leerPulsador):
            cuenta = secuencia(cuenta)
        if(cuenta == 9):
            cuenta = 10
            break
    return 'Conteo Finalizado'

print('Iniciando la ejecución de sentencias..')
print('Inicializando configuración de pines...')
configurarDisplay(display1,display2)
print('Incializando conteo de 0 a 9...')
#contador0a9(cuenta,display1,numero,retraso,veces)
contador0a99(cuenta,display1,display2,numero,retraso,veces)
momento = time.strftime("%c")
print('Finalizado en el siguiente momento: ',momento)