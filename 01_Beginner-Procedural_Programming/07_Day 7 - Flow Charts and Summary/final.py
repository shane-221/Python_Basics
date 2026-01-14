       # Pre conditions prep
import random
from word_list import word_list


        # TODO: Randomly choose a word from the word list and assign it to the chosen word. Then print it.
chosen_word = random.choice(word_list)
print( chosen_word)
        # TODO : Create placeholders
letters=len(chosen_word)
display=""
for x in range( 0, letters):
    display += "_"
                # Placing display as a list because string does not allow for assignment.
                ## Makes the code more complex.
print(display)
        # TODO: Ask the user to guess the letter and assign their answer to a variable called guess. Make guess lowercase.


guess_letter =  input(" Choose letter please")
guess_letter= guess_letter.lower()

     # TODO 3: Check if the letter user guessed is one of the letters in the chosen word.
for i in chosen_word:
    if i==guess_letter:
        display+=guess_letter
    else:
        display +="_"
print(display)
