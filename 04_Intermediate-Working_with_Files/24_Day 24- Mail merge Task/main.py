#TODO: Create a letter using starting_letter.txt

with open("Input/Names/invited_names.txt", mode="r") as file:
    contents  = file.read()
    names = contents.splitlines()

#Todo: my Method
    # Todo : open and retrieve the first name
with open("Input/Names/invited_names.txt", mode ="r") as file:
            # Need to always read the file to fully access it.
    content  = file.read()
    for i in names:
            # Split lines function splits the text into a list of strings by line.

        # Todo: Open the template and pull the thing as a string
        with open("Input/Letters/example.txt", mode ="r") as template :
            template_content  = template.read()
            personal_letter = template_content.replace("[name]", i)

            # Todo: create a new file using the write function
        with open(f"Output/ReadyToSend/letter_for_{i}", mode= "w") as final_file:
            final_file.write(personal_letter)

