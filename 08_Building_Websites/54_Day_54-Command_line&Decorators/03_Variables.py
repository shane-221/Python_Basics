from flask import Flask 

app =Flask(__name__)                             # Step 1: create the app object — nothing running yet


@app.route("/")                                 # Step 2: register your routes — still nothing running
def hello_world():
    return "Hello World"




@app.route("/username/<name>")
def greet_name(name):
    return f"Hello {name}"


### Another way to execute this: 
if __name__ =="__main__" :
    app.run()                                   


