import smtplib

#------------------------------------------ variables------------------------------------------------------------------#
my_email= "shanemathew988@gmail.com"
password ="ysma qkrh kwdx joxx"
to_email="shanemathew98--@outlook.com"

#------------------------------------------- Steps for the code--------------------------------------------------------#
connection  = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user= my_email, password= password)
connection.sendmail(from_addr=my_email,
                    to_addrs= to_email,
                    msg="Subject:Hello\n\n This is the mbody of my email"
                    )
connection.close()
