# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 08:11:27 2022

@author: luisn
"""

import pandas as pd
import numpy as np
import scipy.stats as sps
import matplotlib.pyplot as plt

df = pd.read_csv('penguins.csv')
df.columns
aleta= df['flipper_length_mm'].dropna()
masa = df['body_mass_g'].dropna()


plt.figure()
plt.scatter(masa, aleta, c='peru',s=30,marker='p',label='obs')
plt.title('Diagrama de dispersion masa vs aleta')
plt.xlabel('masa')
plt.ylabel('aleta')
plt.legend()

c= np.corrcoef(masa,aleta)

slope, intercept, rvalue, p, se= sps.linregress(masa,aleta)
ygorro = intercept + slope*masa


plt.figure()
plt.plot(masa,ygorro,linewidth=2,color='teal',label='predicción')
plt.scatter(masa, aleta, c='peru',s=30,marker='p',label='obs')

plt.title('Diagrama de dispersion masa vs aleta \n r='+str(round(c[0,1],2)))
plt.xlabel('masa')
plt.ylabel('aleta')
plt.legend()


residuales = aleta-ygorro
orden = np.arange(1,np.size(residuales)+1)
plt.figure()
plt.subplot(1,2,1)
plt.stem(orden,residuales)
plt.title('Residuales vs Orden')
plt.xlabel('orden')
plt.ylabel('valor de residual')
plt.subplot(1,2,2)
plt.hist(residuales, 30,color='violet',histtype='step',density=True)
plt.xlabel('Valor de residual')
plt.ylabel('Frecuencia normalizada')
plt.title('Distribución de los residuales')
