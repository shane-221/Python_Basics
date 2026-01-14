import pandas
import pandas as pd
from pandas.core.internals.construction import dataclasses_to_dicts

# Todo: reading the CSV File.
            #  Todo 1: All functionalities are optional except for the path that leads to the csv file
data = pd.read_csv( "weather_data.csv")
print(data)

            #  Todo 2:Can print out the data for a column
                ## Assumes that the first name of all the rows will be the names.
print(data["temp"])
                ## Can also use the code on line 13 because panda already attributes the first item to be the list name
data.temp

            # Todo 3: Converting it into a dictionary
data_dict = data.to_dict()
print( data_dict)

            # Todo 4: Converting the series into a list
data_list  = data["temp"].to_list()
print (data_list)

            # Todo 5: Working out the mean of temperature series
data_temp_average= data["temp"].mean()
print( data_temp_average)

            # Todo 6: Pulling the maximum value of the temperatures.
data_temp_max =  data["temp"].max()
print( data_temp_max)

            # Todo 7: How to access the rows
data_on_Monday= data[data.day== "Monday"]
# print(data_on_Monday)

            # Todo 8: Which row has the highest temperature
highest_temp_day =  data[data.temp ==data.temp.max()]
print(highest_temp_day)

            # Todo 9: Accessing other variables from a saved row.
print(highest_temp_day.condition)

            # Todo 10 : Pulling the temperature for Monday and convert it to Fahrenheit
monday = data[ data.day == "Monday"]
                    # Pulling the tempo for Monday
value  = monday.temp[0]
                    # Making the conversion to Fahrenheit
final_value =  (value*9/5)+32
print(final_value)

            # Todo 11 : Creating a dataframe from scratch
weather_data = {
    "Monday": {"temp_c": 12, "condition": "Sunny"},
    "Tuesday": {"temp_c": 8, "condition": "Rainy"},
    "Wednesday": {"temp_c": 10, "condition": "Cloudy"}
                }
data = pandas.DataFrame(weather_data)

            # Todo 12: Can also convert the data frame into a csv file
data.to_csv("new_data.csv")
                # Input is the path where you want to save this file.