# Todo: Operations
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1-n2
def multiply(n1, n2):
    return n1*n2
def divide(n1, n2):
    return n1/n2

operations={"+": add,
            "-":subtract,
            "*":multiply,
            "/": divide,
            }

# TODO: Game begins
# TODO 3: GAME BEGINS
replay=True
while replay:
    # TODO: 3A Initial opening of the game
    number_one = int(input("What is the first number?"))
    maths = input(" Which operation would you like to perform: "
                  "+"
                  "x"
                  "/"
                  "-")
    number_two = int(input("What is the next number?"))
    # TODO: 3B Application of the inputs.
    output= operations[maths](number_one, number_two)
    print(f"Your output is {output}")

    # TODO: 3C The tree options on what to do with the number( Yes. no, leave)
    next_steps = input(f"""
                         Type 'y' if you want to continue with  {output}
                         Or 'n' if you wish to do a new calculation
                         Or please Type 'l' to leave the game
                         """).lower()
    if next_steps=="l":
        replay = False
        print("Thanks for playing my calculator game!")

    elif next_steps == "n":
        replay = True
        # Redundant but useful for understanding the flow of the game
    elif next_steps == "y":
        continue_loop = True

        while continue_loop:
            second_maths = input(" Which operation would you like to perform: "
                                 "+"
                                 "x"
                                 "/"
                                 "-")
            number_three = int(input("What is the next number?"))
            output_2 = operations[second_maths](output, number_three)
            print(f"Your output is {output_2}")
            output = output_2
            replay_loop = input("Would you like to keep using this number?")
            if replay_loop == "n":
                continue_loop = False

    else:
        print("This is not an option. Please restart the game!")



