print("Welcome to Python Pizza Deliveries!")

size= input("What size pizza do you want? S,M,L :")
pepperoni = input("Do you want pepperoni on your pizza? Y or N:")
extra_cheese= input("Do you want extra cheese? Y or N:")
    # Starting Bill
bill=0
    # Breakdown of the Bills. Can also put the pepperoni sections as a separate nested inf / else section as well.
    ## This would mean that you need three  lines of code.
if size =="S":
    bill+=15
    if pepperoni =="Y" :
        bill+=2
elif size =="M":
    bill+=20
    if pepperoni =="Y":
        bill+=3
elif size == "L":
    bill+=25
    if pepperoni =="Y":
        bill+=3
else:
    print(" Please choose one of the three Options: S, M, L")
        # Extra chesse sections that common to all
if extra_cheese=="Y":
    bill+=1
    # Final Bill printing
print(f"Your final bill is ${bill}.")

