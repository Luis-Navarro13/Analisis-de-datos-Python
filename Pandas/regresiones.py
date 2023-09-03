# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 07:34:42 2022

@author: luisn
"""
import pandas as pd
import numpy as np
import scipy.linalg as spla
import matplotlib.pyplot as plt

df = pd.read_csv('penguins.csv')
ind = df['species'] == 'Gentoo'

x1 = df.loc[ind,'bill_length_mm'].dropna()
x2 = df.loc[ind,'bill_depth_mm'].dropna()
y = df.loc[ind,'flipper_length_mm'].dropna()

fig = plt.figure()
ax = plt.axes(projection='3d')
sp = ax.scatter3D(x1,x2,y,s=16,c='peru')

ax.set_xlabel('bill length [mm]')
ax.set_ylabel('bill depth [mm]')
ax.set_zlabel('flipper length [mm]')
ax.set_title('y=a0+a1x1+a2x2')

M=np.size(y)
Nx=2
X=np.empty((M,Nx+1)); X.fill(np.NaN)
X[:,0] = 1
X[:,1] = x1
X[:,2] = x2
invXT_X = spla.inv(np.dot(X.T,X))
beta = np.dot(np.dot( invXT_X,X.T),y)
ygorro = np.dot(X,beta)
residuales = y-ygorro
orden = np.arange(1,np.size(residuales )+1)

plt.figure( )

plt.subplot(1,2,1)

plt.stem( orden, residuales )
plt.title('residuales vs orden' )
plt.xlabel('orden')

plt.ylabel('valor de residual')
plt.subplot(1,2,2)
plt.hist(residuales,10,color='violet' ,histtype='step' ,density=True)
plt.xlabel('valor de residual')
plt.ylabel('frecuencia normalizada')
plt.title('distribucion de los residuales' )

