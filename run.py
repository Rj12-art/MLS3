import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/recipe")
def recipe():
    return render_template("recipe.html", page_title="Recipe")


@app.route("/signin")
def signin():
    return render_template("signin.html", page_title="Sign In To Your Account")      


@app.route("/signup")
def signup():
    return render_template("signup.html",page_title="Sign Up TO Register")




if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("PORT", "5000")),
        debug = True)
        