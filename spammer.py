import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# log in to the email you're sending from (not recommended to use your personal email)
sender = ''
password = ''

#  email address of your enemy
target = ''

session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(sender, password)

#Put in a numerical quantification of how much you hate the person
hatredQuantified = #<------ENTER NUMBER HERE-------

sentEmails = 1
while sentEmails <= hatredQuantified:
    message = MIMEMultipart()
    message['Subject'] = "I am spam email " + str(sentEmails) + " of " + str(hatredQuantified)
    message['From'] = sender
    message['To'] = target
    body = """Hello,
    I am an automated email dedicated to spamming you :)
    Hope you have a wonderful day!
    
    Kind Regards"""

    bodyText = MIMEText(body)
    message.attach(bodyText)

    session.sendmail(sender, target, message.as_string())
    print('Email Number ' + str(sentEmails) + ' has been sent')
    sentEmails = sentEmails + 1

session.quit()