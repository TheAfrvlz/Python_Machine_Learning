import numpy as np
import os
import re
import matplotlib.pyplot as plt
from tensorflow.keras.utils import to_categorical
import keras
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from keras.models import Sequential,Input,Model
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers.advanced_activations import LeakyReLU


print(os.getcwd())
dirname = os.path.join(os.getcwd(), 'sportimages')
imgpath = dirname + os.sep 
print(os.getcwd())
images = []
directories = []
dircount = []
prevRoot=''
cant=0

print("leyendo imagenes de ",imgpath)

for root, dirnames, filenames in os.walk(imgpath):
    for filename in filenames:
        if re.search("\.(jpg|jpeg|png|bmp|tiff)$", filename):
            cant=cant+1
            filepath = os.path.join(root, filename)
            image = plt.imread(filepath)
            images.append(image)
            b = "Leyendo..." + str(cant)

            if prevRoot !=root:
                prevRoot=root
                directories.append(root)
                dircount.append(cant)
                cant=0
dircount.append(cant)
dircount = dircount[1:]
dircount[0] = dircount[0]+1
print('Directorios leidos:',len(directories))
print("Imagenes en cada directorio", dircount)
print('suma Total de imagenes en subdirs:',sum(dircount))


labels =[]
indice =0
for cantidad in dircount:
    for i  in range(cantidad):
        labels.append(indice)
    indice = indice+1
print("Cantidad etiquetas creadas",len(labels))

deportes = []
indice = 0
for directorio in directories:
    name = directorio.split(os.sep)
    print(indice,name[len(name)-1])
    deportes.append(name[len(name)-1])
    indice = indice+1

y = np.array(labels)
X = np.array(images, dtype=np.uint8)

classes = np.unique(y)
nClasses = len(classes)
print('total number of outputs',nClasses)
print('output clases:' , classes)


trainX, testX, trainY, testY = train_test_split(X,y,test_size= 0.2)
print("training data shape: ", trainX.shape,trainY.shape)
print("testing data shape", testX.shape,testY.shape)

trainX = trainX.astype(np.float32)
testX = testX.astype(np.float32)
trainX = trainX.astype(np.float32)
testX = testX.astype(np.float32)


train_Y_one = to_categorical(trainY)
test_y_one = to_categorical(testY)

print('original label', trainY[0])
print('after conversion',train_Y_one[0])


