import numpy as np  # realizar operaciones matriciales
import matplotlib.pyplot as plt  # realizar graficas

# entradas
p = np.array([[1,1], [1,2], [2,-1], [2,0],[-1,2],[-2,1],[-1,-1],[-2,-2]])
print(f"Entradas:\n{p}\n")

t1 = np.array([[1], [1], [0], [0], [0], [0], [1], [1]])
t2 = np.array([[0], [0], [1], [1], [1], [1], [0], [0]])

print(f"Target:\n{t1}\n")

w1 = np.array([[-1,-0.5]])
b1 = 0.5

w2 = np.array([[0.5,-1]])
b2 = 0

plt.xlim([-5, 6])
plt.ylim([-5, 6])

patterns = np.unique(t1)  # Encuentra los elementos únicos de la matriz t

for patt in patterns:
    pos = np.where(patt == t1)[0]  # np.where(TRUE)[0]
    if patt == 0:
        plt.scatter(p[pos, 0], p[pos, 1], color='g',
                    s=200, marker='o', alpha=0.9)
    else:
        plt.scatter(p[pos, 0], p[pos, 1], color='b',
                    s=200, marker='x', alpha=0.9)




x = np.linspace(-6, 6)
y1 = -(b1 / w1[0][1]) - (x * w1[0][0]) / w1[0][1]
y2 = -(b2 / w2[0][1]) - (x * w2[0][0]) / w2[0][1]

plt.plot(x, y1, 'red', linewidth=2, label='Frontera de decision')
plt.plot(x, y2, 'blue', linewidth=2, label='Frontera de decision')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.title('Fronteras de decisión: REGLA DE PERCEPTRON')
plt.show()
