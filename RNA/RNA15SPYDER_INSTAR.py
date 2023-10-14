import numpy as np
import matplotlib.pyplot as plt
from skimage import io,data
from skimage.color import rgb2gray
from skimage.morphology import binary
import math
#=====================================
def hardLim(n):
    if (n<0): a=0
    else: a=1
    return a
#======================================
Ima12=io.imread("anemia.jpg")

ima12=rgb2gray(Ima12)
binario12=ima12<.7

plt.figure()
plt.imshow(binario12,cmap='gray')

P12=np.ndarray.flatten(binario12)

#-------------------------
Pt=P12
Pn=np.linalg.norm(Pt)
W1=np.loadtxt('w1.txt')
W2=np.loadtxt('w2.txt')
Wn1=np.linalg.norm(W1)
Wn2=np.linalg.norm(W2)
theta=(math.pi)/2.8 #43%
#-------------------------
#INSTAR NUMERO 1
b1=-(Wn1*Pn*(math.cos(theta)))
n1=(np.dot(W1,Pt))+(b1)
a1=hardLim(n1)
#INSTAR NUMERO 2
b2=-(Wn2*Pn*(math.cos(theta)))
n2=(np.dot(W2,Pt))+(b2)
a2=hardLim(n2)


print("N1")
print(a1)
print("N2")
print(a2)