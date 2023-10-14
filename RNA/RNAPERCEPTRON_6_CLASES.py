import numpy as np
import matplotlib.pyplot as plt

p = np.array([[1,5],
              [2,4],
              [4,1],
              [5,1],
              [-2,3],
              [-1,2],
              [-1,-1],
              [0,-2],
              [-5,1],
              [-4,2],
              [-3,-2],
              [-4,-3]])
print(f"Target:\n{p[0]}\n")

t = np.array([[0,0,0],
              [0,0,0],
              [1,0,0],
              [1,0,0],
              [0,1,0],
              [0,1,0],
              [1,1,0],
              [1,1,0],
              [0,0,1],
              [0,0,1],
              [1,0,1],
              [1,0,1]])
print(f"Target:\n{t[4]}\n")



w = np.array([[1, -1], [1, 1], [1, .5]])
print(f"Pesos:\n{w.shape}\n")


b = np.array([[.1], [0.5], [.5]])
print(f"Bias:\n{b.shape}\n")

#factor de aprendizaje 
alpha = 0.9

n = np.array([[0], [0], [0]])

epocas = 270
for j in range(epocas):
  for i in range(np.shape(p)[0]):
    p_T = np.reshape(p[i], (2,1))
    #print(p_T)
    #producto punto
    a = np.dot(w,p_T) + b
    #print(f"a: {a}\n")

    # Hardlim
    if a[0]>=0:
        n[0]=1
    else:
        n[0]=0
    
    if a[1]>=0:
        n[1]=1
    else:
        n[1]=0
     
        
    if a[2]>=0:
        n[2]=1
    else:
        n[2]=0
    #print(f"n: {n}\n")

    t_T = np.reshape(t[i], (3, 1))
    e = alpha*(t_T-n)
    #print(f"e: {e}\n")

    #Reglas de aprendizaje
    w = w + e*p[i]
    b = b + e


print(f"Vector de pesos finales:\n{w}")
print(f"Vector de bias final:\n{b}\n")

#Graficación
plt.xlim([-10, 10])
plt.ylim([-10, 10])


for i in range(p.shape[0]):
    
    if t[i,0] == 0 and t[i,1] == 0 and t[i,2] == 0: 
        plt.scatter(p[i, 0], p[i, 1], color = 'b', s = 100, marker = 'o', alpha = 0.75)
    
    elif t[i,0] == 1 and t[i,1] == 0 and t[i, 2] == 0: 
        plt.scatter(p[i, 0], p[i, 1], color = 'r', s = 100, marker = 'o', alpha = 0.75)
    
    elif t[i,0] == 0 and t[i,1] == 0 and t[i, 2] == 1: 
        plt.scatter(p[i, 0], p[i, 1], color = 'm', s = 100, marker = 'o', alpha = 0.75)
    
    elif t[i,0] == 1 and t[i,1] == 0 and t[i, 2] == 1: 
        plt.scatter(p[i, 0], p[i, 1], color = 'y', s = 100, marker = 'o', alpha = 0.75)
    
    elif t[i,0] == 0 and t[i,1] == 1 and t[i, 2] == 0:  
        plt.scatter(p[i, 0], p[i, 1], color = 'c', s = 100, marker = 'o', alpha = 0.75)
    
    elif t[i,0] == 1 and t[i,1] == 1 and t[i, 2] == 0:  
        plt.scatter(p[i, 0], p[i, 1], color = 'g', s = 100, marker = 'o', alpha = 0.75)
        

x = np.linspace(-10, 10)
y1 = -(b[0] / w[0][1]) - (x * w[0][0]) / w[0][1]
y2 = -(b[1] / w[1][1]) - (x * w[1][0]) / w[1][1]
y3 = -(b[2] / w[2][1]) - (x * w[2][0]) / w[2][1]

plt.plot(x, y1, 'r', linewidth = 2, label='Frontera de decision 1')
plt.plot(x, y2, 'm', linewidth = 2, label='Frontera de decision 2')
plt.plot(x, y3, 'c', linewidth = 2, label='Frontera de decision 3')
#plt.scatter(6, 7, color = 'm', s = 100, marker = '*', alpha = 0.8)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.title('PERCEPTRON de 6 Clases')
plt.show()        


x_prueba = np.array([[5], [7]])
print(np.shape(x_prueba))
x_prueba_T = np.reshape(x_prueba,(2,1))
a2 = np.dot(w, x_prueba_T) + b
if a2[0]>=0:
     n[0]=1
else:
     n[0]=0
    
if a2[1]>=0:
    n[1]=1
else:
    n[1]=0
    
if a2[2]>=0:
    n[2]=1
else:
    n[2]=0
print(f'Clase Final: {n}')