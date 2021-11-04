#!/usr/bin/env python3
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    html_template = render_template("index.html")

    return html_template

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))