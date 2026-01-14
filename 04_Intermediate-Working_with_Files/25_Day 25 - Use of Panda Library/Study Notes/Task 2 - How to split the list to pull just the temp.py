# Todo: Another way to do it- more clean using the inbuilt codes.
import csv
with open("weather_data.csv", mode = "r") as dataset:
    csv_data = csv.reader(dataset)
                # Creates an object that can be looped through
        # Todo: Getting out a list of temperatures
    temperature = []
    for row in csv_data:
        temperature_number = row[1]
        if temperature_number== "temp":
            continue
        else:
            final_temp= int(temperature_number)
            temperature.append(final_temp)
    print( temperature)
