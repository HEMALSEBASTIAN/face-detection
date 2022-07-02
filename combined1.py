from deepface import DeepFace
import cv2
import sys
import smtplib
import imghdr
import threading
from email.message import EmailMessage

flag=0
count=0
def web_cam():
    global flag,count
    cascPath = "C:\\Users\\hemal\\Documents\\GitHub\\face-detection\\haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)

    video_capture = cv2.VideoCapture(0)
    
    while True:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        #if flag==0:
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,               
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
            
        for (x, y, w, h) in faces:
            
            filename = 'faces/ddd.jpg'
            cv2.imwrite(filename, frame)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            count=count+1

        if flag==0:    
            flag=1
            t1 = threading.Thread(target=verify, args=())
            t1.start()
            #verify()
            #t1.join()

        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()

def verify():
    global flag,count
    models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib", "SFace"]
    detectors = ["opencv", "ssd", "mtcnn", "dlib", "retinaface"]
    metrics = ["cosine", "euclidean", "euclidean_l2"]
    verification=DeepFace.verify(
    img1_path="faces\\ddd.jpg",
    img2_path="faces\\MEH.jpg",
    model_name = models[1], distance_metric = metrics[2],
    detector_backend = detectors[0],
    enforce_detection=False)
    #print("\t\t",verification)
    print("\t\t",verification.get('verified'))
    if verification.get('verified')==False:
        print('mail sending')
        email_send()
    print(count)
    flag=0
    count=0


def email_send():
    msg=EmailMessage()
    msg['Subject']='Home Security'
    msg['From']='mysmart99mail@gmail.com'
    msg['To']='hemalsebastian123@gmail.com'
    msg.set_content('An unknown face has been recognized at your doorlock!Image attached!!')
    
    with open('C:\\Users\\hemal\\Desktop\\Webcam-Face-Detect-master\\faces\\ddd.jpg','rb') as f:
        file_data=f.read()
        file_type=imghdr.what(f.name)
        file_name=f.name

    msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)

    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login("mysmart99mail@gmail.com","cjtbiwpobyyqvcpi")
        
    #image added
    #sfv
        smtp.send_message(msg)
    print("mail sent")
    


web_cam()
