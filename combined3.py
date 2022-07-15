from asyncio.windows_events import NULL
import cv2
import smtplib
import imghdr
import threading
import os
import sys
from deepface import DeepFace
from email.message import EmailMessage
from PIL import Image
from jinja2 import pass_environment
from twilio.rest import Client
import tkinter as tk
from attr import s
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

flag=0
count=0
frame=0
frame1=NULL
LINK=""
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
        try:
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
                while(True):
                    try:
                        t1 = threading.Thread(target=verify, args=())
                        break
                    except:
                        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@verify")
                        pass
                down=0
                t1.start()

            #down=down+1
            no_face=0
            cv2.imshow('Video', frame)
            
        except:
            print("NO CAMERA")
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
    #comparing faces with last stranger's face so that email will not be sent again.
    try:
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
    except:
        print("Stranger comparing error")
    
    
    
    print('mail sending')
    filename1 = 'stranger/star.jpg'
    name[0]='Stranger'
    cv2.imwrite(filename1, frame)
    while(True):
        try:
            t2 = threading.Thread(target=email_send, args=())
            t3 = threading.Thread(target=gui, args=())
            t2.start()
            t3.start()
            break
        except:
            print(count)
            print("@@@@@@@@@@@@@@@@@@@@@@stranger")
            pass



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
    global LINK,flag
    account_sid = 'AC113e8a5153f1be30f820fe39994e56e1' 
    auth_token = '0673d0b62b5fd5f2c1870cccb822b4e7' 
    client = Client(account_sid, auth_token) 
    
    message = client.messages.create(  
                                messaging_service_sid='MGe7936fcc99775f919ae5dd2282a5bfb7', 
                                body='ALERT; Video call link :'+str(LINK),      
                                to='+918281565993 ' 
                            ) 
    
    print("sms sent")


def gui():
    print('the print')
    parent = tk.Tk()
    parent.geometry('300x100')
    print('the print1')

    frame1 = tk.Frame(parent)
    frame1.pack()
    print('the prin2')
    #T=tk.Text(frame,height=5,width=52)

    #l =tk.Label(frame, text = "Fact of the Day")
    #l.config(font =("Courier", 14))
    #t='Do you want to call?'

    """text_box= tk.Text(
        frame,
        height=5,
        width=10)"""
    text_lab=tk.Label(parent, text='Do You want to call?').place(x=40,y=10)

    #text_box.pack(side=tk.TOP)
    #text_box.insert('end',t)

    text_disp= tk.Button(frame1, 
                    text="Yes", 
                    command=lambda: fun(parent))

    #l.pack(side=tk.CENTER)
    #T.pack()
    text_disp.pack(side=tk.LEFT,padx=25, pady=40)

    exit_button = tk.Button(frame1,
                    text="No",
                    fg="black",
                    command=lambda: QUIT(parent))
    exit_button.pack(side=tk.RIGHT,padx=35,pady=40)
    print('the print4')
    parent.mainloop()


def QUIT(parent):
    global flag
    flag=0
    parent.quit()
    

def video_call(driver,mail_address,password):
    
    global LINK
    #driver.implicitly_wait(15)
    #click sign in button
    while(True):
        try:
            s=driver.find_element("xpath",'//*[@id="drawer"]/div/div[3]/div[1]/div/span[1]/a')
            s.click()
            print("sign in")
            break
        except:
            pass

    #adding a wait so that next page load
    driver.implicitly_wait(2)

    # input Gmail
    #input username
    while(True):
        try:
            username=driver.find_element("xpath",'//*[@id="identifierId"]')
            username.click()
            username.send_keys(mail_address)

            #click next
            next1=driver.find_element("xpath",'//*[@id="identifierNext"]')
            next1.click()
            print("enter user name")
            break
        except:
            pass
    
    #adding a wait so that next page load
    driver.implicitly_wait(2)
    # input Password
    while(True):
        try:
            pswd=driver.find_element("xpath",'//*[@id="password"]/div[1]/div/div[1]/input')
            pswd.click()
            pswd.send_keys(password)

            #click next
            next2=driver.find_element("xpath",'//*[@id="passwordNext"]')
            next2.click()
            print("password entered")
            break
        except:
            pass
    #adding a wait so that next page load
    driver.implicitly_wait(7)


    while(True):
        try:
            start_button=driver.find_element("xpath",'//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div[3]/div/div[1]/div[1]/div/button/span')
            start_button.click()


            call_button=driver.find_element("xpath",'//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div/ul/li[2]/span[3]')
            call_button.click()
            print("Call pressed")
            break
        except:
            pass
    

  
    
    while(True):
        try:
            driver.implicitly_wait(7)
            ex=driver.find_element("xpath",'//*[@id="ow3"]/div[1]/div/div[10]/div[3]/div[10]/div[3]/div[3]/div/div/div[1]/span/button')

            ex.click()

            link=driver.find_element("xpath",'//*[@id="ow3"]/div[1]/div/div[10]/div[3]/div[4]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]')
            print(link.text)
            LINK=link.text
            sms_send()
            break
        except:
            pass
    



    '''print("checking")
    while(True):
        try:
            driver.find_element("xpath",'//*[@id="yDmH0d"]/div[3]/div[2]/div/div[2]/div/div[2]/button[2]/span').click()
            print("admit")
            break
        except:
            continue'''



def fun(parent):

    global flag,count
    

    #video_capture.release()
    # assign email id and password
    mail_address = 'u1903092@rajagiri.edu.in'
    password = 'iamaHEROMAN@27!'


    # create chrome instance
    #opt = Options()
    opt=webdriver.ChromeOptions()
    opt.add_experimental_option('excludeSwitches', ['enable-logging'])
    opt.add_argument('--disable-blink-features=AutomationControlled')
    opt.add_argument('--start-maximized') #chrome browser will always open in full screen
    opt.add_argument('--disable-extensions') #disable all chrome extension

    #pass the arguments 1 to allow and 2 to block
    opt.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 2,
        "profile.default_content_setting_values.notifications": 1
    })

    #Gives path to chrome webdriver and loads classroom webpage
    driver = webdriver.Chrome(options=opt,service=Service(ChromeDriverManager().install()))

    driver.get(
    'https://apps.google.com/meet/?hs=197')
    video_call(driver,mail_address,password)


    is_closed=False
    while(not is_closed):
        try:
            isc=driver.find_element("xpath",'//*[@id="ow3"]/div[1]/div/div[10]/div[3]/div[10]/div[3]/div[3]/div/div/div[1]/span/button')
        except:
            is_closed=True
    #video_capture = cv2.VideoCapture(0)
    flag=0
    count=0
    parent.quit()


web_cam()
