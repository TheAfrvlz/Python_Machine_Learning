import numpy as np #realizar operaciones matriciales
import matplotlib.pyplot as plt #realizar graficas

#entradas
p = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
print(f"Entradas:\n{p}\n")

t = np.array([[0], [0], [0], [1]])
print(f"Target:\n{t}\n")

w = np.array([[0.5, 0.5]])
b = .2


#Regla de aprendizaje

#-------------------------------------------------------------------------------------------------------
#itearicion 1
p_T = np.reshape(p[0], (2, 1)) #REACOMODA np.reshape(matriz,(filas,columnas)
# Producto punto
a = np.dot(w,p_T) + b
print(f"a: {a}")

# Hardlim
if a>=0:
  n=1
else:
  n=0
print(f"n:{n}")

#Error
e = t[0] - n
print(f"e:{e}")
        
w = w + e*p[0]
b = b + e

#itearicion 2

p_T = np.reshape(p[1], (2, 1)) #REACOMODA np.reshape(matriz,(filas,columnas)
# Producto punto
a = np.dot(w,p_T) + b
print(f"a: {a}")

# Hardlim
if a>=0:
  n=1
else:
  n=0
print(f"n:{n}")

#Error
e = t[1] - n
print(f"e:{e}")
        
w = w + e*p[1]
b = b + e

#itearicion 3

p_T = np.reshape(p[2], (2, 1)) #REACOMODA np.reshape(matriz,(filas,columnas)
# Producto punto
a = np.dot(w,p_T) + b
print(f"a: {a}")

# Hardlim
if a>=0:
  n=1
else:
  n=0
print(f"n:{n}")

#Error
e = t[2] - n
print(f"e:{e}")
      
w = w + e*p[2]
b = b + e

#itearicion 4

p_T = np.reshape(p[3], (2, 1)) #REACOMODA np.reshape(matriz,(filas,columnas)
# Producto punto
a = np.dot(w,p_T) + b
print(f"a: {a}")

# Hardlim
if a>=0:
  n=1
else:
  n=0
print(f"n:{n}")

#Error
e = t[3] - n
print(f"e:{e}")
      
w = w + e*p[3]
b = b + e

#-----------------------------------------------------------------------------------------------
#itearicion 1
p_T = np.reshape(p[0], (2, 1)) #REACOMODA np.reshape(matriz,(filas,columnas)
# Producto punto
a = np.dot(w,p_T) + b
print(f"a: {a}")

# Hardlim
if a>=0:
  n=1
else:
  n=0
print(f"n:{n}")

#Error
e = t[0] - n
print(f"e:{e}")
        
w = w + e*p[0]
b = b + e

#itearicion 2

p_T = np.reshape(p[1], (2, 1)) #REACOMODA np.reshape(matriz,(filas,columnas)
# Producto punto
a = np.dot(w,p_T) + b
print(f"a: {a}")

# Hardlim
if a>=0:
  n=1
else:
  n=0
print(f"n:{n}")

#Error
e = t[1] - n
print(f"e:{e}")
        
w = w + e*p[1]
b = b + e

#itearicion 3

p_T = np.reshape(p[2], (2, 1)) #REACOMODA np.reshape(matriz,(filas,columnas)
# Producto punto
a = np.dot(w,p_T) + b
print(f"a: {a}")

# Hardlim
if a>=0:
  n=1
else:
  n=0
print(f"n:{n}")

#Error
e = t[2] - n
print(f"e:{e}")
      
w = w + e*p[2]
b = b + e

#itearicion 4

p_T = np.reshape(p[3], (2, 1)) #REACOMODA np.reshape(matriz,(filas,columnas)
# Producto punto
a = np.dot(w,p_T) + b
print(f"a: {a}")

# Hardlim
if a>=0:
  n=1
else:
  n=0
print(f"n:{n}")

#Error
e = t[3] - n
print(f"e:{e}")
      
w = w + e*p[3]
b = b + e

#---------------------------------------------------------------------------------
#itearicion 1
p_T = np.reshape(p[0], (2, 1)) #REACOMODA np.reshape(matriz,(filas,columnas)
# Producto punto
a = np.dot(w,p_T) + b
print(f"a: {a}")

# Hardlim
if a>=0:
  n=1
else:
  n=0
print(f"n:{n}")

#Error
e = t[0] - n
print(f"e:{e}")
        
w = w + e*p[0]
b = b + e

#itearicion 2

p_T = np.reshape(p[1], (2, 1)) #REACOMODA np.reshape(matriz,(filas,columnas)
# Producto punto
a = np.dot(w,p_T) + b
print(f"a: {a}")

# Hardlim
if a>=0:
  n=1
else:
  n=0
print(f"n:{n}")

#Error
e = t[1] - n
print(f"e:{e}")
        
w = w + e*p[1]
b = b + e

#itearicion 3

p_T = np.reshape(p[2], (2, 1)) #REACOMODA np.reshape(matriz,(filas,columnas)
# Producto punto
a = np.dot(w,p_T) + b
print(f"a: {a}")

