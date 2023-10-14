
import cv2 as cv

url= "http://192.168.1.14/cam-hi.jpg"
url2="http://192.168.1.18/cam-hi.jpg"

vid = cv.VideoCapture(url)
vid1 = cv.VideoCapture(url2)
Video = True
while(Video):
    ret,Frame = vid.read()
    ret1,Frame1 = vid1.read()

    if(ret):
        Frame = cv.resize(Frame,(400,400),cv.INTER_AREA)
    if(ret1):
        Frame1 = cv.resize(Frame1,(400,400),cv.INTER_AREA)
        im_h = cv.hconcat([Frame1, Frame])
        cv.imshow("camara-esp32",im_h)

    if cv.waitKey() == ord('q'):
        Video=False
        break

vid.release()
vid1.release()
cv.destroyAllWindows()
