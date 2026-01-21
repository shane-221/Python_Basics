import random

from flask import Flask
import random
# Correct Number to be embedded
chosen_number  = random.randint(1, 10)

gifs=["https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmRycTdndGVqMmRyOWl0eWxndWxnczc2ZHR4Mng3Z3hhNmwwMTBjOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hPPx8yk3Bmqys/giphy.gif",
      ]



app=Flask(__name__)

@app.route("/")
def home():
    return "<h1  style ='text-align:center' >Guess a number between 0 and 9</h1>"\
           '<img src ="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZDFndzRjb3JiMmh0bm5xOGY3ajJtdm1ueXdwMjZsbnZydmgxMTd6NiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/nTZt1E0IM8sKSEVirG/giphy.gif" style="display:block; margin: 0 auto;" />'

for i in range(1, 10):
    if i!=chosen_number:
        @app.route("/<int:i>")
        def endpoint():




if __name__=="__main__":
    app.run(debug=True)
