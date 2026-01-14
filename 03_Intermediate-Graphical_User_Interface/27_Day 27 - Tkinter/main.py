from tkinter import *

# Todo: Opening the window. But need to Keep the window open.
window =Tk()

    # Todo: changing the title of the program:
window.title("My first GUI Program")
    # Todo: adjust the size of the screen.
window.minsize(width=500, height = 300)



# Todo: Creating Labels
my_label = Label(text="I am a Label", font =( " Arial", 24, "bold"))
    # Todo: Laying out how the label will be laid out on the screen( Need to do it for all the classes)
my_label.pack()
    # Todo: Can change the default properties
my_label["text"]= "New Text"


# Todo: Adding buttons
    # Todo: How do you get the button to change the title
def button_click():
        # When the button gets clicked, the text gets replaced with the specific value
    # my_label["text"]=" The Button got Clicked"
        # or you could also:
    # my_label.config(text="buton got clicked")
        # When the button gets clicked the text gets replaced with whats on the entry box
    my_label["text"]=input.get()




# Todo: Entry or Text Boxes
input  = Entry(width=50)
input.pack()
    # Can add whats written in the box to be the title.



# Todo: Getting the button to exit and work
button= Button(text = "Click me ", command = button_click)
button.pack()




# Todo: Keeps the window running
window.mainloop()
