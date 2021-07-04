import smtplib

# log in to the email you're sending from (not recommended to use your personal email)
sender = ''
password = ''

#  email address of your enemy
target = ''

session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender, password) #login with mail_id and password

message = 'TEST'

session.sendmail(sender, target, message)
session.quit()