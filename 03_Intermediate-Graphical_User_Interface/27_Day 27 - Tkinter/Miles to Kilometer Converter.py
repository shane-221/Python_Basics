from tkinter import *



# Todo: Opening the window. But need to Keep the window open.
window =Tk()


    # Todo: changing the title of the program:
window.title("Miles to Km Converter")
    # Todo: adjust the size of the screen.
window.minsize(width=300, height = 100)

# Todo: Entry or Text Boxes
input  =(Entry(width=20))
input.grid(column=1, row=0)

# Todo: creating the functiont to click
def calculate_function():
    miles = float(input.get())
    final_km= miles*1.609
    number_Label["text"]=final_km




# Todo: Creating the button to Click:
button  = Button(text= "Calculate", command= calculate_function)
button.grid(column=1, row=2)



# Todo: Creating all the text
    # Todo: KM Label
km_label = Label(text="KM", font =( " Arial", 10, "normal"))
km_label.grid(column= 2, row =  1)

    # Todo; Creating the changing Km Function

number_Label= Label(text="0", font =( " Arial", 10, "normal"))
number_Label.grid(column= 1, row =  1)
    # Todo: is equal to part
equal_to_label = Label(text="is equal to", font =( " Arial", 10, "normal"))
equal_to_label.grid(column= 0, row =  1)

    # Todo: Miles letters
miles_label = Label(text="Miles", font =( " Arial", 10, "normal"))
miles_label.grid(column= 3, row =  0)



# Todo: Keeps the window running
window.mainloop()