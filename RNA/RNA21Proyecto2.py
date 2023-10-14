import numpy as np
import matplotlib.pyplot as plt
from skimage import io,data
from skimage.color import rgb2gray
from skimage.morphology import binary
import math
import numpy as np
import matplotlib.pyplot as plt
from skimage import io,data
from skimage.color import rgb2gray
from skimage.morphology import binary

Ima1=io.imread('Srojo.jpg')
Ima2=io.imread('Samarillo.jpg')
Ima3=io.imread('Sverde.jpg')

ima1=rgb2gray(Ima1)
plt.figure(1)
plt.imshow(ima1,cmap='gray')
binario1=ima1<.7
plt.figure()
plt.imshow(binario1,cmap='gray')