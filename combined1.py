import cv2
import smtplib
import imghdr
import threading
import os
import sys
from deepface import DeepFace
from email.message import EmailMessage
from PIL import Image
from twilio.rest import Client 

flag=0
count=0
frame=0
name=['']
def web_cam():
    global flag,count,frame,name
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)

    video_capture = cv2.VideoCapture(0)
    no_face=0  
    down=0
    x=0
    y=0
    while True:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #to detect faces in each frame
        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor=1.1,
            minNeighbors=5,               
            minSize=(200, 200),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        #to save image and draw rectangle when face is detected 
         
        for (x, y, w, h) in faces:
            filename = 'faces/ddd.jpg'
            no_face=1
            cv2.imwrite(filename, frame)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
            count=count+1
            down=down+1

        if no_face==0:
            name[0]=''

        cv2.putText(frame,name[0],(x,y-10),cv2.FONT_HERSHEY_SIMPLEX, 0.8,(0, 255, 0), 1)
        #to call verify function
        #call verify function only when the previous thread has finish execution
        if flag==0 and no_face==1 and down>100:    
            flag=1
            t1 = threading.Thread(target=verify, args=())
            down=0
            t1.start()

        #down=down+1
        no_face=0
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()


#function to perform face verification
def verify():
    global flag,count,frame,name
    models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib", "SFace"]
    detectors = ["opencv", "ssd", "mtcnn", "dlib", "retinaface"]
    metrics = ["cosine", "euclidean", "euclidean_l2"]
    

    #comparing faces with the owners of the house.
    try:
        for file in os.listdir("owners"):
            print("\tOwners : ",file)
            verification=DeepFace.verify(
            img1_path="faces\\ddd.jpg",
            img2_path="owners\\"+file,
            model_name = models[2], distance_metric = metrics[1],
            detector_backend = detectors[1],
            enforce_detection=False)

            if verification.get('verified')==True:
                name=file.split('.')
                nn=name[0]
                name[0]=nn[1:]
                print("%%%%%%%%%%%%%%%%% Access Granted %%%%%%%%%%%%%%%%")
                current_owner=cv2.imread('owners/'+file)
                filename = 'owners/'+'1'+file[1:]
                cv2.imwrite(filename, current_owner)
                flag=0
                count=0
                return
    except:
        print("%%%%%%%%%%%%%%%%%% No face deteacted %%%%%%%%%%%%%%%")


    print("%%%%%%%%%%%%%%%%%%Comparing stranger face%%%%%%%%%%%%%%%%%%")
    #comparing faces with last starnger's face so that email will not be sent again.
    for file in os.listdir("stranger"):
        print("\tStranger : ",file)
        verification=DeepFace.verify(
        img1_path="faces\\ddd.jpg",
        img2_path="stranger\\"+file,
        model_name = models[-2], distance_metric = metrics[-2],
        detector_backend = detectors[0],
        enforce_detection=False)
        if verification.get('verified')==True:
            name[0]='Stranger'
            print("%%%%%%%%%%%%%%%%% Stranger again no email sent %%%%%%%%%%%%%%%%")
            print(count)
            flag=0
            count=0
            return
    
    
    
    
    print('mail sending')
    filename1 = 'stranger/star.jpg'
    name[0]='Stranger'
    cv2.imwrite(filename1, frame)
    t2 = threading.Thread(target=email_send, args=())
    t3 = threading.Thread(target=sms_send, args=())
    t2.start()
    t3.start()
    #email_send()
    print(count)
    flag=0
    count=0



#function to send email notification to owner with stranger's image.
def email_send():
    msg=EmailMessage()
    msg['Subject']='Home Security'
    msg['From']='mysmart99mail@gmail.com'
    msg['To']='hemalsebastian123@gmail.com'
    msg.set_content('An unknown face has been recognized at your doorlock!Image attached!!')
    
    with open('stranger\\star.jpg','rb') as f:
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


def sms_send():
    account_sid = 'AC113e8a5153f1be30f820fe39994e56e1' 
    auth_token = '0673d0b62b5fd5f2c1870cccb822b4e7' 
    client = Client(account_sid, auth_token) 
    
    message = client.messages.create(  
                                messaging_service_sid='MGe7936fcc99775f919ae5dd2282a5bfb7', 
                                body='ALERT',      
                                to='+919497297856 ' 
                            ) 
    
    print(message.sid)

web_cam()