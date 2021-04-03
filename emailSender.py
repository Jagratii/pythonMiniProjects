import smtplib 
from email.message import EmailMessage

sender_email = input("Enter your e-mail : ")
rec_email = input("Enter reciever's e-mail : ")
password = input("Enter your password : ")
message = input("Enter your message")

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, password)
print("Logged in successfully")
server.sendmail(sender_email, rec_email, message)
print("E-mail was sent sucessfully")