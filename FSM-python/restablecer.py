# -*- coding: utf-8 -*-
"""
Created on Mon Mar  16:10:24 2019
@author: Ghiordy F. Contreras
"""

import time
import RPi.GPIO as GPIO
print('Borrando scripts anteriores en el',time.strftime("%c"))
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
def restablecer():
    for i in range(27):
        GPIO.setup(i,GPIO.OUT)
        GPIO.output(i,False)
        print('Pin ',i,'restablecido')
    print('Terminado: ',time.strftime("%c"))
    return 'Hecho!'

restablecer()

''' Reestablece los pines cuando no se sabe
que programa ha sido cargado previamente y evita
danar algun dispositivo nuevo al conectar en el GPIO'''