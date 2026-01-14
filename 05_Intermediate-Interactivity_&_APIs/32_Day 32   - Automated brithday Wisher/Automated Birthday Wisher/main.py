##########################################---Hard Starting Project---##################################################
##1. Update the birthdays.csv with your friends & family's details.
##HINT: Make sure one of the entries matches today's date for testing purposes.

##2. Check if today matches a birthday in the birthdays.csv
##HINT 1: Only the month and day matter.
##HINT 2: You could create a dictionary from birthdays.csv that looks like this:
##birthdays_dict = {
#     (month, day): data_row
# }
##HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
##if (today_month, today_day) in birthdays_dict:

#----------------------------------------------------Set-up------------------------------------------------------------#
import pandas as pd
import datetime as dt
import random
import smtplib
import time

game_on = False
my_email= "shanemathew988@gmail.com"
password ="ysma qkrh kwdx joxx"





#-------------------Place all the code into a while loop so it runs then closes at the right time----------------------#


def send_birthday_emails():
                #------------------Get the Birthday CSV and check for month and days-------------------------#
    data = pd.read_csv("./birthdays.csv")
    # Todo: creates the items in the csv file into a list of dictionaries.
    dataset= data.to_dict(orient= "records")

    # Todo: running the check for months and days that match today
    today_month = dt.datetime.now().month
    today_day = dt.datetime.now().day

    check_dataset_today={
                        (record["month"], record["day"] ):dataset.index(record)
                        for record in dataset
                        if record["day"]==today_day and record["month"]==today_month
                        }

    # Todo: create a list of dictionaries with all the relevant values to make it easier to use later+ allows scalability
    final_birthday_list=[]
    for i in check_dataset_today:
        final_birthday_list.append(dataset[check_dataset_today[i]])
    ### Conclusion: worked out a list of dictionaries that contain each person data###

                #-----------Only case if the Birthday is true then pick a random template-----------#
    random_template=["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    chosen_template= random.choice(random_template)
    chosen_type= chosen_template

    # Todo: Looking through each of the items in the list
    for i in final_birthday_list:

        # Todo: Open the template + convert into a string + create a new content file
        with open(f"./letter_templates/{chosen_type}", mode="r") as template:
            content= template.read()
            new_content = content.replace ("[NAME]", i["name"])

        # Todo: create a new file with the newly created string file
        with open(f'./Final_Letters/Email_for_{i["name"]}', mode = "w") as template:
            template.write(new_content)

                #---------------Send the email to them at a certain time-----------------------#
    # Todo: Preping the variables I will be using.


        with smtplib.SMTP("smtp.gmail.com") as connection:
            # Todo: Basics of preparing to send
            connection.starttls()
            connection.login( user = my_email, password = password)
            # Todo: Getting the content into string format to embedd
            with open(f'/Final_Letters/Email_for_{i["name"]}', mode = "r") as final_file:
                email_content = final_file.read()

            connection.sendmail(
                                from_addr= my_email,
                                to_addrs= i["email"],
                                msg =f"Subject: Happy Birthdayy!!\n\n{email_content}"
                                )
    check_function()
#-------------------------------- Starting the Game loop when it hits a certain time-----------------------------------#

def check_function():
    while True:
        now = dt.datetime.now()
        if now.hour==9 and now.minute==0:
            send_birthday_emails()
            break
        time.sleep(30)

check_function()