import smtplib

# email information
sender_email = "rdgohil22@gmail.com"
sender_password = input(str("Enter your password: "))
recipient_email = "rajdipgohil22@gmail.com"
email_subject = "Data Analysis project"
message= """Hello sir 
                       
                   I would like to work with on Data Analysis Project
                   
                   Thanks and Regard
                   Rajdipsinh Gohil."""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, sender_password)
print("Login successful")
server.sendmail(sender_email, recipient_email, message)     
print("Email has been sent to", recipient_email)