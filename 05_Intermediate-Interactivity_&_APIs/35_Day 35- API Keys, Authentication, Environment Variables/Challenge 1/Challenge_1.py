import requests
#-------------------------------------------------- Constants----------------------------------------------------------#
LONGTITUDE =-0.127758
LATITUDE = 51.507351
API_KEY= "3e24f9a482c9a6d6cd7749d499de293e"
#------------------------------------------------- Request the data----------------------------------------------------#
response =requests.get(url= f" https://api.openweathermap.org/data/2.5/forecast?lat={LATITUDE}&lon={LONGTITUDE}&appid={API_KEY}")
print(response)

data= response.json()
print (data)