# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 08:22:18 2022

@author: luisn
"""

"""
Spyder Editor
This is a temporary script file.
"""
#Mi primer codigo en ciencia de datos
#Hacer graficas de la precipitacion promedio por mes en lugares

import numpy as np #alias np
import matplotlib.pyplot as plt #alias plt

data = np.loadtxt('precip3_data.csv',dtype=float,delimiter=',')#carga el archivo, los datos se delimitan por comas

ind_meses=np.arange(12) #Grafica

nom_meses = ['anual']

plt.figure() #agarra los datos de la base, elije una columna, ancho de la linea, color de la linea, marcadores de la linea, etiqueta de la simbologia
plt.plot(ind_meses,data[12,0]*np.ones(12),linewidth=2,color='blue',linestyle='--',label="Mexico")
plt.plot(ind_meses,data[12,1]*np.ones(12),linewidth=2,color='red',linestyle='--',label="Londres")
plt.plot(ind_meses,data[12,2]*np.ones(12),linewidth=2,color='green',linestyle='--',label="KL")

plt.legend() #Crea la simbologia
plt.title('Precipitacion anual en 3 ciudades selesctas', fontsize=16)
plt.xlabel('Mes del año',fontsize=14) #eje x
plt.xlabel('precipitacion [mm]',fontsize=14)
plt.tick_params(labelsize=12)
plt.xticks(ind_meses,nom_meses)