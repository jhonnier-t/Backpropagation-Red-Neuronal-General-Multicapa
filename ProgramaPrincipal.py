# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:34:10 2020

@author: Jhonnier Tangarife Ardila
"""
import time
import copy
import numpy as np
import CalculoMatrices as cm
import FuncionEvaluacion as fe
import FuncionErroresBack as eb
import ActualizarPesos as ap
import ErrorCuadraticoMedio as ecm

Tiempo_Inicial =  time.time()
#################### --- Inicialización de las variables --- ##################
vfuntion   =   [3 , 3, 2]
VectorCapas=[2 ,3 , 2, 1]
m=cm.Cmatrices(VectorCapas)
m_act=copy.deepcopy(m)
xe=[[1,1],[0,1],[1,0],[0,0]]
yd=[0,1,1,0]
n=2
##################### ---- Verificación de los datos con ECM --- #############
yn=[]
for k in range(len(yd)):
    h,yc,ys,dfh = fe.FuncionEval(m_act,xe[k],vfuntion)
    yn.append(ys)
ECM = ecm.ErrorCM(yd,yn)
###################### ---- Inicio Programa principal--------- ################
while (ECM>=0.005):
    yn=[]
    for i in range(len(xe)):  
        h,yc,ys,dfh = fe.FuncionEval(m_act,xe[i],vfuntion)
        ErroresCC = eb.ErroresBack(m_act,ys,yd[i])
        m_act = ap.ActPesos(m_act,xe[i],yc,dfh,ErroresCC,n)  
        yn.append(ys)          
    ECM=ecm.ErrorCM(yd,yn)       
####################### ---- Final Programa principal--------- ################ 
Tiempo_Final = time.time()
Tiempo_Ejecucion = Tiempo_Final - Tiempo_Inicial 
print("Tiempo de ejecucion: ",Tiempo_Ejecucion,"Segundos")
print("Salidas ideales: ",yd)
print("Salidas reales: \n",np.array(yn))

   
    




    