#importar bibliotecas
import numpy as np #realizar operaciones matriciales
import matplotlib.pyplot as plt #realizar graficas

err_vector = []

#entradas
p = np.array([[0,0], [0,1], [1,0], [1,1]])
print(f"Entradas:\n{p}\n")

t = np.array([[-1], [-1], [-1], [1]])
print(f"Target:\n{t}\n")

w = np.array([[0.2, 0.7]])
b = 0.4

#factor de aprendizaje
alpha = 0.1

#Regla de aprendizaje
epocas = 15
for j in range(epocas):
    #print(f"Epoca numero {j}")
    esuma =0
    for i in range(np.shape(p)[0]): #Repetir segun la cantidad de filas de p
        p_T = np.reshape(p[i], (2, 1)) #REACOMODA np.reshape(matriz,(filas,columnas)
        
        # Producto punto
        a = np.dot(w,p_T) + b
        #print(f"a: {a}")
        
        # Pureline
        n = float(a) 
        #print(f"n:{n}")
        
        #Error
        e = (t[i] - n)
        #print(f"e:{e}")
        
        w = w + 2*e*alpha*p[i]
        b = b + 2*e*alpha
        esuma+= e

esuma = np.abs(esuma)
err_vector.append(esuma)
        
print(f"Vector de pesos finales:\n{w}")
print(f"Bias final:\n{b}")

#####Graficar problema
plt.xlim([-1.0, 2.0])
plt.ylim([-1.0, 2.0])

patterns = np.unique(t) #Encuentra los elementos únicos de la matriz t

for patt in patterns:
  pos = np.where(patt == t)[0] # np.where(TRUE)[0]
  if patt == -1:
    plt.scatter(p[pos, 0], p[pos, 1], color = 'g', s = 200, marker = 'o', alpha = 0.9)
  else:
    plt.scatter(p[pos, 0], p[pos, 1], color = 'b', s = 200, marker = 'x', alpha = 0.9)

x = np.linspace(-1, 5)
y = -(b / w[0][1]) - (x * w[0][0]) / w[0][1]

plt.plot(x, y, 'red', linewidth = 2, label='Frontera de decision')
plt.scatter(-.5,-.5, color = 'm', s = 100, marker = '*', alpha = 0.8)

plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.title('Fronteras de decisión: REGLA DE ADALINE')
plt.show()

####################### clasificador

p = np.array([[-0.5,-0.5]])
p_T = np.reshape(p[0], (2, 1))
a = np.dot(w,p_T) + b
if a >= 0:  
  print("clase 1")
else:  
  print("clase 2")