# Hardlim
if a>=0:
  n=1
else:
  n=0
print(f"n:{n}")

#Error
e = t[2] - n
print(f"e:{e}")
      
w = w + e*p[2]
b = b + e

#itearicion 4

p_T = np.reshape(p[3], (2, 1)) #REACOMODA np.reshape(matriz,(filas,columnas)
# Producto punto
a = np.dot(w,p_T) + b
print(f"a: {a}")

# Hardlim
if a>=0:
  n=1
else:
  n=0
print(f"n:{n}")

#Error
e = t[3] - n
print(f"e:{e}")
      
w = w + e*p[3]
b = b + e

#---------------------------------------------------------------------------------------------------
#itearicion 1
p_T = np.reshape(p[0], (2, 1)) #REACOMODA np.reshape(matriz,(filas,columnas)
# Producto punto
a = np.dot(w,p_T) + b
print(f"a: {a}")

# Hardlim
if a>=0:
  n=1
else:
  n=0
print(f"n:{n}")

#Error
e = t[0] - n
print(f"e:{e}")
        
w = w + e*p[0]
b = b + e

#itearicion 2

p_T = np.reshape(p[1], (2, 1)) #REACOMODA np.reshape(matriz,(filas,columnas)
# Producto punto
a = np.dot(w,p_T) + b
print(f"a: {a}")

# Hardlim
if a>=0:
  n=1
else:
  n=0
print(f"n:{n}")

#Error
e = t[1] - n
print(f"e:{e}")
        
w = w + e*p[1]
b = b + e

#itearicion 3

p_T = np.reshape(p[2], (2, 1)) #REACOMODA np.reshape(matriz,(filas,columnas)
# Producto punto
a = np.dot(w,p_T) + b
print(f"a: {a}")

# Hardlim
if a>=0:
  n=1
else:
  n=0
print(f"n:{n}")

#Error
e = t[2] - n
print(f"e:{e}")
      
w = w + e*p[2]
b = b + e

#itearicion 4

p_T = np.reshape(p[3], (2, 1)) #REACOMODA np.reshape(matriz,(filas,columnas)
# Producto punto
a = np.dot(w,p_T) + b
print(f"a: {a}")

# Hardlim
if a>=0:
  n=1
else:
  n=0
print(f"n:{n}")

#Error
e = t[3] - n
print(f"e:{e}")
      
w = w + e*p[3]
b = b + e
#----------------------------------------------------------------------------------------------
#itearicion 1
p_T = np.reshape(p[0], (2, 1)) #REACOMODA np.reshape(matriz,(filas,columnas)
# Producto punto
a = np.dot(w,p_T) + b
print(f"a: {a}")

# Hardlim
if a>=0:
  n=1
else:
  n=0
print(f"n:{n}")

#Error
e = t[0] - n
print(f"e:{e}")
        
w = w + e*p[0]
b = b + e

#itearicion 2

p_T = np.reshape(p[1], (2, 1)) #REACOMODA np.reshape(matriz,(filas,columnas)
# Producto punto
a = np.dot(w,p_T) + b
print(f"a: {a}")

# Hardlim
if a>=0:
  n=1
else:
  n=0
print(f"n:{n}")

#Error
e = t[1] - n
print(f"e:{e}")
        
w = w + e*p[1]
b = b + e

#itearicion 3

p_T = np.reshape(p[2], (2, 1)) #REACOMODA np.reshape(matriz,(filas,columnas)
# Producto punto
a = np.dot(w,p_T) + b
print(f"a: {a}")

# Hardlim
if a>=0:
  n=1
else:
  n=0
print(f"n:{n}")

#Error
e = t[2] - n
print(f"e:{e}")
      
w = w + e*p[2]
b = b + e

#itearicion 4

p_T = np.reshape(p[3], (2, 1)) #REACOMODA np.reshape(matriz,(filas,columnas)
# Producto punto
a = np.dot(w,p_T) + b
print(f"a: {a}")

# Hardlim
if a>=0:
  n=1
else:
  n=0 
print(f"n:{n}")

#Error
e = t[3] - n
print(f"e:{e}")
      
w = w + e*p[3]
b = b + e

#####Graficar problema
plt.xlim([-1.0, 2.0])
plt.ylim([-1.0, 2.0])

patterns = np.unique(t) #Encuentra los elementos únicos de la matriz t

for patt in patterns:
  pos = np.where(patt == t)[0] # np.where(TRUE)[0]
  if patt == 0:
    plt.scatter(p[pos, 0], p[pos, 1], color = 'g', s = 200, marker = 'o', alpha = 0.9)
  else:
    plt.scatter(p[pos, 0], p[pos, 1], color = 'b', s = 200, marker = 'x', alpha = 0.9)

x = np.linspace(-1, 2)
y = -(b / w[0][1]) - (x * w[0][0]) / w[0][1]

plt.plot(x, y, 'red', linewidth = 2, label='Frontera de decision')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.title('Fronteras de decisión: REGLA DE PERCEPTRON')
plt.show()

