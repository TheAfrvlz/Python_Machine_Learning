import cv2
import os
import mediapipe as mp
import serial
import time
import numpy as np

#ser = serial.Serial('COM4', 9600, timeout=1)
time.sleep(2)





mp_face_detection = mp.solutions.face_detection

LABELS = ["No-Seguro", "Seguro","Con - Antecedentes"]

# Leer el modelo
face_mask = cv2.face.LBPHFaceRecognizer_create()
face_mask.read("Reconocimiento_Superior.xml")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
contador_S = 0
with mp_face_detection.FaceDetection(
     min_detection_confidence=0.5) as face_detection:

     while True:
          ret, frame = cap.read()
          if ret == False: break
          frame = cv2.flip(frame, 1)

          height, width, _ = frame.shape
          frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
          results = face_detection.process(frame_rgb)

          if results.detections is not None:




               for detection in results.detections:
                    xmin = int(detection.location_data.relative_bounding_box.xmin * width)
                    ymin = int(detection.location_data.relative_bounding_box.ymin * height)
                    w = int(detection.location_data.relative_bounding_box.width * width)
                    h = int(detection.location_data.relative_bounding_box.height * height)


                    if xmin < 0 and ymin < 0:
                         continue

                    face_image = frame[ymin : ymin + h, xmin : xmin + w]
                    face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
                    face_image = cv2.resize(face_image, (72, 72), interpolation=cv2.INTER_CUBIC)
                    
                    result = face_mask.predict(face_image)

                    if result[1] < 150:
                         color = (0, 255, 0) if LABELS[result[0]] == "Seguro" else (0, 255, 255)
                         if LABELS[result[0]] == "No-Seguro":
                              print('Descubrir Rostro')
                              #ser.write(b'N')
                              cv2.putText(frame, "{}".format(LABELS[result[0]]), (xmin, ymin - 15), 2, 1, color, 1, cv2.LINE_AA)

                         else:

                              faces_suspect = os.listdir('Sospechosos/')
                              for face in faces_suspect:
                                   if(os.path.isfile(os.path.join('Sospechosos/',face))):
                                        
                                        template = cv2.imread('Sospechosos/'+face)
                                        image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                                        template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
                                        res = cv2.matchTemplate(image_gray, template_gray, cv2.TM_SQDIFF)
                                        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
                                        min_thresh = (min_val + 1e-6) *1.5

                                        if(min_thresh == 0):
                                             pass
                                        else:
                                             #ser.write(b'N')
                                             color = (0, 0,255)
                                             print('Persona con antecedentes de asalto - NO SUBIR')   
                                             cv2.imwrite('Sospechosos/Sospechoso_{}.jpg'.format(contador_S),frame[xmin:xmin+w,ymin:ymin+h])
                                             cv2.rectangle(frame, (xmin, ymin), (xmin + w, ymin + h), color, 2)
                                             cv2.putText(frame, "{}".format(LABELS[2]), (xmin, ymin - 15), 2, 1, color, 1, cv2.LINE_AA)  
                              print('Persona No Sospechosa - Dejar Subir')
                              #ser.write(b'P')

                              
                         cv2.rectangle(frame, (xmin, ymin), (xmin + w, ymin + h), color, 2)
 

          cv2.imshow("Frame", frame)
          k = cv2.waitKey(1)
          if k == 27:
               break

cap.release()
cv2.destroyAllWindows()
#ser.close()