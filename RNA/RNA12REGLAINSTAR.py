import numpy as np
import math

def hardlim(n):
    if (n < 0):
        a=0
    else:
        a =1
    return a

W =  np.array([[12,10,25,13,27]])
Pt = np.array([[12],[10],[25],[13],[27]])

Wn = np.linalg.norm(W)
Pn = np.linalg.norm(Pt)

theta =0 
theta = (math.pi)/6
#regla instar
b = - (Wn*Pn*(math.cos(theta)))
n = np.dot(W,Pt)+b
a = hardlim(n)

print(f"a= {a}")