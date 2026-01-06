import smtplib
import glob
import os
from email.message import EmailMessage


def latest_output_file():
    list_of_files = glob.glob('../Output_Emails/*')
    latest_file = max(list_of_files, key=os.path.getmtime)      # From Stack overflow Pulls the file path of the most recent file
    if not latest_file:
        print(" There is a problem with the Output HTML file")
        return None
    else:
        with open(latest_file, encoding="utf-8") as file:
            output = file.read()
            return output

class Email:
    def __init__(self, **kwargs):
        self.to_email =kwargs["to_email"]
        self.from_email = kwargs["from_email"]
        self.password =kwargs["password"]
        self.host =kwargs["host"]

    def send_email(self):
        # Using the message Module:
        msg = EmailMessage()
        msg.set_content(latest_output_file(), subtype="html")

        msg['Subject'] = 'There is an update on the stocks you are tracking!'
        msg['From'] = self.from_email
        msg['To'] = self.to_email

        # Connects the smtplib client session to the host
        connection = smtplib.SMTP(self.host)#
        # message is encrypted
        connection.starttls()
        #Login phase
        connection.login(user=self.from_email, password =self.password)
        # Sending email
        connection.send_message(msg)
        # Close the connection
        connection.quit()





