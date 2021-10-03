import os
import json
from flask import Flask, render_template

os.environ.setdefault("SECRET_KEY", "secret_flash_key")
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/recipe")
def recipe():
    data = []
    with open("data/recipe.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("recipe.html",page_title="Recipe",recipe=data)


@app.route("/pasta")
def pasta():
    render_template("pasta.html",page_title="Pasta for the Day?")


@app.route("/beef")
def beef():
    data = []
    with open("data/recipe.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("beef.html", page_title= "Beef",recipe=data)    

@app.route("/signin")
def signin():
    return render_template("signin.html",page_title="Sign Up TO Register")


@app.route("/signup")
def signup():
    return render_template("signup.html",page_title="Sign Up TO Register")




if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("PORT", "5000")),
        debug = False)
        
