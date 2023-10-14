import numpy as np
import matplotlib.pyplot as plt

p = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
t = np.array([0, 1, 1, 0])

alpha = 0.5
epochs = 10000

#Pesos y bias iniciales
w1 = np.array([[0.1, 0.2], [-0.4, 0.5]])
b1 = np.array([0.3, -0.6])
w2 = np.array([0.7, 0.8])
b2 = np.array([-0.9])

#------------------------------------- Iniciando Red Neuronal
err_vector = []
for epoch in range(epochs):
  count = 0
  err = 0
  for x in p:
    #Feed forward primera capa
    n1 = np.dot(x,w1.T) + b1
    #Sigmoid function
    a1 = 1/(1+np.exp(-n1))
    #Feed forward segunda capa
    n2 = np.dot(a1,w2.T) + b2
    #Sigmoid function
    a2 = 1/(1+np.exp(-n2))
    #a2 = n2

    #Calcular error
    err += np.power(t[count] - a2, 2)

    #Backpropagation
    s2 = -(t[count] - a2) * a2 * (1-a2)

    #Actualizando pesos y bias de la segunda capa
    n_w2 = w2 - alpha * s2 * a1
    n_b2 = b2 - alpha * s2 

    s1 = s2 * w2 * a1 * (1-a1)

    #Actualizando pesos y bias de la primera
    n_b1 = b1 - alpha * s1
    x = np.reshape(x, (1, len(x)))
    s1 = np.reshape(s1, (len(s1),1))
    n_w1 = w1 - alpha * np.multiply(s1,x)

    w1 = n_w1
    b1 = n_b1
    w2 = n_w2
    b2 = n_b2

    count += 1
  err_vector.append(err)

#%%%   
# Graph error
plt.figure(0)
plt.plot(err_vector)
plt.xlabel('Epochs')
plt.ylabel('Error')
plt.title('BP algorithm')
#plt.show()

#Graficando fornteras de decisión
h = 0.01
x_min, x_max = -0.2, 1.2
y_min, y_max = -0.2, 1.2

xx,yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

Z = np.c_[xx.ravel(), yy.ravel()]
out = np.zeros(np.shape(Z)[0])

for i in range(len(out)):
  #Feed forward
  z1 = np.dot(Z[i],w1.T) + b1
  a1 = 1 / (1 + np.exp(-z1))
  z2 = np.dot(a1, w2) + b2
  a2 = 1 / (1 + np.exp(-z2))
  out[i] = a2

out = out.reshape(xx.shape)
levels = np.linspace(0, 1)
plt.figure(1)
plt.contourf(xx, yy, out, levels)
plt.colorbar()
# Plotting data
lis = np.unique(t)
for i in range(len(t)):
    if i == 0:
        pos = np.where(t == 0)[0]
        plt.plot(p[pos][:, 0], p[pos][:, 1], 'o', color = 'm', markersize = 15)
    else:
        pos = np.where(t == 1)[0]
        plt.plot(p[pos][:, 0], p[pos][:, 1], 'x', color = 'r', markersize = 15)
plt.title('Decision boundary')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

print("\tresultado MLP")
print("Patron:    t:     out:")
count = 0
for x in p:
  #feed foward
  z1 = np.dot(x,w1.T)+b1
  a1 = 1/(1+np.exp(-z1))
  z2 = np.dot(a1,w2)+b2
  a2 = 1/(1+np.exp(-z2))
  print(f"{count}.{x}-----{t[count]}----->{a2}")
  count +=1