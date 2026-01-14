    # Import of relevant modules
import random
from Support_Files import letters, numbers,symbols
    # Opening statements
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
    # Choice of Letters, symbols and numbers
final_setup=[]
for i in range(1,nr_letters+1):
    final_setup+= random.choice(letters)
for i in range(1,nr_symbols+1):
    final_setup+= random.choice(symbols)
for i in range(1,nr_numbers+1):
    final_setup+= random.choice(numbers)

    # Rearrange the order in the list  for randomisation
random.shuffle(final_setup)
    # Converting the list into a string:
a_string=""
for x in final_setup:
    a_string+=x
    # Final Output
print(f"The password should be: {a_string}")



