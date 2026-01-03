import smtplib
import glob
import os
from email.mime.text import MIMEText



class Email:
    def __init__(self, **kwargs):
        self.to_email =kwargs["to_email"]
        self.from_email = kwargs["from_email"]
        self.password =kwargs["password"]
        self.host =kwargs["host"]

    def latest_output_file(self):
        list_of_files = glob.glob('../output_emails/*')
        latest_file = max(list_of_files, key=os.path.getmtime)      # From Stack overflow Pulls the file path of the most recent file
        if not latest_file:
            print("There are no output files")
            return None
        else:
            with open(latest_file,'r') as f:
                contents =f.read()
                # Smtp requuires all the code to be ascii--- so need to convert them all into characters it accepts.
                msg = MIMEText(contents, "html", "utf-8")
                return msg.as_string()


    def send_email(self):
        # Connects the smtplib client session to the host
        connection = smtplib.SMTP(self.host)#
        # message is encrypted
        connection.starttls()
        #Login phase
        connection.login(user=self.from_email, password =self.password)
        # Sending email
        connection.sendmail(from_addr=self.from_email,
                            to_addrs=self.to_email,
                            msg=self.latest_output_file()
                            )
        # Close the connection
        connection.close()





