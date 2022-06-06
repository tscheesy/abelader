from flask import Flask, render_template, redirect, request, url_for
from pytube import YouTube

import video_data
import data

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home_sweet_home():
    # bei Submit Home-Formular IF
    if request.method == "POST":
        form_input = request.form["youtube_link"]
        try:
            # pytube prüft mittels "except", ob für den Link ein gültiges youtube-Objekt besteht
            video = YouTube(form_input)
            video.check_availability()
        except:
            # Wird für die Eingabe kein gültiges youtube-objekt gefunden, wird der Eingabe-String fürs Fehlerhandling an index.html zurückgegeben
            return render_template("index.html", form_input=form_input)

        # Fetching relevant data from API as dict "video_info" with module "video_data", also extracting ID from url
        video_info = video_data.data_from_input(form_input, video)

        # variables for load & save functions from modules
        entry_title = video_info["title"]
        file = "video_data.json"

        # comparing object to existing entries

        # Saving Video Data in JSON-file
        # Step 1: Create new dict from ID
        data.new_dict(file, entry_title)

        # Step 2: Save all relevant video_info data in dict
        for key in video_info:
            data.save(file, entry_title, key, video_info[key])

        return render_template("questions.html", video_info=video_info)

    # bei Submit questions.html-Formular ELSE
    elif request.method == "GET" and bool(request.args):
        # save form input in json while connecting video ID
        need = request.args["vote_need"]
        return redirect("/download/" + need)
    else:
        return render_template("index.html")


@app.route("/download/<need>", methods=["GET"])
def form_receiver(need):
    need = need
    return render_template("download.html", need=need)


@app.route("/stats")
def show_stats():
    return render_template("stats.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
