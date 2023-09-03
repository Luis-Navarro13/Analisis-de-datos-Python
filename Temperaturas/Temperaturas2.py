# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 08:11:57 2022

@author: luisn
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df =pd.read_csv('Temperaturas_196.csv')
cols_equipo = np.arange(3,9,1) #Del 3 al 8 con paso 1
df_valores = df.iloc[:,cols_equipo] #Quedan solo los valores de la base de datos

colores=['peru','blue','red','pink','yellow','gray','green']

equipos_label= ['E1','E2','E3','E4','E5','E6']
fsize=16
#OPCION 1
equipos = np.arange(1,7,1)
plt.figure()
temp_seca =[5,10,14,19,24,29]
for i in range(0,7):
    plt.scatter(equipos,df_valores.iloc[temp_seca[i],:],c=colores[i],s=80,marker='o',label="Lugar "+str(i+1))
#plt.scatter(equipos,df_valores.iloc[5,:],c="blue",s=80,marker='o',label="Lugar 2")
plt.title("Temperatura seca",fontsize=fsize)
plt.legend()
plt.xticks(equipos,equipos_label)
plt.xlabel('Equipos',fontsize=fsize-2)
plt.tick_params(labelsize=fsize-3)
plt.figure()
plt.scatter(equipos,df_valores.iloc[5,:],c=colores[i],s=80,marker='o',label="Lugar "+str(i+1))