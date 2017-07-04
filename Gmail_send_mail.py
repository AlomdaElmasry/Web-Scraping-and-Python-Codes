import smtplib


username = raw_input("Enter your EmailID : ")
password = raw_input("Enter your password : ")
receiver = raw_input("Enter the Email ID of the receiver : ")

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(username, password)

msg = raw_input("Enter the message : ")

for i in range(0,20):
    s.sendmail(username, receiver, msg=msg)

s.quit()
