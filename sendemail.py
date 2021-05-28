import smtplib
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

s = smtplib.SMTP('smtp.gmail.com', 587)

def sendmail(TEXT,email,SUBJECT,tt):
    
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    
    s.login("lokesh12215123@gmail.com", "Lokesh12215123@")
    message  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    s.sendmail("lokesh12215123@gmail.com", email, message)
    
    
    
    message  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    s.sendmail("lokesh12215123@gmail.com", "lokesh12215123@gmail.com", tt)
    s.quit()
    