# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 13:33:27 2022

@author: luisn
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mli
from funciones_auxiliares import DecompImage
from scipy.ndimage import gaussian_filter
from funciones_auxiliares import contarpix

import numpy.ma as ma

LV1985_pre = mli.imread('1985.png')
LV1995_pre = mli.imread('1995.png')

LV2000_pre = mli.imread('2000.png')
LV2010_pre = mli.imread('2010.png')

LV2020_pre = mli.imread('2020.png')

LV1985 = DecompImage(LV1985_pre)
LV1995 = DecompImage(LV1995_pre)
LV2000 = DecompImage(LV2000_pre)
LV2010 = DecompImage(LV2010_pre)
LV2020 = DecompImage(LV2020_pre)

ciudadLV1 = ma.masked_less(LV1985[:,:,0],0.35)  #Bien
ciudadLV2 = ma.masked_less(LV1995[:,:,0],0.35)  #Bien
ciudadLV3 = ma.masked_less(LV2000[:,:,0],0.36)  #Bien
ciudadLV4 = ma.masked_less(LV2010[:,:,0],0.35)  #Bien
ciudadLV5 = ma.masked_less(LV2020[:,:,0],0.33)  #Bien

pixciu1=contarpix(ciudadLV1)
pixciu2=contarpix(ciudadLV2)
pixciu3=contarpix(ciudadLV3)
pixciu4=contarpix(ciudadLV4)
pixciu5=contarpix(ciudadLV5)

pixxciudad=[pixciu1,pixciu2,pixciu3,pixciu4,pixciu5]
pixcua=(164**2)
mtscua=(3000**2)
km=[]
y=[1995,2000,2010,2020]
y2=[1995,2000,2005,2010,2015,2019]
po=[101.828,115.455,121.159,130.874,137.247,141.945]
for i in range(len(pixxciudad)):
    km1=(mtscua*pixxciudad[i])/(pixcua)*(0.000001)
    km.append(km1)

fig, ax = plt.subplots(figsize = (10, 5)) 
plt.title('Kusatsu\narea y poblacion') 
km.pop(0)  
ax2 = ax.twinx() 
ax.plot(y, km, color = 'g') 
ax2.plot(y2, po, color = 'b') 
  
ax.set_xlabel('Años', color = 'r') 
ax.set_ylabel('Km^2', color = 'g') 
  
ax2.set_ylabel('Poblacion', color = 'b') 
  
plt.tight_layout() 
  
plt.show()

