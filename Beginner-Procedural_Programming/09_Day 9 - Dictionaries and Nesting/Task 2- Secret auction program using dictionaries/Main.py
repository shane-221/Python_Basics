        # TODO 1: Initialisation of inputs
from Logo import logo
import time
def clear_screen():
    print("\n"*50)
auction={}
        #   TODO 2: Opening scene
print(f"""
            {logo}
            Welcome to the auction!
            """)
        #   TODO 3: create the flow chart
continue_game=True
while continue_game:
            #   todo: get the inputs for name and bid
    name= input("What is your name?")
    bid = int(input("What is your bid?"))
            #   todo: place the name and bid into the auction function
    auction[name]=bid
            #   todo: ask if they would like to keep going to make sure there isn't an infinite loop.
    clear_screen()
    end_game= input("Are there any other bidders?Yes or No?").lower()
    if end_game=="no":
        continue_game=False
    elif end_game=="yes":
        continue_game==True
                                # Redundant statement - but useful when building it to see the flow of logic.
    else:
        print("Please choose Yes or No.")
        end_game = input("Are there any other bidders?Yes or No?").lower()
        # TODO 4: Checking who won

highest_value=["name", 0]
                # Use a list instead of  dictionary since its easier to manipulate the key value term.
for i in auction:
    if  auction[i]>highest_value[1]:
        highest_value[1]=auction[i]
        highest_value[0]=i
time.sleep(3)
print(f"The winner of the auction is {highest_value[0]} with {highest_value[1]} as the bid.")
