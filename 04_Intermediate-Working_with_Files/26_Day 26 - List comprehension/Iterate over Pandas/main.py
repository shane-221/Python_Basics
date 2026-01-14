student_scores = {"Students":[ "Alice", "Bob", "Charlie" ,"Diana" , "Ethan" ],
                  "Score ": [88, 76, 93, 85, 90]
                  }


# Todo 1:  Accessing items within a dictionary
# so far we have looped through a dictionary through the use of (key, value) and .items() to spit the
## dictionary into items where we can access the keys separately and the value separately e.g.
for (key, value) in student_scores.items():
    #print( value)
    pass

# Todo 2: Convert the dictionary into a data frame.
import pandas as pd
dataset = pd.DataFrame(student_scores)
print( dataset)
    # Todo: access the data like you would in a dictionary
for (key, value) in dataset.items():
    print(value)
    pass

#     # Todo: this is not that useful given that it iterates over the column. Thus panda produces this function :
# for (index, row) in dataset.iterrows():
#     #print(  row)
#         # This will print everything by rows through each of the index.
#         # Todo: you could access a certain specific row through the dot notation
#     print( row.Students)
#             # This will print out all the students



