from flask import Flask

# Creating an instance of the class
app = Flask(__name__)


# Setting the route through the decorator.
@app.route("/")
def hello_world():
    return "Hello World"
