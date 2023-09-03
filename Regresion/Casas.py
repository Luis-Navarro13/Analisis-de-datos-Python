# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 07:28:58 2022

@author: luisn
"""
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sps
import scipy.linalg as spla
import numpy as np
df = pd.read_csv("kc_house_data.csv")
y = df['price']
x_br = df['bathrooms']
x_area =df['sqft_living']


fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(x_br,x_area,y,s=15,c="blue")
ax.set_xlabel('No de baños')
ax.set_ylabel('area de construccion')
ax.set_zlabel('precio')

def GaussMarkov(X,y):
    invtXT_X=spla.inv(np.dot(X.T,X))
    beta=np.dot(np.dot(invtXT_X,X.T),y)
    ygorro=np.dot(X,beta)
    return beta, ygorro



M=np.size(y)
Xcua=np.empty((M,6)); Xcua.fill(np.NaN)
Xcua[:,0]=1
Xcua[:,1]=x_br
Xcua[:,2]=x_area
Xcua[:,3]=x_br**2
Xcua[:,4]=x_area**2
Xcua[:,5]=x_br*x_area
coefcua,ygorro_cua = GaussMarkov(Xcua, y)
R2_cua=np.var(ygorro_cua)/np.var(y)



fsize=16
plt.figure()
plt.subplot(1,2,1)
plt.hist(y,bins=100,color="red")
plt.xlabel('Precio de casa', fontsize=fsize-2)
plt.ylabel('Frecuencia',fontsize=fsize-2)
plt.tick_params(labelsize=fsize-3)

plt.subplot(1,2,2)
plt.hist(y,bins=100,color="peru")
plt.xlabel('Precio de casa',fontsize=fsize-2)
plt.ylabel('Frecuencia',fontsize=fsize-2)
plt.tick_params(labelsize=fsize-3)
plt.xscale('log')


plt.figure()
plt.scatter(x_br, y)
plt.xlabel('Numero de baños')
plt.ylabel('Precio de la casa')

Xlin=np.empty((M,2)); Xlin.fill(np.NaN)
Xlin[:,0]=1
Xlin[:,1]=x_br
coeflin,ygorro_lin = GaussMarkov(Xlin, y)
R2_lin=np.var(ygorro_lin)/np.var(y)

Xcua=np.empty((M,3)); Xcua.fill(np.NaN)
Xcua[:,0]=1
Xcua[:,1]=x_br
Xcua[:,2]=x_br**2
coefcua,ygorro_cua = GaussMarkov(Xcua, y)
R2_cua=np.var(ygorro_cua)/np.var(y)



plt.figure()
plt.scatter(x_br,y,label="Datos",s=10,marker="*",c="darkslategrey")
plt.scatter(x_br,ygorro_lin,label='reg lin $R^2=$'+str(np.round(R2_lin,2)),s=20,marker="p",c="fuchsia")
plt.scatter(x_br,ygorro_cua,label='reg lin $R^2=$'+str(np.round(R2_cua,2)),s=20,marker="p",c="blue")
plt.xlabel('numero de baños',fontsize=fsize-2)
plt.xlabel('precio',fontsize=fsize-2)
plt.title('Precio vs num de baños',fontsize=fsize-2)
plt.tick_params(labelsize=fsize-3)
plt.legend()

        
    
    
    
    
    
    
    
    