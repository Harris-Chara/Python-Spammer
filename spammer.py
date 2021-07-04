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

message = MIMEMultipart()
message['Subject'] = "I am a spam email"
message['From'] = sender
message['To'] = target
body = 'I am spam'

bodyText = MIMEText(body)
message.attach(bodyText)

session.sendmail(sender, target, message.as_string())
session.quit()