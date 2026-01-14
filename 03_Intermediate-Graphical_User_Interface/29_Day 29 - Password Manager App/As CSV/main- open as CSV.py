from tkinter import *
import pandas as pd
from tkinter import messagebox

#---------------------------------------------Constants----------------------------------------------------------------#
FONT = ( " Arial", 12, "bold")

#--------------------------------------Building the Screen ------------------------------------------------------------#


        #####################----- Building the image section -----################

# Todo: window functions
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

# Todo: Canvas with the image
canvas = Canvas( width = 200,height= 200, highlightthickness= 0)
logo_ing =PhotoImage(file ="../../Day 30 - Errors, Exceptions, JSON Data/Using JSON to search/logo.png")
canvas.create_image(100, 100, image= logo_ing )
canvas.grid(row= 0,column =1)


# ----------------------------------------------Functionalities---------------------------------------------------------#
# Todo: Saving the data. Creating an embedded list, then convert to data frame, then to a text file

        # Todo: Creating an embedded list

def save():
        #  Todo: Get all the values
    website_value = website_input.get()
    email_value = email_input.get()
    password_value = password_input.get()
    #Todo 1: Checking to see if the values are not empty
    if len(website_value)!=0 and len(email_value)!=0 and len(password_value)!=0:

            # Todo 2: checking if they are sure of it
        is_ok = messagebox.askokcancel(title = website_value,
                               message =f"""
                               These are the details entered:
                                Email:{email_value}
                                Password : { password_value}
                                Is it okay to save?     
                                    """)
        if is_ok:

            #  Todo 2 : Put the items into a list
            item_list =[website_value, email_value, password_value]

            #  Todo 2: Create that singular list into a data frame
            dataset = pd.DataFrame([item_list], columns =["Website", "Email", "Password"])

            # Todo 2: This data frame is added into a primary data frame thats a csv with the headings.
            dataset.to_csv("Password record.csv",
                           mode ="a",
                           header = False,
                           index = False)
            # Todo 2: deleting the values once you click add.
            website_input.delete(0, END)
            password_input.delete(0, END)
            email_input.delete(0, END)

    # Todo 1: Other sside of the if statement
    else:
        messagebox.showinfo(title ="Oops",message =" Please dont leve the fields empty!")

def print_results():
    data =pd.read_csv("Password record.csv")

    # Todo: Creating the new Window
    window2= Tk()
    window2.title("Password List", )
    window2.config(padx=20, pady=20, bg= "black")

    # Todo: Pulling the text from the function.
    password_content  = Text(window2,  font=FONT, fg="white", bg="black")
    password_content.focus()
    password_content.insert("1.0", data)
    password_content.grid(row=0, column= 0)

#--------------------------------UI Interface -------------------------------------------------------------------------#

        #####################-----Button Sections-----###########################
# Todo: List of passwords function
add_button = Button(text= "Generalist List of Passwords ", command  = print_results, width = 36)
add_button.grid(row=4, column= 1, columnspan= 2, sticky= "ew")

# Todo:Add it onto my list
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