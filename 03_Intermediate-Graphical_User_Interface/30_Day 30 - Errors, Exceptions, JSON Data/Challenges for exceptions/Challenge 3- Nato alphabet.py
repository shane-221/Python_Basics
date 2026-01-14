#----------------------------------------------Challenge---------------------------------------------------------------#
#Adjust this code block to reduce errors related o inputs that are not alphabets


#------------------------------------------------Code------------------------------------------------------------------#
import pandas as pd

dataset= pd.read_csv("nato_phonetic_alphabet.csv")



# Todo: Pulling out the letter to the code so that you have a neat dictionary to play with:
new_dataset = { row.letter:row.code for (index, row) in dataset.iterrows()}

# Todo: create a list of phonetic code words that the user inputs:
def user_data():
    game_run= True
    while game_run:
        user_input = input("Enter a word : ").upper()
        try:
            word_lists = [new_dataset[letter] for letter in user_input]
            print(f" Your code is:{ word_lists}")
            game_run= False
        except KeyError:
            print("Sorry only letters in the alphabet please!")


user_data()