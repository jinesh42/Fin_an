import smtplib 
from email.mime.text import MIMEText
import ssl

sender ='jain.jinesh220@gmail.com'
password='mpxgtxtegwmocull'
receiver=['jain.jinesh220@gmail.com','jain.jinesh1996@outlook.com']

body='''
Hello world!!!\nIt is very beautiful place.
'''

msg=MIMEText(body)
msg['Subject']= 'First Email'
msg['From']='jain.jinesh220@gmail.com'
msg['To']="jain.jinesh220@gmail.com,jain.jinesh1996@outlook.com"

context=ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
    smtp.login(sender,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    print("Email sent Successfully")