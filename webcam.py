import cv2
import sys

cascPath = "C:\\Users\\hemal\\Desktop\\Webcam-Face-Detect-master\\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,               
        minSize=(10, 10),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    #print(type(faces))

    print(faces)
    for (x, y, w, h) in faces:
        print('working')
        filename = 'faces/ddd.jpg'
        cv2.imwrite(filename, frame)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    print('stop')
    
    
    cv2.imshow('Video', frame)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()
