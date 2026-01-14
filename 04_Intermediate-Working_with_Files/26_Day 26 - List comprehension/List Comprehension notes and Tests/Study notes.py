numbers =[1,2,3,4,5]
# Todo: list comprehension --- old method

new_list =[]
for n in numbers:
    add_1= n+ 1
    new_list.append(add_1)
print (new_list)

# Todo: List comprehension method
new_list = [n+1
            for n  in numbers ]
print (new_list)

# Todo: use the range function to create a list where each of the numbers is doubled.
new_numbers = [ n*2 for n in range(1,6)]
print(new_numbers)

# Todo: conditional list comprehension
names = ["Alex","Jordan", "Taylor", "Morgan","Casey"]
short_names = [name for name in names if len(name)<5]
print(short_names)

# Todo: changing somethign with list comprehension.
names_list = [ "Aiden", "Bella", "Cameron", "Dylan", "Evelyn","Finn", "Grace",  "Harper","Isaac"]
new_names =[names.upper() for names in names_list if len(names)>6 ]
print(f"new_names:{new_names}")