# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 22:24:59 2022

@author: luisn
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 07:31:31 2022

@author: adolh
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#import seaborn as sns #Seaborn es una libreria que hace gráficas, es muy compatible con pandas

df=pd.read_csv('Temperaturas_63.csv')
df1=pd.read_csv('Temperaturas_196.csv')

cols_equipos=np.arange(3,9,1)

df_valores_63=df.iloc[:,cols_equipos]
df_valores_196=df1.iloc[:,cols_equipos]
#Opcion1
#Diagramma de dispersión, para todos los equipos en diferentes ubicaciones

equipos =np.arange(1,7,1)
equipos_label=['E1','E2','E3','E4','E5','E6']
indaux_locaciones=[0,5,10,14,19,24,29]
colores_ubicaciones=['peru','darkslategray','blue','rebeccapurple','green','red','darkviolet']

##Ubicacion 1
fsize=16
plt.figure()
plt.subplot(1,2,1)
for i in range(7):
    plt.scatter(equipos,df_valores_63.iloc[indaux_locaciones[i],:],c=colores_ubicaciones[i],s=40,marker='^',label='lugar '+ str(i+1))
del i
plt.title('Temperatura seca',fontsize=fsize)
plt.legend()
plt.xticks(equipos,equipos_label)
plt.xlabel('Equipos',fontsize=fsize-2)
plt.ylabel('Temperaturas')
plt.tick_params(labelsize=fsize-3)
plt.ylim(10,33)

plt.subplot(1,2,2)
for i in range(7):
    plt.scatter(equipos,df_valores_196.iloc[indaux_locaciones[i],:],c=colores_ubicaciones[i],s=40,marker='^',label='lugar '+ str(i+1))
del i
plt.title('Temperatura seca',fontsize=fsize)
plt.legend()
plt.xticks(equipos,equipos_label)
plt.xlabel('Equipos',fontsize=fsize-2)
plt.ylabel('Temperaturas')
plt.tick_params(labelsize=fsize-3)
plt.ylim(10,33)

#Cajas con humedad relativa
hum_rel=[2,7,12,16,21,26,31]
ubic_label=['CARPA','PASTO','BIBLIO','GRAVA','CENOTE','PASTO2','SILLA']

fsize=16
plt.figure()
for i in range(7):
    plt.boxplot(df_valores_63.iloc[hum_rel[i],:],positions=[i+1])
del i

for i in range(7):
    plt.violinplot(df_valores_196.iloc[hum_rel[i],:],positions=[i+1])
del i
plt.xticks(range(1,8),ubic_label)
plt.xlabel('Ubicaciones',fontsize=fsize-2)
plt.tick_params(labelsize=fsize-3)
plt.title('Humedad relativa',fontsize=fsize)