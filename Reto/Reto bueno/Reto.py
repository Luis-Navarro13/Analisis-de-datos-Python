import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mli
from funciones_auxiliares import DecompImage
from scipy.ndimage import gaussian_filter
from funciones_auxiliares import contarpix

import numpy.ma as ma


LV1984_pre = mli.imread('1985.png')
LV2020_pre = mli.imread('2020.png')


# suavizado Gaussiano... luego veremos para que sirve
sigma = 8
LV1984fil_pre = gaussian_filter(LV1984_pre, sigma)
LV2020fil_pre = gaussian_filter(LV2020_pre, sigma)

fsize = 16
plt.figure()
plt.subplot(2,2,1)
plt.imshow(LV1984_pre)
plt.title('1984',fontsize=fsize)
plt.subplot(2,2,2)
plt.imshow(LV2020_pre)
plt.title('2020',fontsize=fsize)
plt.subplot(2,2,3)
plt.imshow(LV1984fil_pre)
plt.title('1984 filtrado',fontsize=fsize)
plt.subplot(2,2,4)
plt.imshow(LV2020fil_pre)
plt.title('2020 filtrado',fontsize=fsize)



LV1984 = DecompImage(LV1984_pre)
LV2020 = DecompImage(LV2020_pre)

dif = LV2020 - LV1984

seq_cmap = plt.get_cmap('binary',100)
div_cmap = plt.get_cmap('bwr',101)


# cuidado aqui, hicimos la última imagen gris y no transparencia
nom_colores = ['rojos','verdes','azules','grises'] 
nom_anos = ['1984','2020','2020-1984']
Ncolores = 4
Nimages = 3


fsize = 16
plt.figure()
for jc in range(Ncolores):
 for jim in range(Nimages):
  if jim==0:
   imaux = LV1984; cmpaux = seq_cmap; limsaux=[0,1]   
  if jim==1:
   imaux = LV2020; cmpaux = seq_cmap; limsaux=[0,1]   
  if jim==2:
   imaux = dif; cmpaux = div_cmap; limsaux=[-1,1]   
  plt.subplot(Ncolores,Nimages,1+jc*Nimages+jim)  
  plt.imshow(imaux[:,:,jc],cmap=cmpaux,vmin=limsaux[0],vmax=limsaux[1])
  plt.ylabel(nom_colores[jc],fontsize=fsize-2)
  if jc==0:
   plt.title(nom_anos[jim],fontsize=fsize)
  plt.colorbar()
  del imaux, cmpaux, limsaux
 del jim
del jc 



difagreg = np.mean(dif,axis=2)
difagregA = np.sign(difagreg)*np.abs(difagreg)**(1/2)
difagregB = np.sign(difagreg)*np.abs(difagreg)**(1/3)


plt.figure()
plt.subplot(1,3,1)   
plt.imshow(difagreg,vmin=-1,vmax=1,cmap=div_cmap)
plt.title('$d$')
plt.colorbar()
plt.subplot(1,3,2)   
plt.imshow(difagregA,vmin=-1,vmax=1,cmap=div_cmap)
plt.title('$d^{1/2}$')
plt.colorbar()
plt.subplot(1,3,3)   
plt.imshow(difagregB,vmin=-1,vmax=1,cmap=div_cmap)
plt.title('$d^{1/3}$')
plt.colorbar()

#Mascara
ciudad = ma.masked_greater(difagregB,0.0)
plt.figure()
plt.subplot(1,3,1)   
plt.imshow(ciudad,vmin=-1,vmax=1,cmap=div_cmap)


#Al dividir ciudad entre ciudad, quedan solo "unos" "1" haciendo que todos los puntos se vuelvan azules
ciudad_1 = ciudad/ciudad


pix = np.sum(ciudad_1) #Nuevos pixeles en la ciudad  o cambio de 1992 a 2010



ciudadLV = ma.masked_less(LV1984[:,:,0],0.35)

plt.figure()
plt.suptitle("Kusatsu - 2000")
plt.subplot(1,2,1)
plt.imshow(LV1984[:,:,0],vmin=0,vmax=1,cmap=seq_cmap)
plt.colorbar()
plt.subplot(1,2,2)
plt.imshow(ciudadLV,vmin=0,vmax=1,cmap=seq_cmap)
plt.colorbar()


ciudadLV2 = ma.masked_less(LV2020[:,:,0],0.33)

plt.figure()
plt.suptitle(('Kusatsu - 2020'))
plt.subplot(1,2,1)
plt.imshow(LV2020[:,:,0],vmin=0,vmax=1,cmap=seq_cmap)
plt.colorbar()
plt.subplot(1,2,2)
plt.imshow(ciudadLV2,vmin=0,vmax=1,cmap=seq_cmap)
plt.colorbar()


#Codigo que tengo que sumar para


print(contarpix(ciudadLV))

print(contarpix(ciudadLV2))
