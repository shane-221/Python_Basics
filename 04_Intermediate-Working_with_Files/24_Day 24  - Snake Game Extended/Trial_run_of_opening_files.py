from idlelib.debugobj import myrepr  # More compelx way of doing it
files = open("my_file.txt")
content = files.read()
print(content)
files.close()


    #Easier way of doing it.
with open("my_file.txt") as file:
    content = files.read()
    print(content)
        # Will not need to close the file. With command closes the filre directly.

    # =Can also write within the file:

with open( "my_file.txt", mode =" w") as files:
    files.write(" New text.")
        # This removes everything in the file and puts the write content into it

with open( "my_file.txt", mode =" a") as files:
    files.write("\n New text.")
        # Changing the mode to a will just add the text bit into the file.
        ## a stands for append at the end of the list. Need to run it though.
