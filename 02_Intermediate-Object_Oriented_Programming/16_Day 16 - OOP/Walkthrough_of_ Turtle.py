from turtle import Turtle, Screen
from prettytable import prettytable, PrettyTable

# Need to import the class of the turtle class

timmy = Turtle()
    # From arrow to a turtle----attributes 
timmy.shape("turtle")
    # From Black colour to red colour---attributes
timmy.color("red")
    # Moving the turtle forward---methods:
timmy.forward(100)
    # Printing Timmy.
print(timmy)

# Importing packages to build tables
table= PrettyTable()
    # Using methods
table.add_column("Pokemon",["charmander", "pikachu",  "Squirtle"])
    # Using attributes
table.align ="c"
print(table)

# Exit on Click
my_screen= Screen()
my_screen.exitonclick()



