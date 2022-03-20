from flask import Flask
from flask import render_template
from flask import url_for
from flask import request


app = Flask(__name__)


@app.route("/")
def hello():
    about_link = url_for("about")
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/data")
def data():
    return render_template("data.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
