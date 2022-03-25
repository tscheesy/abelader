from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from pytube import YouTube

import download_file


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def urlreceiver():

    if request.method == "POST":
        url = request.form['youtube_link']
        try:
            youtube_object = YouTube(url)
            youtube_object.check_availability()
        except:
            return "WRONG NUMBER"

        return youtube_object.title

    return render_template("index.html")


@app.route("/download")
@app.route("/download/<id>")
def abc():
    success = 1
    return success


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/data")
def data():
    return render_template("data.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
