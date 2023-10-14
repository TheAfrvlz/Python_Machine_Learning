import numpy as np
import matplotlib.pyplot as plt
from skimage import io,data
from skimage.color import rgb2gray
from skimage.morphology import binary
#=====================================
def HardLim(n):
    if (n<0): a=0
    else: a=1
    return a
#======================================
Ima1=io.imread('anemiaOriginal.jpg')
Ima2=io.imread('globuloOriginal.jpg')

ima1=rgb2gray(Ima1)
#plt.figure(1)
#plt.imshow(ima1,cmap='gray')
binario1=ima1<.7
plt.figure()
plt.imshow(binario1,cmap='gray')

ima2=rgb2gray(Ima2)
#plt.figure(3)
#plt.imshow(ima2,cmap='gray')
binario2=ima2<.7
plt.figure()
plt.imshow(binario2,cmap='gray')

R=binario1.size
P1=np.ndarray.flatten(binario1) #patron imagen1
P2=np.ndarray.flatten(binario2) #patron imagen2

#========================================================0
W1=np.random.rand(1,R)
W2=W1

b=-0.5
alpha=1#factor de apendizaje
gamma=0.1#factor de olvido
PT1=np.transpose(P1)
PT2=np.transpose(P2)

print(W1)
print(W2)

for epoca in range(1000):
    #Neurona 1
    n=np.dot(W1,P1)+b
    a=HardLim(n)
    W1=W1+(alpha*a*PT1)-(gamma*W1)
    #Neurona 2
    n=np.dot(W2,P2)+b
    a=HardLim(n)
    W2=W2+(alpha*a*PT2)-(gamma*W2)
print(W1)
print(W2)

np.savetxt("W1.txt",W1)
np.savetxt("W2.txt",W2)