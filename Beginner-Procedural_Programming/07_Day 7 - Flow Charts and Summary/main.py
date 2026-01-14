        #  Todo: Pre conditions prep
import random
from word_list import word_list
from ASCI import stages,logo

        # TODO: Randomly choose a word from the word list and assign it to the chosen word. Then print it.
chosen_word = random.choice(word_list)

        # TODO : Create placeholders
display=[]
for x in range( 0, len(chosen_word)):
    display += "_"
                # Placing display as a list because string does not allow for assignment and append.
                ## Makes the code more complex.

        # TODO: Initial conditions
lives = 6
stage_pos=0
guessed_letters=[]

        # Todo: Opening set of outputs
print(f"""
        Welcome to Hangman. We have randomly  chosen a word. You have 6 lives until the game ends. 
{logo}
{stages[stage_pos]}
{display}
            There are {len(chosen_word)} letters in your word. 
            Chosen word:{chosen_word}
        """)

        # TODO: Ending of the game
game_end=False

        # TODO: Process of working out if the letter is in the word and applying the lives situation to it.
while not game_end:
    guess_letter =  input("         Please choose the letter: \n")
    guess_letter= guess_letter.lower()

            # TODO: Check if the letter user guessed is one of the letters in the chosen word.
                    # TODO: Initial check to see if is already                                                                                                                                                                          chosen
    if guess_letter in guessed_letters:
        print("Please choose another value. You've already chosen this once")
                    # TODO: What happens when the letter is in the word
    elif guess_letter in chosen_word:
        for i in range(0,len(chosen_word)):
            if  guess_letter==chosen_word[i]:
                display[i] = guess_letter
                guessed_letters.append(guess_letter)

        print(stages[stage_pos])
        print(" That's a correct letter!")
        print(display)

                    # TODO: What happens when the letter is not in the word.
    elif guess_letter not in chosen_word:
        lives=lives-1
        stage_pos=stage_pos+1
        guessed_letters.append(guess_letter)
        print(f"You've guessed {guess_letter}. That's not the correct letter!")
        print(f"You have {lives} life left! ")
        print(stages[stage_pos])

    # TODO: Ending of the game
    if lives == 0:
        game_end = True
        print(" Im sorry but you have not guessed the letters correctly!")
        print( "The word was {chosen_word}")

    if "_" not in display:
        print("Well Done! You've guessed the word correctly.")
        game_end = True
