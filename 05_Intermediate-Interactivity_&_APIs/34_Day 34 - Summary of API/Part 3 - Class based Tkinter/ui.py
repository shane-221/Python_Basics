import tkinter
from tkinter import *
from quiz_brain import QuizBrain#


#-------------------------------------------------- Constants----------------------------------------------------------#
THEME_COLOR = "#375362"
FONT_HEADING = ( " Arial", 18, "bold")



#--------------------------------------------------Class Prep----------------------------------------------------------#

class UserInterface:


    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        # Todo : creating the window with the background colour
        self.window= Tk()
        self.window.config(bg= THEME_COLOR, height=600, width=400, padx=20, pady=20)
        self.window.title("Trivia Question Game")

        # Todo: creating the canvas
        self.canvas = Canvas( width= 400, height = 300 , highlightthickness= 0)
        self.canvas.config( bg= "white" )
        self.canvas_text = self.canvas.create_text(200, 150,
                                                    text=f" Some question Text",
                                                   font=FONT_HEADING,
                                                   width=280)
        self.canvas.grid( row=1, column=0,  padx = 20, pady= 20, columnspan = 2)

        # Todo : Score Label
        self.score_label = Label(text="Score:0", fg= "white",bg= THEME_COLOR)
        self.score_label.grid(row=0, column =1)


        # Todo : Adding in the images:

            # Todo Tick or true function.
        self.true_img =tkinter.PhotoImage(file ="../images/true.png")
        self.true_button = Button( image= self.true_img, command  = None, width=95, height=95)
        self.true_button.config(highlightthickness=0, padx=40, pady=40)
        self.true_button.grid(row=2, column =0)
            # Todo Cross or False function.
        self.false_img =tkinter.PhotoImage(file = "../images/false.png")
        self.false_button = Button( image= self.false_img, command  = None, width=95, height=95)
        self.false_button.config(highlightthickness=0, padx=40, pady=40)
        self.false_button.grid(row=2, column = 1,)

        self.question_upload()
        self.window.mainloop()

    # Todo: creating the function that merges the canvas text with the question and answer stuff
    def question_upload(self, question):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.canvas_text, text = q_text)








