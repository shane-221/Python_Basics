from tkinter import *
from tkinter import messagebox

#---------------------------------------------Constants----------------------------------------------------------------#
FONT = ( " Arial", 12, "bold")

#--------------------------------------Building the Screen ------------------------------------------------------------#


        #####################----- Building the image section -----################

# Todo: window functions
window1 = Tk()
window1.title("Password Manager")
window1.config(padx=20,pady=20)

# Todo: Canvas with the image
canvas = Canvas( width = 200,height= 200, highlightthickness= 0)
logo_ing =PhotoImage(file ="../../Day 30 - Errors, Exceptions, JSON Data/Using JSON to search/logo.png")
canvas.create_image(100, 100, image= logo_ing )
canvas.grid(row= 0,column =1)


# ----------------------------------------------Functionalities---------------------------------------------------------#
# Todo: Saving the data. Creating an embedded list, then convert to data frame, then to a text file

        # Todo: Creating an embedded list

def save():

        # tODO: Get all the values
    website_value = website_input.get()
    email_value = email_input.get()
    password_value = password_input.get()
        # Todo: making sure that the values are correct:

    if len(website_value) != 0 and len(email_value) != 0 and len(password_value) != 0:
        is_ok = messagebox.askokcancel(title=website_value,
                                       message=f"""
                               These are the details entered:
                                Email:{email_value}
                                Password : {password_value}
                                Is it okay to save?     
                                    """)
        if is_ok:
            dataset = f"{website_value} -{email_value} - {password_value}\n"
            with open("Password record.txt", mode ="a") as files:
                files.write(f"{dataset}")

            # Todo: deleting the values once you click add.
            website_input.delete(0, END)
            password_input.delete(0, END)
            email_input.delete(0, END)
    else:
        messagebox.showinfo(title="Oops", message=" Please dont leve the fields empty!")


            # Todo: convert that list into a txt file and using it
def print_results():
    # Todo: Creating the new Window
    window2= Tk()
    window2.title("Password List", )
    window2.config(padx=20, pady=20, bg= "black")

    # Todo: Pulling the text from the function.

    with open("Password record.txt") as file:
        content = file.read()

    # Creating the text Function to present the data

        password_content  = Text(window2,  font=FONT, fg="white", bg="black")
        password_content.focus()
        password_content.insert("1.0", content)
        password_content.grid(row=0, column= 0)




#--------------------------------UI Interface -------------------------------------------------------------------------#

        #####################-----Button Sections-----###########################
# Todo: Add button
add_button = Button(text= "Generate list of Passwords ", command  = print_results, width = 36)
add_button.grid(row=4, column= 1, columnspan= 2, sticky= "ew")

# Todo: Generate Password Button
password_button= Button(text =" Add" , command  = save, width=15, padx= 30)
password_button.grid(row= 3, column= 2)



        #####################-----Entry Section-----##############################
# Todo: Password write section
password_input = Entry( width = 36)
password_input. grid(row= 3, column = 1, sticky= "ew")

# Todo: Email section
email_input = Entry( width =36)
email_input. grid(row= 2, column = 1, columnspan = 2, sticky="ew")

# Todo: Website section
website_input = Entry( width =36 )
website_input. grid(row= 1, column = 1, columnspan= 2, sticky= "ew")
website_input.focus




        ####################----- Text Section-----###############################
# Todo: Password Label
password_text = Label(text ="Password:", font=FONT )
password_text.grid( row= 3, column = 0)

# Todo:  Email/ Username Label
email_text = Label(text ="Email/ Username:", font=FONT )
email_text.grid( row= 2, column = 0)

# Todo:  Website Label
website_text = Label(text ="Website:", font=FONT )
website_text.grid( row= 1, column = 0)
            # Allows you to pre-populate the file.




#----------------------------------------------Exit when needed--------------------------------------------------------#
mainloop()