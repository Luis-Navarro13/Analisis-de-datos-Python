# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 07:45:11 2022

@author: luisn
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mli

image_name = '9-10-1992.png'
myimage =mli.imread(image_name)

image_name2 = '8-11-2010.png'
myimage2 = mli.imread(image_name2)
#La variable es 924x1000 pixeles con 4 colores por eso (924,1000,4)
plt.figure()
plt.subplot(1, 2, 1) #agrega una tabla
plt.imshow(myimage)
plt.title('Las Vegas 1992')
plt.subplot(1, 2, 2) #agrega otra tabla #el ultimo dos significa en la parte derecha por asi decirlo

plt.imshow(myimage2)
plt.title('Las Vegas 2010')

#Trabajando con datos de 1992
mydata=np.array(myimage[:,:,:3])
mydata_gray =np.mean(mydata,axis=2)
mydata_gray2=0.216*mydata[:,:,0]+0.7152*mydata[:,:,1]+0.0722*mydata[:,:,2]

cmap_gray = plt.get_cmap('Greys_r',lut=20)
cmap_red = plt.get_cmap('Reds_r',lut=20)
cmap_green = plt.get_cmap('Greens_r',lut=20)
cmap_blue = plt.get_cmap('Blues_r',lut=20)

plt.figure()
plt.subplot(2,3,1)
plt.imshow(myimage)
plt.subplot(2,3,2)
plt.imshow(mydata_gray,cmap=cmap_gray)
plt.subplot(2,3,3)
plt.imshow(mydata_gray2,cmap=cmap_gray)
plt.subplot(2,3,4)
plt.imshow(mydata[:,:,0],cmap=cmap_red)
plt.subplot(2,3,5)
plt.imshow(mydata[:,:,1],cmap=cmap_green)
plt.subplot(2,3,6)
plt.imshow(mydata[:,:,0],cmap=cmap_blue)

valores_gray = np.ndarray.flatten(mydata_gray)
valores_gray2 = np.ndarray.flatten(mydata_gray2)
valores_reds = np.ndarray.flatten(mydata[:,:,0])

plt.figure()
plt.hist(valores_gray2,bins=100)
plt.title('Histograma del color gris')

plt.figure()
plt.hist(valores_reds,bins=50)
plt.title('Histograma del color rojo')



