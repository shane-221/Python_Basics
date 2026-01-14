import time

print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \\/ _` / __| | | | '__/ _ \\ / __| |/ _` | '_ \\ / _` |
| |_| | |  __/ (_| \\__ \\ |_| | | |  __/ \\__ \\ | (_| | | | | (_| |
 \\__|_|  \\___|\\__,_|___/\\__,_|_|  \\___|_|___/_|\\__,_|_| |_|\\__,_|


Welcome to Treasure Island. 
''')

#Have a three-second gap before the storyline
time.sleep(3)

#1st decision
Decision_1=input('''
You are stranded on an island. 
Having scouted the outer areas of the island; you reach a set of crossroads. 
 Where do you want to go? Type 'left' or 'right'\n''')
Decision_1.lower()

#Pathway for decision 1
if Decision_1=="left" :
  time.sleep(1)
  print('''You've come to a lake. There is an island in the     
  middle of the lake. 
  ''')
  #second decision
  Decision_2=input("You can wait or swim. Type 'wait' or 'swim' \n")
  Decision_2.lower()
  if Decision_2=="wait":
    time.sleep(1)
    print('''
    You notice a small boat at the end of a pier.
    You take the boat and row to the island"
    Eventually you reach a set of doors at the island.
    They are Yellow, Blue and Red
    ''')

    #Decision 3:
    Decision_3=input("Which door do you choose?\n")
    Decision_3.lower()
    if Decision_3=="red":
      time.sleep(1)
      print("You were burned by fire. Game over!")
    elif Decision_3=="blue":
      time.sleep(1)
      print("You were eaten by beasts. Game over!")
    elif Decision_3=="yellow":
      time.sleep(1)
      print("You have reached the Treasure. You win!")
    else:
      time.sleep(1)
      print("You were killed. Game over!")
  else:
    time.sleep(1)
    print("You were eaten by piranhas. Game over!")
else:
  print("You fell into a hole. Game over!")