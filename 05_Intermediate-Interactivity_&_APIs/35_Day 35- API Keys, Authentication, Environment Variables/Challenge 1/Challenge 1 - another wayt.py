# Same thing as before( challenge 1), but you pull the endpoints and then pull the separate variables into a new
## dictionary. Need to use the exact name of the exact parameters.

# Cnt parameter produces the daya for the next 12 hours

import requests



#-------------------------------------------------- Constants----------------------------------------------------------#
OWM_ENDPOINT= "https://api.openweathermap.org/data/2.5/forecast?"
API_KEY= "3e24f9a482c9a6d6cd7749d499de293e"

weather_paramas={
    "lon" : -0.127758,
    "lat" : 51.507351,
    "appid" : API_KEY,
    "cnt": 4
   }

#------------------------------------------------- Request the data----------------------------------------------------#
response =requests.get(url=OWM_ENDPOINT, params=weather_paramas )
response.raise_for_status()
print(response)

weather_data = response.json()
print (weather_data)