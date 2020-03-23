import numpy as np
import FuncionesAct as fa
import copy

def FuncionEval(w,datosE,VecFunc):                          #Matriz de w, datos en posicion(i), vector de funciones
    X=copy.deepcopy(datosE)
    X=list(X)
    X.append(-1)
    DF=[]
    DFH=[]
    hv=[]
    Yv=[]
    Y=[]
    YV=[]
    for i in range(len(w)):                                  # cantidad de matrices de pesos a multiplicar
       
       h=np.dot(w[i],X)                                      # Hace el producto punto de la cantidad de matrices
       hv.append(h)                                          # Se guarda la salida de h de cada neurona en 1 vector
       for k in range(len(w[i])):                            # Cantidad de salidas a hallar, que depende de las salidas de h
           r=len(w[i])                                       # Se utiliza para la condicion del if, si viene un escalar
           if r==1:
               Y.append(fa.FA(VecFunc[i],h))                 # Se evalua la funcion de activacion cada h de cada capa
               DF.append(fa.DF(VecFunc[i],h))
               ys=Y                                          
           else: 
               Y.append(fa.FA(VecFunc[i],h[k]))
               DF.append(fa.DF(VecFunc[i],h[k]))
               ys=Y                                          # Se sobreescribe ys para tomar la salida de la ultima neura
       DFH.append(DF)                                        # Se guardan las derivadas en DFH
       DF=[]                                                 # Se vacía DF para nuevo cálculo de DF   
       Yv.append(Y)                                          # Se guarda en Yv cada salida de cada neurona de cada capa   
       Y.append(-1)                                          # Se le agrega el sesgo para nueva la nueva entrada de la siguiente capa
       X=Y                                                   # X se convierte en la nueva entrada de la siguiente capa
       Y=[]                                                  # Se vacía Y para nuevo cálculo de salidas
       
    for j in range(len(Yv)):                                 # Se le quita el -1 (sesgo) 
           f=Yv[j]
           del f[len(f)-1]
           YV.append(f)
      
    return hv,YV,ys,DFH                                      # Se retorna matriz de arreglos de h, yv y un la salidad total 
       

        
            
                    
              
            

