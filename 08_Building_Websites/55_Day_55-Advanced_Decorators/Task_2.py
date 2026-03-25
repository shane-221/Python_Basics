from flask import Flask


app = Flask(__name__)

## Decorator Function
def bold(function):
    def wrapper():
        print(">>> bold decorator ran")
        output = function()
        return f"<b>{output}</b><html>"
    return wrapper

@app.route("/qq")
@bold
def home():
    return "Hello World"

@app.route("/<name>")
def names(name):
    return f"Hello {name}"



if __name__ =="__main__":
    app.run(debug=True, use_reloader=False)