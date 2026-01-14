import pandas as pd


# Todo: Reading the data:
dataset =  pd.read_csv("Squirrel_Data.csv")

    # Todo: breaking up the dataset by colour and column:
grey = dataset[ dataset["Primary Fur Color" ]== "Gray"]
cinnamon = dataset[ dataset["Primary Fur Color" ]== "Cinnamon"]
black = dataset[ dataset["Primary Fur Color" ]== "Black"]

    # Todo: Adding up the columns:
number_grey= len(grey)
number_cinnamon= len(cinnamon)
number_black = len(black)

    # Todo: converting the colours into a dictionary and building them into a dataframe.
            #  Todo: creating the dictionary to be used.
Fur_colour_data ={
    "Fur Colour":["Gray", "Cinnamon", "Black"],
    "Number":[number_grey, number_cinnamon, number_black]
                 }
            # Todo: adjusting the dataset for dataframe

data = pd.DataFrame(data = Fur_colour_data)
print( data)

    # Todo: converting the file into a csv file.
data.to_csv("Fur_Colour_Data.csv")