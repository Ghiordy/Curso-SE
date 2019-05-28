# -*- coding: utf-8 -*-
"""
Created on Tue May 28 06:56:25 2019

@author: Ghiordy F. Contreras
retrieved from Unidad 2 - Lenguajes de programación
by Angelo Joseph Soto Vergel
"""

from random import randrange
from time import clock

def rellena(talla,rango):
    valores = [0] * talla
    for i in range(talla):
        valores[i] = randrange(0,rango)
    return valores

def burbuja(valores):
    nuevo = valores[:]
    for i in range(len(nuevo)):
        for j in range(len(nuevo)-1-i):
            if nuevo[j] > nuevo[j+1]:
                nuevo[j], nuevo[j+1], nuevo[j]
    return nuevo

# Programa principal
talla = 10
rango = 100000

tiempo_minimo = 10
repeticiones = 0

vector = rellena(talla,rango)

tiempo_inicial = tiempo_final = clock()

while tiempo_final - tiempo_inicial < tiempo_minimo:
    ordenado = burbuja(vector)
    repeticiones += 1
    tiempo_final = clock()

print("Tiempo de ejecucion de burbuja: %f"%\
      ((tiempo_final - tiempo_inicial)/repeticiones))
print((tiempo_final - tiempo_inicial)/repeticiones)
print("Rango: ",rango)
print("Talla: ",talla)
    
