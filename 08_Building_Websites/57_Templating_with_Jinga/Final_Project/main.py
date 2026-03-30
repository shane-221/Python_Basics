from flask import Flask, render_template
import requests 


app = Flask(__name__)


## Blog sections 
@app.route("/")
def blog():
    blog_url= "https://api.npoint.io/c790b4d5cab58020d391"
    response= requests.get(blog_url)
    all_posts= response.json()
    return render_template("post.html", posts= all_posts)

## Read route 
@app.route("/post/<int:id>")
def id_page(id):
    blog_url= "https://api.npoint.io/c790b4d5cab58020d391"
    response= requests.get(blog_url)
    all_posts= response.json()
    post = [ post for post in all_posts  if post["id"]==id][0]
    print(post)
    return render_template("read_page.html", posts = post)
    

if __name__ == "__main__":
    app.run(debug=True)
