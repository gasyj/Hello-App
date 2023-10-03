# main.py

from flask import Flask

app = Flask(_name_)

@app.route("/")
def index():
    return "Congratulations, Web App is Live!"
