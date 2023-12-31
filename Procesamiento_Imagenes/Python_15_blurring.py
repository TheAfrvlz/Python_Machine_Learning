from matplotlib import pyplot as plt
import numpy as np
import mahotas
import cv2

image = cv2.imread('imagenes/newIMA.jpg')

kernel = np.ones((5,5),np.float32)/25
 
#Filtra la imagen utilizando el kernel anterior
dst = cv2.filter2D(image,-1,kernel)
 
plt.subplot(121),plt.imshow(image),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Promediada')
plt.xticks([]), plt.yticks([])
cv2.imshow("Convolucion2d",dst)
cv2.imshow("Original",image)
plt.show()
cv2.waitKey(0)

#arreglo de imagenes horizontales
blurred = np.hstack([
#metodo de suavizado al cual se le asigna la imagen  y el tamaño de la matriz de suavizado
cv2.blur(image, (3, 3)),
cv2.blur(image, (5, 5)),
cv2.blur(image, (7, 7)),
cv2.blur(image, (10, 10))])
cv2.imshow("Original",image)
cv2.imshow("Averaged", blurred)
cv2.waitKey(0)

blurred = np.hstack([
cv2.GaussianBlur(image, (3, 3), 0),
cv2.GaussianBlur(image, (5, 5), 0),
cv2.GaussianBlur(image, (7, 7), 0)])
cv2.imshow("Original",image)
cv2.imshow("Gaussian", blurred)
cv2.waitKey(0)

blurred = np.hstack([
cv2.medianBlur(image, 3),
cv2.medianBlur(image, 5),
cv2.medianBlur(image, 7)])
cv2.imshow("Original",image)
cv2.imshow("Median", blurred)
cv2.waitKey(0)

blurred = np.hstack([
cv2.bilateralFilter(image, 5, 21, 21),
cv2.bilateralFilter(image, 7, 31, 31),
cv2.bilateralFilter(image, 9, 41, 41)])
cv2.imshow("Original",image)
cv2.imshow("Bilateral", blurred)
cv2.waitKey(0)