import smtplib
with smtplib.SMTP('smtp.gmail.com',587) as smtp:
 smtp.ehlo()
 smtp.starttls()
 smtp.ehlo()

 smtp.login("mysmart99mail@gmail.com","cjtbiwpobyyqvcpi")

 subject='Grab dinner!!'
 body='hey there!!'
 
 msg=f'Subject: {subject}\n\n{body}'

 smtp.sendmail('mysmart99mail@gmail.com','mysmart99mail@gmail.com',msg)