import requests
#------------------------------------------Constants-------------------------------------------------------------------#
AMOUNT= 30
#------------------------------------------API Request-----------------------------------------------------------------#
response= requests.get(url=f"https://opentdb.com/api.php?amount={AMOUNT}&type=boolean")
response.raise_for_status()
data = response.json()
question_data =[i for i in data["results"]]
