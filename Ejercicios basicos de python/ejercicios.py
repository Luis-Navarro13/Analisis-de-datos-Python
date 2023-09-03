# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 08:05:59 2022
matplotlib.pyplot es el que maneja las imagenes
@author: luisn
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,10,0.1)
y = x**2
z = x**3
i = x**4
sen = np.sin(x)
w = np.exp(x)
coa = np.cos(x)
#y toma todos los valores de x y los eleva al cuadrado
top=100
plt.figure()
plt.subplot(1,2,1) #crea una tabla
plt.plot(x,y,color='peru',marker='h',linewidth=1,label='$x^2$')
#plt.plot(x,y) le pido que me grafique x contra y
plt.plot(x,z,color='red',marker='h',linewidth=1,label='$x^3$')
plt.plot(x,i,color='blue',marker='h',linewidth=1,label='$x^4$')
plt.ylim(-top, top)
plt.legend()
plt.xlabel('Valores de x')
plt.ylabel('Valores de x en su potencia [2,3,4]')

#TABLA 2

plt.subplot(1,2,2)
plt.ylim(-2, 10)
plt.plot(x,w,color='Orange',marker='H',linewidth=10,label='$exp(x)$')
plt.plot(x,sen,color='black',marker='*',linewidth=1,label='$sen(x)$')
plt.plot(x,coa,color='red',marker='+',linewidth=1,label='$cos(x)$')
plt.legend()
plt.xlabel('Valores de x')
plt.ylabel('Valores [EXP, SEN, COS] en x')
