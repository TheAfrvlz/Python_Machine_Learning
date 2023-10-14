import cv2
cap = cv2.VideoCapture(0)
contador = 0
while True:
    ret,frame = cap.read()
    
    s_frame = cv2.resize(frame,(40,40),cv2.INTER_AREA)

    cv2.imshow('captura',frame)

    if cv2.waitKey(1) & 0xFF == ord('p'):
        cv2.imwrite("Pistola/Nq/objeto_{}.jpg".format(contador),s_frame)
        print("objeto_{}.jpg".format(contador))
        contador = contador +1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()