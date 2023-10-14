import numpy as np  # realizar operaciones matriciales
import matplotlib.pyplot as plt  # realizar graficas

# entradas
p = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
print(f"Entradas:\n{p}\n")

t = np.array([[0], [0], [0], [1]])
print(f"Target:\n{t}\n")

w = np.array([[0.5, 0.15]])
b = 1


# Regla de aprendizaje

epocas = 7
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
        
        w = w + e*p[i]
        b = b + e


# Graficar problema
plt.xlim([-1.0, 2.0])
plt.ylim([-1.0, 2.0])

patterns = np.unique(t)  # Encuentra los elementos únicos de la matriz t

for patt in patterns:
    pos = np.where(patt == t)[0]  # np.where(TRUE)[0]
    if patt == 0:
        plt.scatter(p[pos, 0], p[pos, 1], color='g',
                    s=200, marker='o', alpha=0.9)
    else:
        plt.scatter(p[pos, 0], p[pos, 1], color='b',
                    s=200, marker='x', alpha=0.9)

x = np.linspace(-1, 2)
y = -(b / w[0][1]) - (x * w[0][0]) / w[0][1]

plt.plot(x, y, 'red', linewidth=2, label='Frontera de decision')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.title('Fronteras de decisión: REGLA DE PERCEPTRON')
plt.show()
