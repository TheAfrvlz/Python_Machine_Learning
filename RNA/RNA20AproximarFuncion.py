import numpy as np

#---------------------------Valores iniciales
p=1
t = 1 + np.sin((p*np.pi)/(4))
w1 = np.array([[-0.27], [-0.41]])
b1 = np.array([[-0.48], [-0.13]])
w2 = np.array([[0.09, -0.17]])
b2 = np.array([[0.48]])
alpha = 0.1

#--------------------------------Feed forward
a0 = p

n1 = np.dot(w1,a0)+b1
a1 = 1 / (1 + np.exp(-n1))

n2 = np.dot(w2,a1)+b2
a2 = n2

e = t-a2

#-------------------------------Sensitividades
s2 = -2*e

s1 = a1*(1-a1)*w2.T*s2

#Propagacion hacias atras

n_w2 = w2 - alpha * s2 * a1.T
n_b2 = b2 - alpha * s2

n_w1 = w1 - alpha * s1 * a0
n_b1 = b1 - alpha * s1 