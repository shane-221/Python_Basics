from flask import Flask 

app =Flask(__name__)                             # Step 1: create the app object — nothing running yet


@app.route("/")                                 # Step 2: register your routes — still nothing running
def hello_world():
    return "Hello World"


### Need to point to a file that you export as the server( into the terminal). In windows, this is: 

    ## set FLASK_APP=Task_1.py
    ## flask run 
 

### Executes the code from the specific name. 
print(__name__)



### Another way to execute this: 
if __name__ =="__main__" :
    # The code above will run the server from the current file. If the file is being imported by another file -- it will replace the name of the file.

    app.run()                                    # Step 3: NOW the local server starts


