#otp generation
import random
import math
import smtplib#simple mail transfer protocol library


digits="0pooja@123456789"
OTP=""

for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
msg=OTP

s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("poojach207@gmail.com","ktku kdro bhgj gbnq")
user="poojach207@gmail.com"
emailid=input("enter the mail which you want to send otp")
s.sendmail(user,emailid,msg)

while True:
    a=input("enter the otp")
    if a==OTP:
        print("otp is correct")
    else:
        print("wrong otp")






    
                
