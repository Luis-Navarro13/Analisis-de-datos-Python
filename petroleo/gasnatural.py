# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 07:32:29 2022

@author: luisn
"""

import numpy as np #importamos la libreria que tiene las funciones matematicas
import matplotlib.pyplot as plt #importamos la libreria que se encarga de hacer las graficas
import pandas as pd
#asignamos como filename a nuestra base de datos
# leer los datos numéricos  #creamos un array de 6 espacios del 0 al 5uardam
gas_str = np.genfromtxt('daily_csv.csv',delimiter=',',dtype='str',skip_header=True, usecols=[0])
gas_float = np.genfromtxt('daily_csv.csv',delimiter=',',dtype='float',skip_header=True, usecols=[1])

gas_str2 = np.genfromtxt('brent-daily_csv.csv',delimiter=',',dtype='str',skip_header=True, usecols=[0])
gas_float2 = np.genfromtxt('brent-daily_csv.csv',delimiter=',',dtype='float',skip_header=True, usecols=[1])

gas_str3 = np.genfromtxt('wti-daily_csv.csv',delimiter=',',dtype='str',skip_header=True, usecols=[0])
gas_float3 = np.genfromtxt('wti-daily_csv.csv',delimiter=',',dtype='float',skip_header=True, usecols=[1])

salaries_str = np.genfromtxt('AAPL.csv',delimiter=',',dtype='str',skip_header=True, usecols=[0])
salaries_float = np.genfromtxt('AAPL.csv',delimiter=',',dtype='float',skip_header=True, usecols=[1])
gas_fechas = pd.to_datetime(salaries_str)


indval_apple=np.isfinite(salaries_float)
aux3 = np.mean(salaries_float)
apple_gas3=np.isfinite(salaries_float)


fsize=15
gas_fechas = pd.to_datetime(gas_str)
gas_fechas2 = pd.to_datetime(gas_str2)
gas_fechas3 = pd.to_datetime(gas_str3)
gas_fechas4 = pd.to_datetime(salaries_str)
plt.figure()
ax = plt.gca()
ax.set_facecolor('beige')
plt.title('Evolución temporal del Gas Natural, Petróleo Brent y Petróleo WTI',fontsize=fsize-1)
plt.show()
plt.plot(gas_fechas,gas_float,color='crimson',label="Petroleo")
plt.plot(gas_fechas2,gas_float2,color='blue',label="Gas natural")
plt.plot(gas_fechas3,gas_float3,color='green',label="WTI")

aux = np.mean(gas_float)
indval_gas=np.isfinite(gas_float)
daily_media = np.mean(gas_float[indval_gas])
daily_min = np.min(gas_float[indval_gas])
daily_max = np.max(gas_float[indval_gas])

plt.axhline(daily_media,color="red",label="Gas natural Media")
plt.axhline(daily_min,color="skyblue",label="Gas natural Minimo")
plt.axhline(daily_max,color="greenyellow",label="Gas natural Maximo")

aux2 = np.mean(gas_float2)
indval_gas2=np.isfinite(gas_float2)
brent_media = np.mean(gas_float2[indval_gas2])
brent_min = np.min(gas_float2[indval_gas2])
brent_max = np.max(gas_float2[indval_gas2])

plt.axhline(brent_media,color="deeppink",label="Brent Media")
plt.axhline(brent_min,color="darkblue",label="Brent Minimo")
plt.axhline(brent_max,color="lime",label="Brent Maximo")

aux3 = np.mean(gas_float3)
indval_gas3=np.isfinite(gas_float3)
wti_media = np.mean(gas_float3[indval_gas3])
wti_min = np.min(gas_float3[indval_gas3])
wti_max = np.max(gas_float3[indval_gas3])

plt.axhline(wti_media,color="maroon",label="Brent Media")
plt.axhline(wti_min,color="darkorchid",label="Brent Media")
plt.axhline(wti_max,color="salmon",label="Brent Media")

plt.xlabel('Años',fontsize=fsize-1)
plt.ylabel('Precio petroleo',fontsize=fsize-1)
plt.legend()

"""plt.figure()
aux2 = np.mean(gas_float2)
indval_gas2=np.isfinite(gas_float2)
plt.plot(gas_fechas2,gas_float2,color='red',label="Gas")
plt.axhline(brent_media,color="blue")
plt.axhline(brent_min,color="blue")
plt.axhline(brent_max,color="blue")
plt.xlabel('Años',fontsize=fsize-1)
plt.ylabel('Precio petroleo',fontsize=fsize-1)
plt.legend()"""
gas_diff = np.diff(gas_float)
gas_diff2 = np.diff(gas_float2)
gas_diff3 = np.diff(gas_float3)
apple_diff = np.diff(salaries_float)
plt.figure()
#plt.hist(gas_diff,bins=100) x variacion  Y conteo
plt.subplot(4,1,1,)
indaux = np.abs(gas_diff)<1
gas_limpio1=gas_diff[indaux]
plt.hist(gas_limpio1,bins=100,color="Purple")
plt.xlabel('Conteo',fontsize=fsize-1)
plt.ylabel('Frecuencia',fontsize=fsize-1)
plt.title('Diferencias diarias Gas natural',fontsize=fsize-1)
plt.legend()
plt.subplot(4,1,2)
indaux1 = np.abs(gas_diff2)<2
gas_limpio2=gas_diff2[indaux1]
plt.hist(gas_limpio2,bins=100,color="pink")
plt.xlabel('Conteo',fontsize=fsize-1)
plt.ylabel('Frecuencia',fontsize=fsize-1)
plt.title('Diferencias diarias Petroleo Brent',fontsize=fsize-1)
plt.subplot(4,1,3)
indaux2 = np.abs(gas_diff3)<2
gas_limpio3=gas_diff3[indaux2]
plt.hist(gas_limpio3,bins=100,color="Blue")
plt.xlabel('Conteo',fontsize=fsize-1)
plt.ylabel('Frecuencia',fontsize=fsize-1)
plt.title('Diferencias diarias Petroleo WTI',fontsize=fsize-1)
plt.subplot(4,1,4)
indaux3 = np.abs(apple_diff)<50
gas_limpio4=apple_diff[indaux3]
plt.hist(gas_limpio4,bins=100,color="Peru")
plt.xlabel('Conteo',fontsize=fsize-1)
plt.ylabel('Frecuencia',fontsize=fsize-1)
plt.title('Diferencias diarias Acciones Apple',fontsize=fsize-1)
#plt.subplot(4,1,4)
#indaux3 = np.abs(apple_diff)<.1
#gas_limpio4=apple_diff[indaux3]
#plt.hist(gas_limpio4,bins=100)

plt.figure()
aux = np.mean(gas_float)
indval_gas=np.isfinite(gas_float)
plt.plot(gas_fechas,gas_float,color='red',label="Gas")
plt.axhline(daily_media,color="blue")
plt.axhline(daily_min,color="blue")
plt.axhline(daily_max,color="blue")
plt.xlabel('Años',fontsize=fsize-1)
plt.ylabel('Precio petroleo',fontsize=fsize-1)
plt.legend()

plt.figure()
aux2 = np.mean(gas_float2)
indval_gas2=np.isfinite(gas_float2)
plt.plot(gas_fechas2,gas_float2,color='red',label="Gas")
plt.axhline(brent_media,color="blue")
plt.axhline(brent_min,color="blue")
plt.axhline(brent_max,color="blue")
plt.xlabel('Años',fontsize=fsize-1)
plt.ylabel('Precio petroleo',fontsize=fsize-1)
plt.legend()

plt.figure()
aux2 = np.mean(gas_float3)
indval_gas3=np.isfinite(gas_float3)
plt.plot(gas_fechas3,gas_float3,color='red',label="Gas")
plt.axhline(wti_media,color="blue")
plt.axhline(wti_min,color="blue")
plt.axhline(wti_max,color="blue")
plt.xlabel('Años',fontsize=fsize-1)
plt.ylabel('Precio petroleo',fontsize=fsize-1)
plt.legend()


plt.figure()
plt.subplot(4,1,1)
aux = np.mean(gas_float)
indval_gas=np.isfinite(gas_float)
plt.title('Gas natural',fontsize=fsize-1)
plt.plot(gas_fechas,gas_float,color='red',label="Diario")
plt.axhline(daily_media,color="blue",label="media",linestyle="dotted")
plt.axhline(daily_min,color="indigo",label="min",linestyle="dashed")
plt.axhline(daily_max,color="royalblue",label="max",linestyle="dashdot")
plt.xlabel('Años',fontsize=fsize-1)
plt.ylabel('Precio',fontsize=fsize-1)
ax=plt.subplot(4,1,1)
ax.set_xlim(pd.Timestamp('1986-01-01'),pd.Timestamp('2024-01-01'))
plt.legend()

plt.subplot(4,1,2)
aux2 = np.mean(gas_float2)
indval_gas2=np.isfinite(gas_float2)
plt.title('Petroleo Brent',fontsize=fsize-1)
plt.plot(gas_fechas2,gas_float2,color='red',label="Diario")
plt.axhline(brent_media,color="blue",label="media",linestyle="dotted")
plt.axhline(brent_min,color="indigo",label="min",linestyle="dashed")
plt.axhline(brent_max,color="royalblue",label="max",linestyle="dashdot")
plt.xlabel('Años',fontsize=fsize-1)
plt.ylabel('Precio',fontsize=fsize-1)
plt.legend()

plt.subplot(4,1,3)
aux2 = np.mean(gas_float3)
indval_gas3=np.isfinite(gas_float3)
plt.title('Petroleo WTI',fontsize=fsize-1)
plt.plot(gas_fechas3,gas_float3,color='red',label="Diario")
plt.axhline(wti_media,color="blue",label="media",linestyle="dotted")
plt.axhline(wti_min,color="indigo",label="min",linestyle="dashed")
plt.axhline(wti_max,color="royalblue",label="max",linestyle="dashdot")
plt.xlabel('Años',fontsize=fsize-1)
plt.ylabel('Precio',fontsize=fsize-1)
plt.legend()

plt.subplot(4,1,4)
apple_gas3=np.isfinite(salaries_float)
apple_media = np.mean(salaries_float[indval_apple])
apple_min = np.min(salaries_float[indval_apple])
apple_max = np.max(salaries_float[indval_apple])
plt.title('Acciones Apple',fontsize=fsize-1)
plt.plot(gas_fechas4,salaries_float,color='crimson',label="Diario")
plt.axhline(apple_media,color="blue",label="media",linestyle="dotted")
plt.axhline(apple_min,color="indigo",label="min",linestyle="dashed")
plt.axhline(apple_max,color="royalblue",label="max",linestyle="dashdot")
plt.xlabel('Años',fontsize=fsize-1)
plt.ylabel('Precio',fontsize=fsize-1)
plt.legend()