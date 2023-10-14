import numpy as np
import matplotlib.pyplot as plt

p = np.array([[0,0],[0,1],[1,0],[1,1]])
print(f"Entradas:\n{p}\n")

t = np.array([[1],[1],[1],[0]])
print(f"Target:\n{t}\n")
#pesos
w = np.array([[2],[2]])
#bias
b= -3

w1 = np.array([[0.2],[0.15]])
#bias
b1= -0.06

w2 = np.array([[2],[2]])
#bias
b2= -0.1

## graficar problema

plt.xlim([-.5,2.0])
plt.ylim([-.5,2.0])

patterns =  np.unique(t) #encontrar valores unicos en el arreglo
print(patterns)

#genera un for de la cantidad de unicos
for patt in patterns:
    #where retorna t o f si es igual a patt = t en la posicion 0
  pos = np.where(patt == t)[0] # np.where(TRUE)[0]
  print(pos)
  if patt == 0:
      #dibuja un punto en la posicion x ,y 
    plt.scatter(p[pos, 0], p[pos, 1], color = 'g', s = 200, marker = 'o', alpha = 0.9)
  else:
    plt.scatter(p[pos, 0], p[pos, 1], color = 'b', s = 200, marker = 'x', alpha = 0.9)


#vector de puntos entre -1,2
x = np.linspace(-1,2)

#x2= -w1x1/w2-b/w2
y1 = -(b / w[1]) - (x * w[0]) / w[1]

y2 = -(b1 / w1[1]) - (x * w1[0]) / w1[1]

y3 = -(b2 / w2[1]) - (x * w2[0]) / w2[1]

plt.plot(x, y1, 'red', linewidth = 2, label='Frontera de decision')
plt.plot(x, y2, 'yellow', linewidth = 2, label='Frontera de decision')
plt.plot(x, y3, 'green', linewidth = 2, label='Frontera de decision')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.title('Fronteras de decisión: REGLA DE PERCEPTRON')
plt.show()
