1# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 07:32:06 2022

@author: luisn
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df =pd.read_csv('Temperaturas_63.csv')
cols_equipo = np.arange(3,9,1) #Del 3 al 8 con paso 1
df_valores = df.iloc[:,cols_equipo] #Quedan solo los valores de la base de datos

df2 =pd.read_csv('Temperaturas_196.csv')
df_valores2 = df2.iloc[:,cols_equipo] #Quedan solo los valores de la base de datos

colores=['peru','blue','red','pink','yellow','gray','green']

equipos_label= ['E1','E2','E3','E4','E5','E6']
fsize=16
#OPCION 1
equipos = np.arange(1,7,1)
plt.figure()
for i in range(0,7):
    j=i*5
    if i>3:
        j=j-1
    plt.scatter(equipos,df_valores.iloc[j,:],c=colores[i],s=80,marker='o',label="Lugar "+str(i+1))
#plt.scatter(equipos,df_valores.iloc[5,:],c="blue",s=80,marker='o',label="Lugar 2")
plt.title("Temperatura seca",fontsize=fsize)
plt.legend()
plt.xticks(equipos,equipos_label)
plt.xlabel('Equipos',fontsize=fsize-2)
plt.ylabel('Grados',fontsize=fsize-2)
plt.tick_params(labelsize=fsize-3)



ubic_label=['Carpa - 1 ','pasto - 2','biblio - 3','Grava - 4','Cenote - 5','Pasto2 - 6','Silla - 7']
plt.figure()
plt.subplot(1,2,1)
hum_rel =[2,7,12,16,21,26,31]
for i in range(0,7):
    plt.boxplot(df_valores.iloc[hum_rel[i],:],positions=[1+i])
plt.xticks(range(1,8),ubic_label)
plt.xlabel('Ubicaciones')
plt.ylabel('Porcentaje de humedad relativa')
plt.title("Grupo 63")

plt.subplot(1,2,2)
hum_rel =[2,7,12,16,21,26,31]
for i in range(0,7):
    plt.boxplot(df_valores2.iloc[hum_rel[i],:],positions=[1+i])
plt.xticks(range(1,8),ubic_label)
plt.xlabel('Ubicaciones')
plt.ylabel('Porcentaje de humedad relativa')
plt.title("Grupo 196")



ubic_label=['Carpa','pasto','biblio','Grava','Cenote','Pasto2','Silla']
plt.figure()
hum_rel =[2,7,12,16,21,26,31]
for i in range(0,7):
    plt.violinplot(df_valores.iloc[hum_rel[i],:],positions=[1+i])
plt.xticks(range(1,8),ubic_label)
plt.xlabel('Ubicaciones')
plt.ylabel('Porcentaje de humedad relativa')


plt.figure()
plt.subplot(1,2,1)
for i in range(0,7):
    j=i*5
    if i>3:
        j=j-1
    plt.scatter(equipos,df_valores.iloc[j,:],c=colores[i],s=80,marker='o',label="Lugar "+str(i+1))
#plt.scatter(equipos,df_valores.iloc[5,:],c="blue",s=80,marker='o',label="Lugar 2")
plt.title("Temperatura seca 'Grupo 63'",fontsize=fsize)
plt.legend()
plt.xticks(equipos,equipos_label)
plt.xlabel('Equipos',fontsize=fsize-2)
plt.ylabel('Grados',fontsize=fsize-2)
plt.tick_params(labelsize=fsize-3)
equipos = np.arange(1,7,1)
plt.ylim(0,33)
plt.subplot(1,2,2)
for i in range(0,7):
    j=i*5
    if i>3:
        j=j-1
    plt.scatter(equipos,df_valores2.iloc[j,:],c=colores[i],marker='o',label="Lugar "+str(i+1))
plt.title("Temperatura seca 'Grupo 196'",fontsize=fsize)
plt.legend()
plt.xticks(equipos,equipos_label)
plt.xlabel('Equipos',fontsize=fsize-2)
plt.ylabel('Grados',fontsize=fsize-2)
plt.tick_params(labelsize=fsize-3)
plt.ylim(0,33)

