# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 07:39:51 2022

@author: luisn
"""

import numpy as np

# funcion para separar imagenes
def DecompImage(img):
 # toma una imagen y produce un arreglo: Red Green Blue Gray   
 img = np.array(img)
 [n1,n2,n3] = np.shape(img)
 img_new = np.empty((n1,n2,4)); img_new.fill(np.NaN)
 img_new[:,:,:3] = img[:,:,:3]
 img_new[:,:,3] = 0.2126*img[:,:,0] + 0.7152*img[:,:,1] + 0.0722*img[:,:,2]
 return img_new


def contarpix(data):
 data_1 = data/data
 pix = np.sum(data_1)
 return pix