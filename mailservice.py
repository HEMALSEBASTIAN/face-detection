import smtplib
smtplibObj = smtplib.SMTP("smtp.gmail.com",587)
smtplibObj.ehlo()
smtplibObj.starttls()
smtplibObj.login("mysmart99mail@gmail.com","cjtbiwpobyyqvcpi")
smtplibObj.sendmail("mysmart99mail@gmail.com","mysmart99mail@gmail.com","Subject:Home Footage\nHello there!!An unknown visitor is at your door!!")
smtplibObj.quit()
#nfhjnhdfkj