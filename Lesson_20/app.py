from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    "Code is read more often than it is written.",
    "First, solve the problem. Then, write the code.",
    "Simplicity is the soul of efficiency."
]

@app.route("/")
def home():
    return app.send_static_file("index.html")

@app.route("/api/quote")
def get_quote():
    quote = random.choice(quotes)
    return jsonify({"quote": quote})

if __name__ == "__main__":
    app.run(debug=True)