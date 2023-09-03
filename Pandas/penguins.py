# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 08:12:30 2022

@author: luisn
"""

#seaborn es muy compatible con pandas

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('penguins.csv')
#df.info()
#Columna buscada por indice
pinguinos_sexo= df.iloc[:,7]

#Columna buscada por titulo de columna
pinguinos_sexo1= df.loc[:,'sex']

#Columna buscada por indice
pinguinos_islas= df.iloc[:,2]

#Columna buscada por titulo de columna
pinguinos_islas1= df.loc[:,'island']


#resumen estadistico
df.describe(include='all')
c = df.corr()
print(c)
conteo_especie = df['species'].value_counts()
conteo_isla = df['island'].value_counts()
conteo_sex = df['sex'].value_counts()

mycolors = ['aquamarine','turquoise','lightseagreen','cyan','aqua']

"""plt.figure()
plt.pie(conteo_especie,labels=conteo_especie.index, colors=mycolors,autopct='%.0f%%')
plt.figure()
sns.barplot(x=conteo_especie.index,y=conteo_especie)

plt.figure()
plt.pie(conteo_sex,labels=conteo_sex.index, colors=mycolors,autopct='%.0f%%')
plt.figure()
sns.barplot(x=conteo_sex.index,y=conteo_sex)

plt.figure()
sns.barplot(x=conteo_isla.index,y=conteo_isla)
plt.figure()
plt.pie(conteo_isla,labels=conteo_isla.index, colors=mycolors,autopct='%.0f%%')"""

#grafica de barras con seaborn
plt.figure()
#plt.title(label="Membresia por especie",fsize=20)

plt.subplot(1,3,1)
plt.title("Membresias por especie")
plt.pie(conteo_especie,labels=conteo_especie.index, colors=mycolors,autopct='%.2f%%',shadow=True,radius=1.3)

plt.subplot(1,3,2)
plt.pie(conteo_isla,labels=conteo_isla.index, colors=mycolors,autopct='%.2f%%',shadow=True,radius=1.3)

plt.subplot(1,3,3)
plt.pie(conteo_sex,labels=conteo_sex.index, colors=mycolors,autopct='%.2f%%',shadow=True,radius=1.3)


plt.figure()
plt.subplot(1,3,1)
plt.title("Membresias por especie")
plt.bar(x=conteo_isla.index,height=conteo_isla,color=mycolors,edgecolor="black")

plt.subplot(1,3,2)
plt.bar(x=conteo_especie.index,height=conteo_especie,color=mycolors,edgecolor="black")

plt.subplot(1,3,3)
plt.bar(x=conteo_sex.index,height=conteo_sex,color=mycolors,edgecolor="black")

CT_esp_sexo=pd.crosstab(df['species'],df['sex'])
cumu_esp_sexo = np.cumsum(CT_esp_sexo,axis=1)
sexos = CT_esp_sexo.columns
cols_sexo=['wheat','slategray']


plt.figure()
for j in range(sexos.size):
    if j==0:
        bot=0
    elif j>0:
        bot=cumu_esp_sexo[sexos[j-1]]
    plt.bar(x=CT_esp_sexo.index,height=CT_esp_sexo[sexos[j]],\
            color=cols_sexo[j],bottom=bot,edgecolor='black',label=sexos[j])
del j
plt.legend()
plt.ylabel('frecuencia')
plt.xlabel('especie')
plt.title('Membresia por especie y sexo')

CT_isla_sexo=pd.crosstab(df['island'],df['sex'])
sexos = CT_isla_sexo.columns
cols_sexo=['aquamarine','turquoise','lightseagreen','cyan','aqua']


plt.figure()
for j in range(sexos.size):
    if j==0:
        bot=0
    elif j>0:
        bot=CT_isla_sexo[sexos[j-1]]
    plt.bar(x=CT_isla_sexo.index,height=CT_isla_sexo[sexos[j]],\
            color=cols_sexo[j],bottom=bot,edgecolor='black',label=sexos[j])
del j
plt.legend()
plt.ylabel('frecuencia')
plt.xlabel('especie')
plt.title('Membresia por isla y sexo')

CT_isla_especie=pd.crosstab(df['species'],df['island'])
species = CT_isla_especie.columns
cols_especies=['aquamarine','turquoise','lightseagreen','cyan','aqua']
cumu_isla_especie = np.cumsum(CT_isla_especie,axis=1)

plt.figure()
for j in range(species.size):
    if j==0:
        bot=0
    elif j>0:
        bot=cumu_isla_especie[species[j-1]]
    plt.bar(x=CT_isla_especie.index,height=CT_isla_especie[species[j]],\
            color=cols_especies[j],bottom=bot,edgecolor='black',label=species[j])
del j
plt.legend()
plt.ylabel('frecuencia')
plt.xlabel('especie')
plt.title('Membresia por isla y especie')



#dropna 
masa_especie = df.pivot(columns='species',values='body_mass_g')
especies = CT_isla_especie.index
plt.figure()
for i in range(especies.size):
    plt.violinplot(masa_especie.loc[:,especies[i]].dropna(),showmeans=True,positions=[i])
del i
plt.xticks(range(especies.size),especies)
plt.xlabel("Especies")
plt.ylabel('Masa corporal [g]')
plt.title('Distribucion corporal por especies')


longa_especie = df.pivot(columns='species',values='flipper_length_mm')
especies = CT_isla_especie.index
plt.figure()
for i in range(especies.size):
    plt.violinplot(longa_especie.loc[:,especies[i]].dropna(),showmeans=True,positions=[i])
del i
plt.xticks(range(especies.size),especies)
plt.xlabel("Especies")
plt.ylabel('flipper_length_mm')
plt.title('Distribucion de la longitud de aletas por especies')


longp_especie = df.pivot(columns='species',values='bill_length_mm')
especies = CT_isla_especie.index
plt.figure()
for i in range(especies.size):
    plt.violinplot(longp_especie.loc[:,especies[i]].dropna(),showmeans=True,positions=[i])
del i
plt.xticks(range(especies.size),especies)
plt.xlabel("Especies")
plt.ylabel('bill_length_mm')
plt.title('Distribucion de picos por especies')

longp2_especie = df.pivot(columns='species',values='bill_depth_mm')
especies = CT_isla_especie.index
plt.figure()
for i in range(especies.size):
    plt.violinplot(longp2_especie.loc[:,especies[i]].dropna(),showmeans=True,positions=[i])
del i
plt.xticks(range(especies.size),especies)
plt.xlabel("Especies")
plt.ylabel('bill_depth_mm')
plt.title('Distribucion de la profundidad de picos por especies')





#df['colores']=np.empty(df.shape[0],dtype="str")

#df['colores'][(df['species']=='Adelie') & (df['sex']=='female')]='peru'
#df['colores'][(df['species']=='Adelie') & (df['sex']=='male')]='blue'
#df['colores'][(df['species']=='Adelie') & (df['sex'].isna())]='white'

#df['colores'][(df['species']=='Chinstrap') & (df['sex']=='female')]='peru'
#df['colores'][(df['species']=='Chinstrap') & (df['sex']=='male')]='blue'
#df['colores'][(df['species']=='Chinstrap') & (df['sex'].isna())]='white'

#df['colores'][(df['species']=='Gentoo') & (df['sex']=='female')]='peru'
#df['colores'][(df['species']=='Gentoo') & (df['sex']=='male')]='blue'
#df['colores'][(df['species']=='Gentoo') & (df['sex'].isna())]='white'


df['colores']=np.empty(df.shape[0],dtype="str")

df['colores'][(df['species']=='Adelie') & (df['sex']=='female')]='pink'
df['colores'][(df['species']=='Adelie') & (df['sex']=='male')]='purple'
df['colores'][(df['species']=='Adelie') & (df['sex'].isna())]='white'

df['colores'][(df['species']=='Chinstrap') & (df['sex']=='female')]='cyan'
df['colores'][(df['species']=='Chinstrap') & (df['sex']=='male')]='blue'
df['colores'][(df['species']=='Chinstrap') & (df['sex'].isna())]='white'

df['colores'][(df['species']=='Gentoo') & (df['sex']=='female')]='lime'
df['colores'][(df['species']=='Gentoo') & (df['sex']=='male')]='green'
df['colores'][(df['species']=='Gentoo') & (df['sex'].isna())]='white'

fig=plt.figure()
ax=plt.axes(projection='3d')
sp=ax.scatter3D(df.loc[:,'bill_length_mm'],df.loc[:,'flipper_length_mm'],df.loc[:,'body_mass_g'],s=16,c=df.loc[:,'colores'])
ax.set_xlabel('bill_length [mm]')
ax.set_ylabel('flipper_length_mm')
ax.set_zlabel('body_mass_g')
ax.set_title('Separacion por especie y sexo')

#plt.legend()
df.describe(include="all")