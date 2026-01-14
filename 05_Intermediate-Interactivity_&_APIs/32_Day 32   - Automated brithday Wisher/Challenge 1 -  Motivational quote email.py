##---------------------------------------------Task--------------------------------------------------------------------#
##
## Email ourselves a motivational quote if it is a specific day and time
##
##--------------------------------------------Constants and Variables--------------------------------------------------#
import random
import datetime as dt
import smtplib

my_email= "shanemathew988@gmail.com"
password ="ysma qkrh kwdx joxx"
to_email="shanemathew98--@outlook.com"

#----------------------------- Extract a list of items and random choice quote-----------------------------------------#
# Todo; Opening the file
with open ("./quotes.txt", mode="r") as file:
    lines = file.read()
    # Todo: applying the splitlines function to get a list of items
    items = lines.splitlines()

    # Todo: randomly choosing an item from the list
    chosen_quote = random.choice( items)

#---------------------------------------------------Matching for the day ----------------------------------------------#
now  = dt.datetime.now()
if now.hour==9 and now.minute==0:
    with smtplib.SMTP("smtp.gmail.com") as connection :
        connection.starttls()
        connection.login(user = my_email, password=password)
        connection.sendmail( from_addr= my_email,
                             to_addrs= to_email,
                             msg =f"Subject:Good morning!!!\n\n\n{chosen_quote}"
                             )