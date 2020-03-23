import numpy as np

def FA(a,b): # primer parametro --> funcion 1 , segundo parametro vector de salida
    if a==1:
        return b
    if a==2:
        b=np.array(b, dtype=np.float32)    
        y= 1/(1+np.exp(-b))
        return y
    if a==3:
        b=np.array(b, dtype=np.float32)
        y=np.tanh(b)
        return y
    
def DF(a,b):
    if a==1:
        return 1
    if a==2:
        b=np.array(b, dtype=np.float32) 
        y=(1/(1+np.exp(-b)))*(1-(1/(1+np.exp(-b))))
        return y
    if a==3:
        b=np.array(b, dtype=np.float32)
        y=1/np.cosh(b)**2
        return y
    
    
    
    