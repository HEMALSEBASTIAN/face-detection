#Create Message Box in Python GUI Application  
import cv2
import sys

cascPath = "/Users/liyajohny/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    #converting image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,    #for resizing the image
        minNeighbors=5,     # Higher value results in fewer detections but with higher quality              
        minSize=(256, 250), #minimum size if the face to be detected
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    
    for (x, y, w, h) in faces:
        print('working')
        filename = 'faces/ddd.jpg'
        cv2.imwrite(filename, frame)                                #saving captured image
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)    #drawing rectangular box around images
        cv2.putText(frame, 'Acces granted', (550,550), cv2.FONT_HERSHEY_COMPLEX, 1,(0, 255, 0), 3)
    print('stop')
    
    
    cv2.imshow('Video', frame)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()
