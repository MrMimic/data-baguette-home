#!/usr/bin/env python3
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    context = {
        "contact_email": "emeric.dynomant@gmail.com",
        "cookies_adress": "https://data-baguette.com/cookies",
        "about_adress": "https://data-baguette.com/about"
    }
    html_template = render_template("index.html", **context)
    return html_template

@app.route("/about", methods=["GET", "POST"])
def about():
    html_template = render_template("about.html")
    return html_template

@app.route("/cookies", methods=["GET", "POST"])
def cookies():
    html_template = render_template("cookies.html")
    return html_template


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))