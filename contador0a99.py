# -*- coding: utf-8 -*-
"""
Created on Tue Mar  16:14:24 2019
@author: Ghiordy F. Contreras
"""

import RPi.GPIO as GPIO
import time
#import datetime

momento = time.strftime("%c")
print('Contador de 0 a 99 iniciado con fecha y hora: ',
      momento)
print('Cargando variables...')

GPIO.setwarnings(False)

display1 = np.array([25,8,7,12,16,20,21])
display2 = np.array([2,3,4,17,27,22,10])
comun = np.array([19,26])
numeros = np.array([[1,1,1,1,1,1,0,0],  # 0
                   [0,1,1,0,0,0,0,0],  # 1
                   [1,1,0,1,1,0,1,0],  # 2
                   [1,1,1,1,0,0,1,0],  # 3
                   [0,1,1,0,0,1,1,0],  # 4
                   [1,0,1,1,0,1,1,0],  # 5
                   [0,0,1,1,1,1,1,0],  # 6
                   [1,1,1,0,0,0,0,0],  # 7
                   [1,1,1,1,1,1,1,0],  # 8
                   [1,1,1,0,0,1,1,0]]) #9

#digitos = 2
cuenta = 0
retraso = 0.1

print('Definiendo funciones...')
print('Función configurar pines...')

def configurarPines(display1,display2):
        GPIO.setmode(GPIO.BCM)
        for i in range(len(display1)):
                GPIO.setup(display1[i],GPIO.OUT)
                GPIO.setup(display2[i],GPIO.OUT)
                GPIO.output(display1[i],False)
                GPIO.output(display2[i],False)
        print('Configuración de pines completada!')

def cargaNumero(display,numero,n,retraso):
        for i in range(len(display)):
                GPIO.output(display[i],numero[n-1,i])
        time.sleep(retraso)
        print('Número ',n,' cargado correctamente.')

def cargaNumero2(display,numero,n,retraso):
        for i in range(len(display)):
                GPIO.output(display[i],numero[n-1,i])
        time.sleep(retraso)
        print('Número ',n,' cargado correctamente.')

def secuencia(cuenta):
        if(cuenta < 10):
                cuenta = cuenta + 1
                print('Contando ... ',cuenta,' , ')
        else:
                print('Reiniciando cuenta...')
                cuenta = 0
                print('Cuenta reiniciada!')

def secuencia2(cuenta):
        if(cuenta < 100):
                cuenta = cuenta + 1
        else:
                print('Reiniciando cuenta...')
                cuenta = 0
                print('Cuenta reiniciada!')

def decisor2(cuenta,display1,display2,numero,retraso,comun):
        if(cuenta < 10):
                cargaNumero(display2,numero,cuenta,retraso,comun)
        else:
                cargaNumero(display1,numero,cuenta//10,retraso,comun)
                cargaNumero(display2,numero,cuenta%10,retraso,comun)
        secuencia2(cuenta)

def contador0a9(cuenta,display1,numero,retraso,veces):
        if(veces < 0):
                while(cuenta < 10):
                        cargaNumero(display2,numero,cuenta,retraso)
                        secuencia(cuenta)
                veces = veces - 1
        print("Conteo finalizado!")

print('Iniciando la ejecución de sentencias..')
print('Inicializando configuración de pines...')
configurarPines(display1,display2)
print('Incializando conteo de 0 a 9...')
contador0a9(cuenta,display1,numero,retraso,veces)







