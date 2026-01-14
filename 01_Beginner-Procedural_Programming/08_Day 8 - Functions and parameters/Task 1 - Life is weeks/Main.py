def life_in_weeks():
    total_life_in_weeks= 90*52
    age= int(input(" How old are you? "))
    left_over_weeks=total_life_in_weeks-(age*52)

    print(f"You have {left_over_weeks} weeks left!")

life_in_weeks()