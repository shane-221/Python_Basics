import random                                                                                                                                                                                                                                          # Need to fix what happens when the user chooses things other than a or B
from game_data import data
from Art import logo,vs

def check_function(comparison_a, comparison_b,):
    global run_game, total_score
    print(f"Compare A: {comparison_a['name']},a {comparison_a['description']}, from {comparison_a['country']}")
    print(vs)
    print(f"Compare B: {comparison_b['name']},a {comparison_b['description']}, from {comparison_b['country']}")

    correct_answer = ""
    if comparison_a["follower_count"] > comparison_b["follower_count"]:
        correct_answer = "a"
    elif comparison_b["follower_count"] > comparison_a["follower_count"]:
        correct_answer = "b"

    user_choice = input("Who has more followers? Type A or B:").lower()

    while user_choice not in ["a", "b"]:                                                                                            # From copilot But useful to do.
        user_choice = input("Invalid choice. Please type A or B: ").lower()

    if user_choice == correct_answer:
        print("That's the correct answer")
        total_score += 1
        print(f"Score:{total_score}")

    else:
        print("That's wrong ")
        print(f"Your final score is:{total_score}")
        run_game=False


total_score = 0
repeat_game=True                                                                                                         #   TODO 1: Run the first set of iteration + Running of the xtra lopp from the finish
while repeat_game:                                                                                                                     # Todo 1a: Pull the random choice from the list
    print(f"""
        {logo}
        Welcome to the Higher or Lower game! 
        Please choose the options that has the higher
         level of followers on instagram. 
        """)
    chosen_items=[]
    run_game = True
    while run_game:
        comparison_1 = random.choice(data)
        comparison_2 = random.choice(data)
        chosen_items.append(comparison_1)
        chosen_items.append(comparison_2)

        if comparison_1 not in chosen_items and comparison_2 not in chosen_items:                                                               # Todo 1b: Then offer the comparisons + Check if they are in the list
            check_function(comparison_a=comparison_1, comparison_b=comparison_2)
                                                                                                                                        # Todo 1c: Choose another two random ones since the first two has already been chosen and
                                                                                                                                        ## deposited in the chosen items list
        else:
            comparison_3 = random.choice(data)
            comparison_4 = random.choice(data)
            chosen_items.append(comparison_3)
            chosen_items.append(comparison_4)

            check_function(comparison_a=comparison_3, comparison_b=comparison_4)
                                                                                                                                        # Todo 1d: Chance to redo the game if they need
    restart_game = input("Would you like to play the game again?Y or N ").lower()
    if restart_game == "y":
        repeat_game = True
        total_score=0
    else:
        repeat_game = False









