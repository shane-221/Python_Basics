from flask import Flask, render_template
import random
import requests

app = Flask(__name__)



## Task 1 Examples
@app.route("/")
def main_page():
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number)

## Task 2: Gender Task 
@app.route("/guess/<name>")
def name_page(name):
    name= name.capitalize()
    gender  = requests.get(f"https://api.genderize.io?name={name}")
    gender= gender.json()
    gender =gender["gender"]
    age = requests.get(f"https://api.agify.io?name={name}")
    age = age.json()
    age = age["age"]
    return render_template("name.html",person_name = name, final_ages = age , genders = gender)


## TASK 3 Examples: 
@app.route("/blog")
def blog():
    blog_url= "https://api.npoint.io/c790b4d5cab58020d391"
    response= requests.get(blog_url)
    all_posts= response.json()
    return render_template("blog.html", posts= all_posts)

if __name__ =="__main__":
    app.run(debug= True )
