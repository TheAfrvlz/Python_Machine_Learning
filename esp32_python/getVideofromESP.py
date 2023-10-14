import cv2 as cv
import urllib.request
import numpy as np

url= 'http://192.168.1.14/cam-lo.jpg'
url1= 'http://192.168.1.18/cam-lo.jpg'


while(True):

    imgResponse = urllib.request.urlopen(url)
    imgNp = np.asarray(bytearray(imgResponse.read()),dtype= np.uint8)
    img = cv.imdecode(imgNp,cv.IMREAD_COLOR)
    cv.imshow('camara-1',img)

    imgResponse1 = urllib.request.urlopen(url1)
    imgNp1 = np.asarray(bytearray(imgResponse1.read()),dtype= np.uint8)
    img1 = cv.imdecode(imgNp1,cv.IMREAD_COLOR)
    cv.imshow('camara-2',img1)

    if cv.waitKey(1) & 0xff == ord('q'):
        break

cv.destroyAllWindows