from Art import logo
import time

# TODO 1: Applying the operations
def operation(first_number, operations, second_number  ):
        # TODO 2: Using these inputs:
    if operations== "+":
        final_number= first_number + second_number
        return final_number
    elif operations == "-":
        final_number= first_number - second_number
        return final_number
    elif operations== "x":
        final_number= first_number*second_number
        return final_number
    elif operations== "/":
        final_number=first_number/second_number
        if final_number==0:
            return None
        else:
            return final_number
    else:
        print("Please choose the correct operation")

#TODO 2: Next step input

def next_step():
    next_steps= input(f"""
                     Type 'y' if you want to continue with  {output}
                     Or 'n' if you wish to do a new calculation
                     Or please Type 'l' to leave the game
                     """).lower()
    return next_steps


# TODO 3: GAME BEGINS
replay=True
while replay:
    print(logo)

    # TODO : Initial opening of the game
    number_one = int(input("What is the first number?\n"))
    maths = input(""" Which operation would you like to perform: 
                  "+"
                  "x"
                  "/"
                  "-"
                  \n""")
    number_two = int(input("What is the next number?\n"))

    output = operation(first_number=number_one, operations=maths, second_number=number_two)
    output= int(output)
    print(f"Your output is {output}")

    next_action= next_step()

    # TODO : Inflection point of the three options
    if next_action=="l":
        replay=False
        print("Thanks for playing my calculator game!")

    elif  next_action=="n":
        replay=True
        print("\n"*50)
                            # Redundant but useful for understanding the flow of the game
    elif next_action=="y":
        continue_loop= True

        while continue_loop:
            second_maths = input(""" Which operation would you like to perform: "
                                 "+"
                                 "x"
                                 "/"
                                 "-"
                                 \n""")
            number_three = int(input("What is the next number?\n"))
            output_2 = operation(first_number=output, second_number=number_three, operations=second_maths)
            print(f"Your output is {output_2}")
            output = output_2
            replay_loop=input("Would you like to keep using this number?\n")
            if replay_loop=="n":
                continue_loop=False
                print("\n"*50)

    else:
        print("This is not an option. Please restart the game!")



