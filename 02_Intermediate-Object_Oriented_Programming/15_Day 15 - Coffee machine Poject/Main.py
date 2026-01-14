from Resources import coffee


                                                                                                                        # Todo Coffee:
                                                                                                                            #   todo:  Ask which coffee they want
def coffee_function():
    coffee_choice= input(f"""
    {coffee}
    Welcome to the coffee machine. What can I offer you? You have a choice between: 
        1) Espresso
        2) Latte 
        3) Cappuccino
    Please type in the type of coffee you prefer:
    """).lower()

    while coffee_choice not in ["espresso", "latte", "cappuccino"]:
        coffee_choice= input(" Invalid choice: Please choose 'Espresso' or 'Latte' or 'Cappuccino':")
                                                                                                                            #   todo: Check if there are sufficient resources
                                                                                                                            #   todo: Check payment
                                                                                                                            #   todo: ask if they want to run the coffee function again or get the report or switch off

                                                                                                                        # Todo Other functions:
                                                                                                                            #  todo: Print the report function.
                                                                                                                            #  todo: ask if they want to run the coffee function again or get the report or switch off.

"-----------------------------------------------------------------------------------------------------------------------"
                                                                                                                        # Todo : Ask if they want coffee or other functions
open_machine= input( """
                     Welcome to the coffee machine Startup function! "
                     Would you like to order coffee or Run other functions?"
                     For coffee - Choose (A). "
                     For other functions - Choose (B)\n 
                     """).lower()
while open_machine not in ["a", "b"]:
    input(" Invalid choice: Please choose 'A' or 'B':")

if open_machine == "a":
    coffee_function()
else:
    "print the report function"
"------------------------------------------------------------------------------------------------------------------------"
