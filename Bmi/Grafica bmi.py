# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 07:16:05 2022
empty.arange
@author: luisn
Evaluar directamente y=f(x)
la funcion se aplica a cada elemento del arreglo(element-wise)
for j1 in range(tamaño de x1)
    for j2 in range(tamaño de x2)
    y[j1,j2] =f(x[1]+x[2])
    del j1
    del j2

"""
import numpy as np
import matplotlib.pyplot as plt
#definiendo variables
m= np.arange(35,120,1) #definiendo la variable de masa
h= np.arange(1.35,2.20,0.01) #definiendo la variable de la altura en cm
#malla para crear la funcion
mm, hh = np.meshgrid(m,h)


#Evaluacion de la funcion m/h**2
bmi=mm/hh**2 #ecuacion del bmi

mycmap = plt.get_cmap('plasma',20)
niveles = [18.5,25,30]


plt.figure() #Crea una grafica
graf_malla = plt.pcolormesh(mm,hh,bmi,cmap=mycmap) 
graf_cont = plt.contour(mm,hh,bmi,niveles,colors='black',linewidths=3)
plt.colorbar(graf_malla) #Hace que el mesh tenga color
plt.xlabel('masa [kg]')
plt.ylabel('altura [cm]')
plt.title('Indice de masa corporal en funcion de masa y altura')
