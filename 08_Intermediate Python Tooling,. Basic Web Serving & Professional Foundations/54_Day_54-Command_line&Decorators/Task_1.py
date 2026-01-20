from flask import  Flask


app= Flask(__name__)


# Can print the name as well:
# print(__name__)
    # Will print out __name__
    # So if its name then it would be considered the main page __main __.
    ## Hence, ti will execute the code.
    ### print(random.__name__) name of the file that will be run

@app.route("/")
def hello_world():
    return "Hello World"


# If the name is the same as the current file
if __name__ =="__main__":
    # Will only need to use standard controls from maon.py
    app.run()
