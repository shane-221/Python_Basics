from flask import Flask 
from flask import render_template


app = Flask(__name__)


@app.route("/")
def opening_page():                                     
    return render_template("index.html")        ## Rendering certain types of templates 


if __name__=="__main__":
    app.run(debug= True)



