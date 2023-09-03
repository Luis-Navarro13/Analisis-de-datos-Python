# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 07:18:09 2022
player,frame,x,y,z,dx,dy,coords,player_num,player_obj,team,num,name,edgecolor,bgcolor
sky_header=True
@author: luisn
"""

#genfromtxt
#loadtxt

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
plt.scatter(datos_num[:,2],datos_num[:,3],c='rebeccapurple',s=10)
plt.title('Posiciones de todos los jugadores en una jugada',fontsize=fsize)
plt.xlabel('largo de la cancha',fontsize=fsize-1)
plt.ylabel('ancho de la cancha',fontsize=fsize-1)
plt.tick_params(labelsize=fsize-2)
# encontrar los jugadores unicos
players = np.unique(datos_num[:,0])
plt.figure()
plt.ylim(0, 80)
plt.xlim(20,105)
for j in range(np.size(players)):
    indaux=datos_num[:,0]==players[j]
    posaux=datos_str[indaux,0][0]  ##Este 0 indica que va a tomar el primer elemento
    if posaux=='attack':
        plt.scatter(datos_num[indaux,2],datos_num[indaux,3],s=80,c='blue',label=players[j],marker='.',linewidth=0.5)
    elif posaux=='defense':
        plt.scatter(datos_num[indaux,2],datos_num[indaux,3],s=80,c='red',label=players[j],marker='o',linewidth=1)
del j
plt.legend()
plt.title('Posiciones de todos los jugadores en una jugada',fontsize=fsize)
plt.xlabel('largo de la cancha',fontsize=fsize-1)
plt.ylabel('ancho de la cancha',fontsize=fsize-1)
plt.tick_params(labelsize=fsize-2)
