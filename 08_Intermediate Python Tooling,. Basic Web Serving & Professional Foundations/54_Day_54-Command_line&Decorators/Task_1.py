from flask import Flask 

app =Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"


### Need to point tot a file that you export as the server( into the terminal). In windows, this is: 

## set FLASK_APP=Task_1.py
## flask run 