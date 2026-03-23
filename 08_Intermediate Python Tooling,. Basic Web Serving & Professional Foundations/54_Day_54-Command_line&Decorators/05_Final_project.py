from flask import Flask 
import random 

#### Prep code: 
correct_number = random.randint(0, 9)
app =Flask(__name__)




#### Homepage ------------------------------------------#
@app.route("/")
def home_path():
    return """
    <h1>Guess a number between 0 and 9</h1>
    <img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNW1pZXdrb2F0ZGFtZGE3MmZsMzA4bHozZGFsc2FhaDZ6emd4MHlzbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7aCSPqXE5C6T8tBC/giphy.gif' width='300'>
    """
@app.route("/<int:number>")
def outcome_path(number):
    if number == correct_number:
        return  """<h1>Correct answer!</h1>
    <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width='300'>"""

    elif number < correct_number:
        return  """<h1>Too low!</h1>
    <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width='300'>"""

    else: 
        return  """<h1>Too High!</h1>
<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width='300'>"""
    

#### Running the code ----------------------------------#
if __name__ =="__main__" :
    
    app.run(debug= True)                                    


