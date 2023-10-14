import numpy as np  # realizar operaciones matriciales
import matplotlib.pyplot as plt  # realizar graficas

# entradas
p = np.array([[2,6], [4,4], [6,3], [4,10],[7,10],[9,8]])
print(f"Entradas:\n{p}\n")

t = np.array([[0], [0], [0], [1], [1], [1]])
print(f"Target:\n{t}\n")

w = np.array([[5, 1]])
b = -1
#factor de aprendizaje

alpha = 0.1

# Regla de aprendizaje

epocas = 25
for j in range(epocas):
    print(f"Epoca numero: {j}")
    for i in range(np.shape(p)[0]):
        p_T = np.reshape(p[i],(2,1))
        a = np.dot(w,p_T)+b
        print(a)

        if a>=0:
           n=1
        else:
          n=0
        print(f"n:{n}")

          #Error
        e = t[i] - n
        print(f"e:{e}")
        
        w = w + alpha*e*p[i]
        b = b + alpha*e


# Graficar problema
plt.xlim([-1.0, 12])
plt.ylim([-1.0, 12])

patterns = np.unique(t)  # Encuentra los elementos únicos de la matriz t

for patt in patterns:
    pos = np.where(patt == t)[0]  # np.where(TRUE)[0]
    if patt == 0:
        plt.scatter(p[pos, 0], p[pos, 1], color='g',
                    s=200, marker='o', alpha=0.9)
    else:
        plt.scatter(p[pos, 0], p[pos, 1], color='b',
                    s=200, marker='x', alpha=0.9)


print(f"Vector de pesos finales",w)
print(f"Valor final del Bias",b)
x = np.linspace(-1, 12)
y = -(b / w[0][1]) - (x * w[0][0]) / w[0][1]

plt.plot(x, y, 'red', linewidth=2, label='Frontera de decision')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.title('Fronteras de decisión: REGLA DE PERCEPTRON')
plt.show()

#clasificador

p = np.array([[3,5]])
p_T = np.reshape(p[1],(2,1))
a = np.dot(w,p_T) + b

if a>=0:
  print("clase 1")
else:
   print("clase 2")
