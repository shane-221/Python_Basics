from tkinter import *
import math
# ----------------------------------------------- CONSTANTS ---------------------------------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
marks =""
my_timer =None

# -------------------------------------------------------- UI SETUP -------------------------------------------------- #

# Todo: Building of the screen
window =Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg =YELLOW)

# Todo: Placing the image on the screen.
canvas  = Canvas(width =200, height=224 ,  highlightthickness=0)
canvas.config(bg= YELLOW)
tomato_img = PhotoImage(file="tomato.png")          # Image will not learn the tomato file. Hence, need to
                                                    ## read through the file and get access to the location.
canvas.create_image(100, 112, image =tomato_img)
timer_text = canvas.create_text(100, 130, text ="00:00", fill= "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(row=1, column = 1)
                                        # Need to create padding on each side of the picture to make it look cleaner

# Todo: placing the title on the screen
total_label = Label(text="Study Timer", font =( " Arial", 30, "normal"), fg= GREEN, bg= YELLOW)
total_label.grid(column= 1, row =  0)

# Todo: starting the timer to call the function and adjusting for the specific times.
def start_timer():                                                                                                      #(2)#
    global reps
    if reps == 1 or reps==3 or reps ==5 or reps ==7:
        count_down(WORK_MIN*60)
        study_label1 = Label(text="Study! ", font=(" Arial", 20, "normal"), fg=GREEN, bg=YELLOW)
        study_label1.grid(column=1, row=4)
        # Todo: Adding a tick mark for every session completed
        global marks
        marks += "✓"
        check_marks.config(text=marks)
        reps+=1
    elif reps==2 or reps ==4 or reps==6:
        count_down(SHORT_BREAK_MIN*60)
        break_label1 = Label(text="Break", font=(" Arial", 20, "normal"), fg=PINK, bg=YELLOW)
        break_label1.grid(column=1, row=4)
        reps+=1
    elif reps==8:
        count_down(LONG_BREAK_MIN*60)
        break_label2 = Label(text="""
                            Well Done! You've finished the session""",
                            font=(" Arial", 20, "normal"), fg=RED, bg=YELLOW)
        break_label2.grid(column=1, row=4)


# -------------------------------------------- TIMER RESET ---------------------------------------------------------- #
def reset_timer():
    # Todo: How to stop the timer
    global my_timer
    window.after_cancel(my_timer)
    # Todo: resetting the tick marks
    global marks
    marks =""
    check_marks.config(text  = marks)
    # Todo: resetting the timer
    canvas.itemconfig(timer_text, text= "00:00")
    # Todo: reset reps to 0
    global reps
    reps = 0
timer_reset = Button(text ="Reset",  highlightthickness= 0, command= reset_timer)
timer_reset.grid(row = 2, column =3)

# ---------------------------------------------- TIMER MECHANISM ---------------------------------------------------- #
# Todo: Timer Button
timer_start = Button(text= "Start", highlightthickness= 0, command= start_timer)                                        #(1)#
timer_start.grid(row = 2, column = 0)

# Todo: Creating the timer tick mark
check_marks  = Label(text=marks, font =( " Arial", 20, "normal"), fg= GREEN, bg= YELLOW)
check_marks.grid(column= 1, row =  3)

# --------------------------------------=------- COUNTDOWN MECHANISM ------------------------------------------------- #
# Todo: Start button gets clicked--> count donw function gets applied encased with the number of sections
#  ------>leads to the count down function. This is where the number is converted into minutes and seconds
#  where two things happen: 1) seconds keep reuducing 2) WSeconds gets converted into minutes and seconds and displayed.
def count_down(seconds):                                                                                                 #(3)#
    count_min = math.floor(seconds/60)
    count_seconds= seconds% 60

    if count_seconds<10:
        count_seconds =f"0{count_seconds}"

    if seconds>0:
        global my_timer
        my_timer = window.after(1000, count_down, seconds-1)
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")
    else:
        start_timer()
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")



#-----------------------------------------------KEEP THE SCREEN OPEN--------------------------------------------------#
window.mainloop()