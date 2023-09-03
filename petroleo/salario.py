# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 07:29:26 2022

@author: luisn
"""

import numpy as np #importamos la libreria que tiene las funciones matematicas
import matplotlib.pyplot as plt #importamos la libreria que se encarga de hacer las graficas
import pandas as pd
#asignamos como filename a nuestra base de datos
# leer los datos numéricos  #creamos un array de 6 espacios del 0 al 5uardam
salaries_str = np.genfromtxt('AAPL.csv',delimiter=',',dtype='str',skip_header=True, usecols=[0])
salaries_float = np.genfromtxt('AAPL.csv',delimiter=',',dtype='float',skip_header=True, usecols=[1])
gas_fechas = pd.to_datetime(salaries_str)
plt.figure()
plt.plot(gas_fechas,salaries_float,color='crimson',label="Petroleo")