def love_calculator(your_name, their_name):
    your_name = your_name.lower()
    print(f"Your name is {your_name}")
    print(f"Their name is {their_name}")
    their_name=their_name.lower()

    total_you=0
    total_their=0

    for i in your_name:
        if  i in "true":
            total_you+=1

    for i in their_name:
        if  i in "true":
            total_their+=1
    print(f"Your love score is=: {total_you}{total_their}")

love_calculator("Shane", "Mathew")