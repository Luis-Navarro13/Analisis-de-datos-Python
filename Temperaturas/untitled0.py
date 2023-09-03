# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 13:44:56 2022

@author: luisn
"""

x=8
c=[]
while x>0:
    if x%2==0:
        x=x//2
        c.append(0)
    elif x%2==1:
        x=x//2
        c.append(1)
for i in range(1,len(c)+1):
    print(c[-i],end="")

