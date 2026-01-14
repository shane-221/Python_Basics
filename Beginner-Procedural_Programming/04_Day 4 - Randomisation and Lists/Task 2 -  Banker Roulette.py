import random

# List of friends
friends  = ["Alice", "Bob", "Charlie", "David", " Emmanuel"]
    # Random choice of number
chosen_number= random.randint(0, len(friends)-1)
    # Random chosen person
chosen_person= friends[chosen_number]
#Final output
print(f" The person who will pay is:{ chosen_person}")
