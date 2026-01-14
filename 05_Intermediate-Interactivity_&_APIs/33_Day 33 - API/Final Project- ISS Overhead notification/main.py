import requests
from datetime import datetime
import smtplib


#----------------------------------------------Constants---------------------------------------------------------------#
MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

my_email= "shanemathew988@gmail.com"
password ="ysma qkrh kwdx joxx"

#----------------------------------------------- API Request ----------------------------------------------------------#
# Todo : Raise the request  for the ISS Position
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

# Todo: Raise the request for your position
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
    # Todo' Pull the hour in which the sun rises and sets
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(f"sunrise:{sunrise}")
print(f"sunset:{sunset}")
#-----------------------------------Checking against the requests to send email----------------------------------------#
time_now = datetime.now()
# Todo: when it is dark
if  (time_now.hour> sunset) or (time_now.hour<sunrise):
    # Todo: The ISS is close to my location
    if (MY_LAT-5<= iss_latitude <= MY_LAT + 5) and  (MY_LONG- 5<= iss_longitude <= MY_LONG+5):
        # Todo: send email if its close
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(
                                user = my_email,
                                password = password
                            )
            connection.sendmail(
                                from_addr=my_email ,
                                to_addrs= my_email,
                                msg ="Subject: ISS above you!\n "
                                     "Please look up! The ICC Space station is right above you! "
            )




# BONUS: run the code every 60 seconds.



