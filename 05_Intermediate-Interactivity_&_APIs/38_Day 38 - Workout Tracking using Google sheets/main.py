#---------------------------------------Import modules-----------------------------------------------------------------#
import requests
from datetime import datetime
import os
#------------------------------------------Constants related to the individual-----------------------------------------#
# Todo : Parameters for the calorie API
user_query= input("Tell me which exercises you did?")
exercise_parameters = {
    "weight_kg" : 80,
    "height_cm" : 194,
    "age": 26,
    "gender": "male",
    "query": user_query
                    }

#-------------------------------------------Data that is important are important to the code---------------------------#
# tODO : Header data for the calorie request
headers ={
    "x-app-key" :os.environ.get("app-key"),
    "x-app-id": os.environ.get("app-id")
}
# Todo: Calorie constants
calorie_url = "https://trackapi.nutritionix.com/v2/natural/exercise"


# Todo: Sheet Constants
sheet_url= os.environ.get("sheet-url")
sheet_headers = {"Authorization" :os.environ.get("sheet_headers")}
#---------------------------------------------------Calorie request----------------------------------------------------#

# Todo: Request for the exercise parameters to get the calories and time
post_request = requests.post(url=calorie_url, headers=headers, json=exercise_parameters )
    # This is a response object. Then need to convert it into json to be usable
data =post_request.json()
print( data)
#--------------------------------------------sheetly request-----------------------------------------------------------#
# Todo: Parameter for the Sheetly api to put data into the excel sheet.
date_time_now= datetime.now()
date_now=date_time_now.strftime("%x")
time_now= date_time_now.strftime("%X")

sheet_params= {"sheet1":
                   {"date":date_time_now.strftime("%x"),
                    "time": date_time_now.strftime("%X"),
                    "exercise":data["exercises"][0]["user_input"],
                    "duration":data["exercises"][0]["duration_min"],
                    "calories":data["exercises"][0]["nf_calories"]
                }}

# Todo; Send request for the sheetly to google sheets
sheet_request= requests.post(url = sheet_url, json= sheet_params, headers = sheet_headers)
sheet_request.raise_for_status()

#
