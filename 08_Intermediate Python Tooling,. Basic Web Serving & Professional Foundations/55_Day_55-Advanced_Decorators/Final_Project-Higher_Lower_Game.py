import random

from flask import Flask
import random

# Correct Number to be embedded
chosen_number = random.randint(1, 10)

wrong_gifs = [
    "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif",  # Wrong buzzer / fail
    "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif",  # Too low / disappointed
    "https://media.giphy.com/media/l2YWqU7ev0l5nfYTC/giphy.gif",  # Shaking head no
    "https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif",  # Nope
    "https://media.giphy.com/media/3o7TKr3nzbh5WgCFxe/giphy.gif",  # Wrong answer
    "https://media.giphy.com/media/9Y5BbDSkSTiY8/giphy.gif",  # Facepalm
    "https://media.giphy.com/media/xUOwGgxZLBmqB87sic/giphy.gif",  # Incorrect
]

correct_gifs = [
    "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif",  # Celebration
    "https://media.giphy.com/media/111ebonMs90YLu/giphy.gif",  # Yes!
    "https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif",  # Thumbs up
    "https://media.giphy.com/media/5GoVLqeAOo6PK/giphy.gif",  # Nailed it
    "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif",  # Victory
    "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif",  # Success
    "https://media.giphy.com/media/26BRBKqUiq586bRVm/giphy.gif",  # Celebration dance
]

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1  style ='text-align:center' >Guess a number between 0 and 9</h1>" \
           '<img src ="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZDFndzRjb3JiMmh0bm5xOGY3ajJtdm1ueXdwMjZsbnZydmgxMTd6NiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/nTZt1E0IM8sKSEVirG/giphy.gif" style="display:block; margin: 0 auto;" />'

@app.route("/<int:guess>")
def guess(guess):
        if guess != chosen_number:
            gif = random.choice(wrong_gifs)
            return "<h1  style ='text-align:center' >Wrong Number</h1>" \
                f'<img src ="{gif}" style="display:block; margin: 0 auto;" />'

        elif guess != chosen_number:
            gif = random.choice(correct_gifs)
            return "<h1  style ='text-align:center' >Guess a number between 0 and 9</h1>" \
                   f'<img src ="{gif}" style="display:block; margin: 0 auto;" />'

if __name__ == "__main__":
    app.run(debug=True)
