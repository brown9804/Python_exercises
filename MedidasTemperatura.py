#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 14:35:33 2018

@author: brown9804
"""
############ 			DEFINICIONES				#######

#def rankineAFahrenheit(rankine):
 #   fanh = rankine -459.67
  #  return fanh


def fahrenheitARankine(fahrenheit):
	rankine = fahrenheit + 459.67
	return rankine
    
def celciusAFahrenheit(celsius):
	fahrenheit = (9/5)*celsius + 32
	return fahrenheit

#def kelvinARankine(kelvin):
 #   rankine = (9/5)*kelvin
  #  return rankine

def rankineAKelvin(rankine):
	kelvin = (5/9)*rankine 
	return kelvin 


def esencial():
	imprimir = True
	while (imprimir):    
		valorSeleccionado = int(input("1. Fahrenheit a Kelvin\n2. Celsius a Rankine\n\n ¿Cuál tabla desea imprimir? "))
		if (valorSeleccionado == 1):
			incremento = input("Digite el incremento entre líneas: ")
			temperatura = 0
			print("\nFahrenehit\tKelvin")
			while temperatura <= 200:
				rankinef = fahrenheitARankine(temperatura)
				print("%f\t%f" % (temperatura, rankinef))
				temperatura += incremento
		elif (valorSeleccionado ==2):
			celsius = int(input("¿Cuál es la temperatura inicial para comenzar con la conversión de Celsius a Rankine?"))
			incremento = input("Digite el incremento entre líneas: ")
			temperatura = 0
			print("\nCelsius\tRankine")
			while (temperatura >= 0 and temperatura <26):
				for multi in range(0,26):
					rankine = fahrenheitARankine(celciusAFahrenheit(celsius))
					print("%f\t%f" % (temperatura, rankine))
					temperatura += incremento
		
		imprimir = bool(int(input("¿Desea imprimir otra tabla?\n1 - Sí\n0 - No\n")))

		
		
####### 			IMPLEMENTACION				#######
   	
esencial()


