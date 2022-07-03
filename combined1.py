from deepface import DeepFace
import cv2
import sys
import smtplib
import imghdr
import threading
from email.message import EmailMessage
import os

flag=0
count=0
frame=0
def web_cam():
    global flag,count,frame
    cascPath = "C:\\Users\\hemal\\Documents\\GitHub\\face-detection\\haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)

    video_capture = cv2.VideoCapture(0)
    f=0
    down=0
    while True:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        #if flag==0:
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,               
            minSize=(90, 90),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
            
        for (x, y, w, h) in faces:
            f=1
            filename = 'faces/ddd.jpg'
            cv2.imwrite(filename, frame)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            count=count+1

        if flag==0 and f==1 and down>100:    
            flag=1
            t1 = threading.Thread(target=verify, args=())
            down=0
            t1.start()
            #verify()
            #t1.join()

        down=down+1
        f=0
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()

def verify():
    global flag,count,frame
    models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib", "SFace"]
    detectors = ["opencv", "ssd", "mtcnn", "dlib", "retinaface"]
    metrics = ["cosine", "euclidean", "euclidean_l2"]
    

    for file in os.listdir("stranger"):
        print("\tStranger : ",file)
        verification=DeepFace.verify(
        img1_path="faces\\ddd.jpg",
        img2_path="stranger\\"+file,
        model_name = models[-2], distance_metric = metrics[-2],
        detector_backend = detectors[0],
        enforce_detection=False)
        if verification.get('verified')==True:
            print("%%%%%%%%%%%%%%%%% Stranger again no email sent %%%%%%%%%%%%%%%%")
            print(count)
            flag=0
            count=0
            return
    try:
        for file in os.listdir("owners"):
            print("\tOwners : ",file)
            verification=DeepFace.verify(
            img1_path="faces\\ddd.jpg",
            img2_path="owners\\"+file,
            model_name = models[-2], distance_metric = metrics[-2],
            detector_backend = detectors[0],
            enforce_detection=False)

            if verification.get('verified')==True:
                print("%%%%%%%%%%%%%%%%% Access Granted %%%%%%%%%%%%%%%%")
                filename = 'owners/001.jpg'
                cv2.imwrite(filename, frame)
                break
    except:
        print("%%%%%%%%%%%%%%%%%% No face deteacted %%%%%%%%%%%%%%%")
    
    
    print("\t\t",verification.get('verified'))
    if verification.get('verified')==False:
        print('mail sending')
        filename = 'stranger/star.jpg'
        cv2.imwrite(filename, frame)
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
