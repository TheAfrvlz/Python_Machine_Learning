import matplotlib.pyplot as plt    

def hardlim(n):
    if (n < 0):
        a=0
    else:
        a =1
    return a

w_vector=[]
P0 = 1; W0 = 0 #campana
P1 = 0; W1 = 1 #alimento
b = -0.5
alpha = 0.6 #factor aprendizaje
gamma = 0.3 #factor de olvido

#razon de aprendizaje
epocas = 150

for  j in range(epocas): 
    n = (P0*W0)+(P1*W1)+b
    a = hardlim(n)#target

    #regla de hebb

    W0 =float( W0 + (alpha*a*P0)-(gamma*W0))

    if(j >10):
        P0 = 1; P1 = 1
    elif (j>100):
        P0 = 1; P1 =0


    w_vector.append(W0)

plt.plot(w_vector,'*r')
plt.show()