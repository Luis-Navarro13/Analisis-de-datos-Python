# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 08:15:26 2022

@author: luisn
"""

import numpy as np
import matplotlib.pyplot as plt



fsize=16
datos= np.loadtxt('iris_data.csv' ,dtype=float,delimiter=',')
var_names=['sep lon','sep anc','pet lon','pet anc']
N=4
plt.figure()
plt.boxplot(datos[:,0:N])
plt.xticks(range(1,5),var_names)
plt.title('Diagrama de caja sin distincion de especies', fontsize=fsize)
plt.xlabel('Variable medida', fontsize=fsize-1)
plt.ylabel('[cm]', fontsize=fsize-1)
plt.tick_params(labelsize=fsize-2)


#La que tiene mayor variabilidad es la longitud del petalo
#La que tiene menor variabilidad es el ancho del sepalo



#Diagramas de caja por subespecie
especies=['setosa','versicolor','Virginica']
Ntipo=3

plt.figure()
for j in range(Ntipo):
    plt.subplot(1, Ntipo,1+j) #indexacion logica
    indaux =(datos[:,-1] == j+1)
    plt.boxplot(datos[indaux, 0:N],showmeans=True)
    plt.title(especies[j],fontsize=fsize-1)
    plt.xticks(range(1,5),var_names)
    plt.xlabel('variable medida', fontsize=fsize-2)
    plt.ylabel('[cm]', fontsize=fsize-2)   
    plt.tick_params(labelsize=fsize-3) #Tamaño de la letra en las coordenadas
    del j
    plt.suptitle('diagramas de cajas por especie', fontsize=fsize)
    
#histograma global
N=4
Tablas=['Numero de plantas Largo sepalo','Numero de plantas Ancho sepalo','Numero de plantas Largo petalo','Numero de plantas Ancho petalo']
plt.figure()
for j in range(N):
    plt.subplot(2, 2,1+j)
    plt.hist(datos[:,j],bins=15)
    plt.legend() 
    plt.title(Tablas[j])
    del j
mediciones=['Largo sepalo','Ancho sepalo','Largo petalo','Ancho petalo']
cols=['red','blue','green']

N=4
Ntipo=3
plt.figure()
for jvar in range(N):
    plt.subplot(2,2,1+jvar)
    for jesp in range(Ntipo):
        indaux =(datos[:,-1] == jesp+1)
        plt.hist(datos[indaux,jvar], bins=10,facecolor=cols[jesp],alpha=0.5,label=especies[jesp])
    del jesp
    plt.legend() 
    plt.title(mediciones[jvar])
del jvar


#Grafica de dispersion
# 1.- Abrir el canvas
# 2.- Hacer el cilo sobre las especies (range Nesp)
#       Selecciona la especie indicada
#       Grafica la especie indicada
# Termina el ciclo
# 3.- Poner leyenda
# 4.- Poner titulo
# 5.- Poner nombre a los ejes
#scatter = grafica
Nspecie = 3
fsize =14
plt.figure()
plt.subplot(1, 2, 1)
for jesp in range(Nspecie):
    indaux = datos[:,-1] == jesp+1
    plt.scatter(datos[indaux,0],datos[indaux,1],s=60,marker='h',c=cols[jesp],label=especies[jesp])
del jesp
plt.legend()
plt.xlabel('Longitud de sepalo [cm]',fontsize=fsize-1)
plt.ylabel('Ancho de sepalo [cm]',fontsize=fsize-1)
plt.title('Diagrama de dispersion para el sepalo de 3 especies de Iris', fontsize=fsize)
plt.tick_params(labelsize=fsize-2)

plt.subplot(1,2,2) #numero filas, numero de columnas
for jesp in range(Nspecie):
     indaux = datos[:,-1] == jesp+1
     plt.scatter(datos[indaux,2], datos[indaux,3], s=60,marker='*',c=cols[jesp],label=especies[jesp])
del jesp
plt.legend()
plt.xlabel('Longitud de petalo [cm]',fontsize=fsize-1)
plt.ylabel('Ancho de petalo [cm]',fontsize=fsize-1)
plt.title('Diagrama de dispersion para el petalo de 3 especies de Iris', fontsize=fsize)
plt.tick_params(labelsize=fsize-2)



























    