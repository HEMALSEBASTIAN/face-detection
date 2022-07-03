import smtplib
import imghdr
from email.message import EmailMessage
 


msg=EmailMessage()
msg['Subject']='Home Security'
msg['From']='mysmart99mail@gmail.com'
msg['To']='mysmart99mail@gmail.com'
msg.set_content('An unknown face has been recognized at your doorlock! Image attached!!')

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