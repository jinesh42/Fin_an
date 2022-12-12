import smtplib
import ssl
from email.message import EmailMessage

email_sender = 'jain.jinesh220@gmail.com'
email_password = 'mpxgtxtegwmocull'
email_receiver = 'jain.jinesh220@gmail.com'


subject = 'Yearly Report!'
body = """
New report has come please check
"""

em=EmailMessage()
em['Subject'] = subject
em['From'] = email_sender
em['To'] = email_receiver
em.set_content(body)
with open('Expenses_by_year.pdf','rb') as fp:
    em.add_attachment(fp.read(),maintype='application',subtype='pdf', filename='Expenses_by_year.pdf')    
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())