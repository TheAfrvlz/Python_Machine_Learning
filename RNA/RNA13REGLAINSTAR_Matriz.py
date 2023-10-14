import numpy as np
import math

def hardlim(n):
    if (n < 0):
        a=0
    else:
        a =1
    return a

W =  np.array(([0,0,0,0,1,1,0,0,0,0],
               [0,0,0,0,1,1,0,0,0,0],
               [0,0,0,0,1,1,0,0,0,0],
               [0,0,0,0,1,1,0,0,0,0],
               [0,0,0,0,1,1,0,0,0,0],
               [0,0,0,0,1,1,0,0,0,0],
               [0,0,0,0,1,1,0,0,0,0],
               [0,0,0,0,1,1,0,0,0,0],))

Pt =  np.array(([0,0,0,0,1,1,0,0,0,0],
               [0,0,0,0,1,1,0,0,0,0],
               [0,0,0,0,1,1,0,0,0,0],
               [0,0,0,0,1,1,0,0,0,0],
               [0,0,0,0,1,1,0,0,0,0],
               [0,0,0,0,1,1,0,0,0,0],
               [0,0,0,0,1,1,0,0,0,0],
               [0,0,0,1,1,1,1,0,0,0],))

#flates 
W= W.flatten()
Pt = Pt.flatten()


Wn = np.linalg.norm(W)
print(Wn)
Pn = np.linalg.norm(Pt)
print(Pn)

theta =0 
#theta = (math.pi)/6
#regla instar
b = - (Wn*Pn*(math.cos(theta)))
n = np.dot(W,Pt)+b
a = hardlim(n)

print(f"a= {a}")