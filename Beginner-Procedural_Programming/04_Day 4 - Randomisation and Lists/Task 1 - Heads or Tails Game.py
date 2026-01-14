print("Hello! Welcome to the heads or tails game!\n")

import  random
import time

random_number= random.randint(0,1)
time.sleep(2)

if random_number ==0:
    print(" The coin flip produces: Heads")
else:
    print(" The coin flip produces: Tails")
