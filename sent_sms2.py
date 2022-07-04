from twilio.rest import Client 
 
account_sid = 'AC113e8a5153f1be30f820fe39994e56e1' 
auth_token = '0673d0b62b5fd5f2c1870cccb822b4e7' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MGe7936fcc99775f919ae5dd2282a5bfb7', 
                              body='ALERT',      
                              to='+919846049228 ' 
                          ) 
 
print(message.sid)
