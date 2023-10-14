import numpy as np  # realizar operaciones matriciales
import matplotlib.pyplot as plt  # realizar graficas

errV=[]
#entradas
p = np.array([[1, 1], [1, 2], [2, -1], [2, 0], [-1, 2], [-2, 1], [-1, -1], [-2, -2]])
print(f"Entradas:\n{p}\n")

t = np.array([[0,0], [0,0], [0,1], [0,1], [1,0], [1,0], [1,1], [1,1]])
print(f"Target:\n{t}\n")

w = np.array([[.5,0.5],[0.5,.5]])
print(f"Pesos:\n{w}\n")

b = np.array([[1],[1]])
print(f"bias:\n{b}\n")

#factor de aprendizaje
alpha = 0.1

n = np.array([[0],[0]])
epocas = 5

for j in range(epocas):
    #np.shape(p)[0] - filas
    #np.shape(p)[1] - columnas
    print(f"epoca no: {j} -----------------")
    for i in range(np.shape(p)[0]):
        p_T = np.reshape(p[i],(2,1))
        a = np.dot(w,p_T)+b
        print(f"a: {a}\n")

        if a[0]>=0:
           n[0]=1
        else:
           n[0]=0

        if a[1]>=0:
           n[1]=1
        else:
           n[1]=0

        print (f"n: {n}\n")
        tT = np.reshape(t[i],(2,1))
        e = alpha*(tT-n)
        print (f"e: {e}\n")

        w = w + e*p[i]
        b = b + e

        errV.append(e) 

print(f"Vector final pesos: \n{w}")
print(f"Vector Bias final: \n{b}")


plt.xlim([-6, 6])
plt.ylim([-6, 6])

patterns = np.unique(t)  # Encuentra los elementos únicos de la matriz t

for patt in patterns:
    pos = np.where(patt == t)[0]  # np.where(TRUE)[0]
    if patt == 0:
        plt.scatter(p[pos, 0], p[pos, 1], color='g',
                    s=200, marker='o', alpha=0.9)
    else:
        plt.scatter(p[pos, 0], p[pos, 1], color='b',
                    s=200, marker='x', alpha=0.9)




x = np.linspace(-6, 6)
y1 = -(b[0] / w[0][1]) - (x * w[0][0]) / w[0][1]
y2 = -(b[1] / w[1][1]) - (x * w[1][0]) / w[1][1]

plt.plot(x, y1, 'red', linewidth=2, label='Frontera de decision')
plt.plot(x, y2, 'blue', linewidth=2, label='Frontera de decision')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.title('Fronteras de decisión: REGLA DE PERCEPTRON')
plt.show()
