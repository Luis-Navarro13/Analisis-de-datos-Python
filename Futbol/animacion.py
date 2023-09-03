"""
Created on Fri Sep  2 08:29:56 2022

@author: luisn
"""

import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0,10,0.1); Nt = np.size(t)

x=t*np.cos(t)
y=t*np.sin(t)

u=-t*np.cos(t)
v=-t*np.sin(t)
plt.figure()
for j in range(Nt):
    plt.scatter(x[j],y[j],c='peru')
    plt.scatter(u[j],v[j],c='teal')
    plt.xlim([-10,10])
    plt.ylim([-8,8])
    plt.pause(.000001)
del j
