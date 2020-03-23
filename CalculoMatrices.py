# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 12:41:35 2020

@author: user
"""
#Primer parametro vector capas

#import random
import numpy as np
import random

def Cmatrices(x): # Vector de capas
    l=len(x)
    w=[]
    
    for i in range(l-1): # numero de matrices proporcional al numero de capaz
        w1=[]
        #Llenar matrix
        for f in range(x[1+i]): # numero de filas
            w1.append([])
            for c in range(x[i]+1): # numero de columnas
                
                w1[f].append(random.random())
        
        w.append(w1)
    
    return w
                
                
                
                
        
        