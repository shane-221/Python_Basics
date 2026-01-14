# Opening code:
print("Welcome to the tip calculator!")

#The necessary data
total_bill= float(input("What was the total bill?\n"))
tip= int(input("How much tip would you like to give?( 10%, 15%,  or  25%)\n"))
people=int(input("How many people to split the bill?\n"))

# Calculations
    # Tip percentages
tip_percentage= 1+( tip/100)
final_bill= total_bill * tip_percentage
final_bill_pp=( final_bill / people)
final_bill_pp= round(final_bill_pp,2)

# Final output
print(f"    Each person should pay:£{final_bill_pp}")
