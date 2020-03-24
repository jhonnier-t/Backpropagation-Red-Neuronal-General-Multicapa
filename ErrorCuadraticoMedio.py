import numpy as np

def ErrorCM(yd,yn):
    if len(yn[0])!=1:
        yn=np.array(yn)
        yd=np.array(yd)
        Err=yd-yn
        ET=np.sqrt(np.mean(Err**2)) 
        return ET
    else:
        yn=np.array(yn)
        yd=np.array(yd)
        yn=yn.T
        yn=yn[0][0]
        Err=yd-yn
        ET=np.sqrt(np.mean(Err**2)) 
        return ET
    
        