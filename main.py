from flask import Flask, render_template, url_for, request
from pytube import YouTube

import video_data

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        form_input = request.form["youtube_link"]
        try:
            video = YouTube(form_input)
            video.check_availability()
            # pytube prüft mittels "except", ob für den Link ein gültiges youtube-Objekt besteht
        except:
            # Wird für die Eingabe kein gültiges youtube-objekt gefunden, wird die eingabe ans index.html zurückgegeben
            return render_template("index.html", form_input=form_input)

        video_info = video_data.data_from_input(form_input, video)
        return render_template("questions.html", video_info=video_info)
    return render_template("index.html")


@app.route("/<session_id>", methods=["GET", "POST"])
def requestions(session_id):
    questions = True
    return render_template("index.html", questions=questions, session_id=session_id)


@app.route("/download", methods=["POST"])
def urlreceiver():
    if request.method == "POST":
        link = request.form["youtube_link"]
        video = YouTube(link)

        video_stats = {
            "titel": video.title,
            "beschreibung": video.description,
            "dauer": str(video.length),
            "datum": video.publish_date,
            "thumbnail": video.thumbnail_url,
            "keywords": video.keywords,
            "views": video.views,
            "bewertung": video.rating,
            "author": video.author,
            "poster_channel_id": video.channel_id,
            "channel_url": video.channel_url,
            "metadaten": video.metadata,
            "age_gate": video.bypass_age_gate(),


        }

        return render_template("download.html", video_stats=video_stats)


@app.route("/stats")
def data():
    return render_template("stats.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
