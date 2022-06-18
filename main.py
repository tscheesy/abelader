from flask import Flask, render_template, redirect, request, url_for
from pytube import YouTube

import video_data
import data

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home_sweet_home():
    # bei Submit Home-Formular "POST"
    if request.method == "POST":
        form_input = request.form["youtube_link"]

        # Check, 0b url schon in Datenbank vorhanden, so werden unnötige API-Zugriffe verhindert
        #

        try:
            # pytube prüft, ob für den Link ein gültiges youtube-Objekt besteht
            video = YouTube(form_input)
            video.check_availability()
        except:
            # Wird für die Eingabe kein gültiges youtube-objekt gefunden, wird der Eingabe-String fürs Fehlerhandling an index.html zurückgegeben
            return render_template("index.html", form_input=form_input)

        # Fetching relevant data from API as dict "video_info" with module "video_data", also extracting ID from url
        video_info = video_data.data_from_input(form_input, video)

        # variables for load & save functions from modules
        entry_title = video_info["id"]
        file = "video_data.json"

        # comparing object to existing entries, "downloads"-counter + 1 if already exisiting
        if data.load(file, entry_title):
            data.counter_up(file, entry_title, "times_entered")

        else:
            # Saving Video Data in JSON-file
            # Step 1: Create new dict from ID
            data.new_dict(file, entry_title)

            # Step 2: start downloads-counter at 1
            data.save(file, entry_title, "times_entered", 1)

            # Step 3: Save all relevant video_info data in dict
            for key in video_info:
                data.save(file, entry_title, key, video_info[key])

        return render_template("questions.html", video_info=video_info)

    # bei Submit questions.html-Formular "GET", nur die drei erlaubten values aus "questions" werden als GET-args akzeptiert
    elif request.method == "GET" and request.args["vote_need"] == "creator" or request.args["vote_need"] == "fun" or request.args["vote_need"] == "repost":
        # save form input in json while connecting video ID
        need = request.args["vote_need"]

        file = "counter_data.json"
        data.new_dict(file, )

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
