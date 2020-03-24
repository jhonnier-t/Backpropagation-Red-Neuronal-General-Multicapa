import numpy as np
import copy

def ActPesos(W,X1,yc,der,Errs,n):
    wv=copy.deepcopy(W)
    Yc=copy.deepcopy(yc)
    x=copy.deepcopy(X1)
    
    for i in range(len(wv)):                    #Numero de matrices a actualizar    
        
        x=list(x)
        x.append(-1)
        X=np.array(x)
        
        if i!=0:
            Yk=Yc[i-1]
            Yk.append(-1)
            X=Yk
            X=np.array(X)
            
        for f in range(len(wv[i])):
            for c in range(len(wv[i][f])):
                
                wv[i][f][c]=float(wv[i][f][c] + n*Errs[i][f]*der[i][f]*X[c])                  
    
    return wv