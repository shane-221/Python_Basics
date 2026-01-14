import requests

MY_LAT=51.507351
MY_LNG = -0.127758


# Todo: Parameters
parameters ={
        "lat":MY_LAT,
        "lng":MY_LNG,
        "formatted": 0
}



# Todo: Need to provide the required parameters
response = requests.get(url= "https://api.sunrise-sunset.org/json", params= parameters)
response.raise_for_status()


# Todo: Getting the data as a JSON Format
data= response.json()

# Todo:Get the sunrise and the sunset data
sunrise= data["results"]["sunrise"]
sunset = data ["results"]["sunset"]



# Todo: split the sunrise data and sunset data
print((sunrise.split("T")[1].split(":")))


# Todo: Print the data
print(sunset)

    # Can use the date time function to make the comparison to work out the difference betwen now and sunrise + sunset