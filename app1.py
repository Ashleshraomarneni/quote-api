from flask import Flask, jsonify
import random

app = Flask(__name__)

QUOTES = [
    "Keep it simple.",
    "DevOps is culture.",
    "Automate everything.",
    "Containers are cool.",
    "Push, pull, deploy, repeat."
]

@app.route("/")
def get_quote():
    return jsonify({"quote": random.choice(QUOTES)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

