from flask import Flask, render_template, request, redirect, url_for
import os
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('my_app')
answer = None


@app.route("/", methods=["GET", "POST"])
def home():
    global answer
    answer = None
    return render_template("index.html")


@app.route("/age",  methods=["GET", "POST"])
def results():
    name = request.form.get("input")
    response = requests.get(url=f"https://api.agify.io?name={name}")
    age = int(response.json()["age"])
    return render_template("age.html", age=age, answer=answer)


@app.route("/k",  methods=["GET", "POST"])
def correct():
    global answer
    answer = "correct"
    return redirect(url_for('results'))


@app.route("/m",  methods=["GET", "POST"])
def wrong():
    global answer
    answer = "wrong"
    return redirect(url_for('results'))


if __name__ == "__main__":
    app.run(debug=True)
