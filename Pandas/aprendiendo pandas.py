# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 08:15:59 2022

@author: luisn
"""

import pandas as pd
dic1={'var1':[1,2],'var2':[3,4]}
df = pd.DataFrame(data=dic1)

dic2={'a':1,'b':2,'c':3}
ser = pd.Series(data=dic2,index=['a','b','c']) 
#index=['a','b','c'] le das orden a tu serie
ser2 = pd.Series(data=dic2,index=['b','a','c']) 
aux = df.loc[:,'var2']

#Abrir archivo en pandas df = pd.read_csv('penguins.csv')
#df.head() vista previa de la base de datos
#df.info() resumen de la base de datos
#df.describe() estadisticos descriptivos de la base de datos
#df.iloc[] usando indices
#df.loc['nombre'] usando el nombre propio de la columna

""" 
Se pueden contar membresias de diferentes clases
df['']



"""