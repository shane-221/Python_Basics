import random
import time

from Choices import game_choice

Choice=input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors\n")
Choice=int(Choice)

#Your choice
if Choice==0:
    print("You chose rock")
    print(game_choice[0])
if Choice==1:
    print("You chose paper")
    print(game_choice[1])
if Choice==2:
    print("You chose scissors")
    print(game_choice[2])
time.sleep(3)

#computer choice
Computer_choice=random.randint(0,2)
if Computer_choice==0:
    print(" Computer chose:Rock")
    print(game_choice[0])
elif Computer_choice==1:
    print("Computer chose Paper")
    print(game_choice[1])
elif Computer_choice==2:
      print("Computer chose Scissors")
      print(game_choice[2])

#Conclusion:
if Choice>=3 or Choice<0:
    print("You've typed an invalid number. You lose!")
elif  Choice >Computer_choice:
    print("You Won!")
elif Computer_choice==2 and Choice==0:
    print(" You won! ")
elif Computer_choice==Choice:
    print("Its a draw. Try again!")
