# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 10:53:41 2022

@author: luisn
"""

import numpy as np
import matplotlib.pyplot as plt
# player,frame,x,y,dx,dy,team,edgecolor,bgcolor
filename = 'Real_vs_Barcelona_limpio.csv'
# leer los datos numéricos 
ind_num = np.arange(0,6)
datos_num = np.genfromtxt(filename,delimiter=',',dtype='float',skip_header=True,usecols=ind_num)
# leer los datos string (palabras)
ind_str = np.arange(6,9)
datos_str = np.genfromtxt(filename,delimiter=',',dtype='str',skip_header=True,usecols=ind_str)
# la figura con todas las jugadas. 
fsize = 15
plt.figure()
plt.scatter(datos_num[0:288,2],datos_num[:288,3],c='rebeccapurple',s=10)
plt.title('Posicion de un jugador en la jugada',fontsize=fsize)
plt.xlabel('largo de la cancha',fontsize=fsize-1)
plt.ylabel('ancho de la cancha',fontsize=fsize-1)
plt.xlim([0,100])
plt.ylim([0,80])
plt.tick_params(labelsize=fsize-2)
# encontrar los jugadores unicos
players = np.unique(datos_num[:,0])


plt.figure()
for j in range(np.size(players)):
    indaux=datos_num[:,0]==players[j]
    posaux=datos_str[indaux,0][0]
    plt.pause(.000001)
    if posaux=='attack':
        plt.scatter(datos_num[indaux,2],datos_num[indaux,3],c='blue',s=10,label=players[j],marker="H")
    elif posaux=='defense':
        plt.scatter(datos_num[indaux,2],datos_num[indaux,3],c='red',s=10,label=players[j],marker="*")
plt.title('Posiciones de todos los jugadores en una jugada',fontsize=fsize)
plt.xlabel('largo de la cancha',fontsize=fsize-1)
plt.ylabel('ancho de la cancha',fontsize=fsize-1)
plt.legend()
plt.figure()
plt.xlim([0,100])
plt.ylim([0,80])
for j in range(288):
    plt.scatter(datos_num[j,2],datos_num[j,3],c='peru')
    plt.pause(.000001)
del j


cuadros=np.unique(datos_num[:,1]); Ncuadros=np.size(cuadros)
plt.figure()
ax = plt.gca()
ax.set_facecolor('green')
plt.show()
for j in range (Ncuadros):
    ind=datos_num[:,1]==1
    plt.scatter(datos_num[ind,2],datos_num[ind,3],c=datos_str[ind,1])
    plt.xlim([20,100])
    plt.ylim([0,90])
    plt.pause(0.0001)
del j