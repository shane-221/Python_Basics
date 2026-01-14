# Todo: On way to do it but it will be messy and visually unappealing.
with open("weather_data.csv", mode= "r") as dataset:
    datasets = dataset.readlines()
    print(datasets)