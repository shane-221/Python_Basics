print( "Hello, welcome to the odd or even number generator!")
number= input("What is your number?\n")
    # Convert the number into an integer, so no longer a string
number= int( number)

    #apply the test for odd or even:
output = number%2
    # Output that will be presented
if output ==0:
    print(" This is an even number!")
else:
    print("This is an odd number")
