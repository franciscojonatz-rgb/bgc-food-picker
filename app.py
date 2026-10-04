from flask import Flask, render_template
import random
from restaurants import restaurants

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate")
def generate():
    restaurant = random.choice(restaurants)
    return render_template(
        "index.html",
        restaurant=restaurant
    )


if __name__ == "__main__":
    app.run(debug=True)