colores=['peru','blue','red','pink','green']
temps=[3,8,13,22,27,32]
plt.figure()
plt.subplot(1,2,1)
for i in range(0,5):
    plt.scatter(equipos,df_valores.iloc[temps[i],:],c=colores[i],s=80,marker='o',label=ubic_label[i+2])
plt.title("Temperatura suelo 'Grupo 63'",fontsize=fsize)
plt.legend()
plt.xticks(equipos,equipos_label)
plt.xlabel('Equipos',fontsize=fsize-2)
plt.ylabel('Grados',fontsize=fsize-2)
plt.tick_params(labelsize=fsize-3)
plt.ylim(0,40)
equipos = np.arange(1,7,1)
plt.subplot(1,2,2)
for i in range(0,5):
    plt.scatter(equipos,df_valores2.iloc[temps[i],:],c=colores[i],marker='o',label=ubic_label[i+2])
    

plt.title("Temperatura suelo 'Grupo 196'",fontsize=fsize)
plt.legend()
plt.xticks(equipos,equipos_label)
plt.xlabel('Equipos',fontsize=fsize-2)
plt.ylabel('Grados',fontsize=fsize-2)
plt.tick_params(labelsize=fsize-3)
plt.ylim(0,40)

colores=['peru','blue','red','pink','yellow','gray','green']
temps=[1,6,11,15,20,25,30]
plt.figure()
plt.subplot(1,2,1)
for i in range(0,7):
    plt.scatter(equipos,df_valores.iloc[temps[i],:],c=colores[i],s=80,marker='o',label=ubic_label[i])
plt.title("Temperatura humeda 'Grupo 63'",fontsize=fsize)
plt.legend()
plt.xticks(equipos,equipos_label)
plt.xlabel('Equipos',fontsize=fsize-2)
plt.ylabel('Grados',fontsize=fsize-2)
plt.tick_params(labelsize=fsize-3)
plt.ylim(0,20)
equipos = np.arange(1,7,1)
plt.subplot(1,2,2)
for i in range(0,7):
    plt.scatter(equipos,df_valores2.iloc[temps[i],:],c=colores[i],marker='o',label=ubic_label[i])
plt.title("Temperatura humeda 'Grupo 196'",fontsize=fsize)
plt.legend()
plt.xticks(equipos,equipos_label)
plt.xlabel('Equipos',fontsize=fsize-2)
plt.ylabel('Grados',fontsize=fsize-2)
plt.tick_params(labelsize=fsize-3)
plt.ylim(10,30)
equipos = np.arange(1,7,1)




colores=['peru','blue','red','pink','yellow','gray','green']
temps=[4,9,18,23,28,33]
plt.figure()
plt.subplot(1,2,1)
for i in range(0,6):
    if i>3:
        plt.scatter(equipos,df_valores.iloc[temps[i],:],c=colores[i],s=80,marker='o',label=ubic_label[i+1])
    plt.scatter(equipos,df_valores.iloc[temps[i],:],c=colores[i],s=80,marker='o',label=ubic_label[i])
plt.title("Temperatura humeda 'Grupo 63'",fontsize=fsize)
plt.legend()
plt.xticks(equipos,equipos_label)
plt.xlabel('Equipos',fontsize=fsize-2)
plt.ylabel('Grados',fontsize=fsize-2)
plt.tick_params(labelsize=fsize-3)
plt.ylim(0,20)
equipos = np.arange(1,7,1)
plt.subplot(1,2,2)
for i in range(0,7):
    if i>3:
         plt.scatter(equipos,df_valores2.iloc[temps[i],:],c=colores[i],s=80,marker='o',label=ubic_label[i+1])
    plt.scatter(equipos,df_valores2.iloc[temps[i],:],c=colores[i],marker='o',label=ubic_label[i])
plt.title("Temperatura humeda 'Grupo 196'",fontsize=fsize)
plt.legend()
plt.xticks(equipos,equipos_label)
plt.xlabel('Equipos',fontsize=fsize-2)
plt.ylabel('Grados',fontsize=fsize-2)
plt.tick_params(labelsize=fsize-3)
plt.ylim(10,30)
equipos = np.arange(1,7,1)