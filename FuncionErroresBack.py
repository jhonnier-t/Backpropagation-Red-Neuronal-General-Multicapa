import numpy as np
import sympy as sp

def ErroresBack(w,ys,yd):
    Ev=[]
    ys=np.array(ys)
    yd=np.array(yd)
    Ee=yd-ys
    X=Ee
    Ev.append(list(Ee))
    
    for i in range(len(w)-1):                           # Numero de capas para hallar el error hacia atras
        
        w1=sp.Matrix(w[(len(w)-1)-i])                   # Se convierte a matriz
        w1.col_del(-1)                                  # Se borra la ultima columna (umbrales)
        w1=w1.T                                         # Se traspone la matriz
        X=np.array(X)                                   # Se convierte en array, X=Ee , Ee=yd-ys
        X=list(np.dot(w1,X))                            # Producto punto de entre la matriz de pesos . X
        Ev.append(X)                                    # Se agrega a una lista el producto punto
        
    Ev=list(Ev)                                         # Se guardan todos los errores de cada capa en la lista Ev
    Ev.reverse()                                        # Se reordena los errores ya que se calculó mediante backpropagation
    return Ev            
                    
    
            
        
        
    