import random

                    # TODO 1: Prepping the functions and variables
global Lives
Lives = 0
number_loop = True
game_working = True


def difficulty_function():
    difficulty = input(" Choose a difficulty. Type 'easy' or 'hard':").lower()
    return difficulty
                                                                             # Choosing the difficulty

def number_checker(lives, random_number_final) :
    global number_loop
    global game_working


    while number_loop:
        chosen_number = int(input("Please choose a number:"))
                                                                                # Need to account for cases where they mistype the cases. But haven't been
                                                                                ## taught how to do that
        if lives < 1:
            print("I'm sorry but you've lost the game!")
            number_loop = False
            game_working=False
            print(f" You have {lives} remaining!")
                                                                                # method 1 of loop breaking when lives become less than 1
        elif chosen_number > random_number_final:
            print(" You are too high!")
            lives -= 1
            print(f" You have {lives} remaining!")
                                                                                # What happens when the number is too high
        elif chosen_number < random_number_final:
            print("You are too low!")
            lives -= 1
            print(f" You have {lives} remaining!")
                                                                                # What happens when the number is too low
        elif chosen_number == random_number_final:
            print("Well done, that's the correct number")
            number_loop = False
            game_working= False
            print(f" You have {lives} remaining!")
                                                                                # What happens when you get to the correct number
        # TODO 2: Begin the game
                #TODO 1a: Opening the game up

def game_start():
    print("""Welcome to the number guessing game!
            I'm thinking of a number between 1 and 100. 
        """)
                                                                                # Random number gets chosen every time
    random_number = random.randint(1, 100)

    # TODO 1b: Choosing difficulty and running it as a loop in case of the else statement.

    while game_working:
        global Lives
        difficulty_choice = difficulty_function()
                                                    # This means that the function will only run once.
                                                    # Choice of difficulty
                                                        ## In essence the game working loop is for the difficulty top account for input other than easy or hard
                                                        ### The number_loop lopp is for the program to continue until either they lose the game or win the game.
        if difficulty_choice == "easy":
            Lives = 10
            number_checker(lives=Lives, random_number_final=random_number)

        elif difficulty_choice == "hard":
            Lives = 5
            number_checker(lives=Lives, random_number_final=random_number)

        else:
            print(" Please choose one of the options")
game_start()

                        # TODO 3: Replay the game once the loops finish.
keep_running= True
while keep_running:
    restart_game = input("Would you like to play the game again? Please choose Y or N")
    if restart_game == "y":
        game_start()
    elif restart_game == "n":
        print("Thanks for playing my game!")
        keep_running= False
    else:
        print(" That's not one of the options!")

                # This is an infinite/ recursive loop if they keep choosing the wrong one.





