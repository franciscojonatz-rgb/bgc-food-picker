from flask import Flask, render_template
import random
from restaurants import restaurants

app = Flask(__name__)


restaurants = [
    {
        "name": "Manam",
        "cuisine": "Filipino",
        "price": "₱₱",
        "vibe": "Casual"
    },
    {
        "name": "Mendokoro Ramenba",
        "cuisine": "Japanese",
        "price": "₱₱",
        "vibe": "Casual"
    },
    {
        "name": "Mamou",
        "cuisine": "Steakhouse",
        "price": "₱₱₱₱",
        "vibe": "Date Night"
    },
    {
        "name": "Gallery by Chele",
        "cuisine": "Filipino / Modern",
        "price": "₱₱₱₱",
        "vibe": "Fine Dining"
    },
    {
        "name": "COCHI",
        "cuisine": "Filipino",
        "price": "₱₱₱",
        "vibe": "Dinner"
    },
    {
        "name": "a mano",
        "cuisine": "Italian",
        "price": "₱₱₱",
        "vibe": "Date Night"
    },
]


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
