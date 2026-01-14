# Todo: Challenge

# Data Overlap
# 💪 This exercise is HARD 💪
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the numbers that are common in both files.
# e.g. if file1.txt contained:
#
# 1
#
# 2
#
# 3
#
# and file2.txt contained:
#
# 2
#
# 3
#
# 4
#
# result = [2, 3]
# Try to use List Comprehension instead of a Loop.


# Todo: Creating a  master list with all the numbers from both files
list_numbers1 = []
list_numbers2=[]
# Todo; pulling the numbers into the list from both files
with open("file1.txt") as file1:
    content = file1.read().splitlines()
    for i in content:
        i = int(i)
        list_numbers1.append(i)

with open("file2.txt") as file2:
    content = file2.read().splitlines()
    for i in content:
        i = int(i)
        list_numbers2.append(i)
# Todo: removing common numbers
result = [num for num in list_numbers1 if num in list_numbers2]
print(result)
