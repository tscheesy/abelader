from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from pytube import YouTube

import download_file


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
@app.route("/<url>")

def urlreceiver():
    if request.method == "POST":
        url = request.form["youtube_link"]
        try:
            youtube_object = YouTube(url)
            youtube_object.check_availability()
        except:
            failed_link = True
            return render_template("index.html", no_link=url, failed_link=failed_link)

        object_stats = youtube_object.title + " " + youtube_object.metadata() + " " + youtube_object.streams()
        return render_template('download.html', youtube_object=youtube_object, stats=object_stats)

    return render_template("index.html")


@app.route("/download")
@app.route("/download/<id>", methods=["GET", "POST"])


def start_download(video_id):
    video_id = 666
    download_file.abelade(video_id)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/data")
def data():
    return render_template("data.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
