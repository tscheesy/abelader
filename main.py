from flask import Flask, render_template, redirect, request, url_for
from pytube import YouTube

import operator
import plotly.express as px

import video_data
import data

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home_sweet_home():
    # bei Submit Home-Formular "POST"
    if request.method == "POST":
        data.counter_up("counter_data.json", "page_views", "questions")
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

        # counting link entry
        data.counter_up("counter_data.json", "totals", "links_entered")

        # Fetching relevant data from API as dict "video_info" with module "video_data", also extracting ID from url
        video_info = video_data.data_from_input(form_input, video)

        # variables for load & save functions from modules
        video_id = video_info["id"]
        file = "video_data.json"

        # comparing object to existing entries, "downloads"-counter + 1 if already exisiting
        if data.load_value(file, video_id):
            data.counter_up(file, video_id, "times_entered")

        else:
            # Saving Video Data in JSON-file
            # Step 1: Create new dict from ID
            data.new_dict(file, video_id)

            # Step 2: start downloads-counter at 1
            data.save(file, video_id, "times_entered", 1)

            # Step 3: Save all relevant video_info data in dict
            for key in video_info:
                data.save(file, video_id, key, video_info[key])

        return render_template("questions.html", video_info=video_info)

    # bei Submit questions.html-Formular "GET" mit args
    elif request.method == "GET" and bool(request.args):

        # nur die drei erlaubten values aus "questions" werden als GET-args akzeptiert, sonst zurück zu index.html
        if request.args["vote_need"] == "creator" or request.args["vote_need"] == "fun" or request.args["vote_need"] == "repost":

            # unused line, unresolved GET-Issue: video_id = request.args["vidid"]

            # save form input in counter-json
            need = request.args["vote_need"]
            data.counter_up("counter_data.json", "purpose", need)

            return redirect("/download/" + need)

        else:
            return render_template("index.html")

    # normaler erster load homepage:
    else:
        data.counter_up("counter_data.json", "page_views", "home")
        return render_template("index.html")


@app.route("/download/<need>", methods=["GET", "POST"])
def form_receiver(need):
    data.counter_up("counter_data.json", "page_views", "download")

    if request.method == "POST":
        data.counter_up("counter_data.json", "totals", "downloads")

    need = need
    return render_template("download.html", need=need)


@app.route("/stats")
def show_stats():
    data.counter_up("counter_data.json", "page_views", "stats")

    # load counter_data json
    counter_dict = data.load_dict("counter_data.json")

    # get purpose dict from counter_dict and sort items by highest value for ranking
    # dict sorting solution from https://www.delftstack.com/de/howto/python/how-to-sort-a-dictionary-by-value/, reversed
    purpose_sorted = sorted(counter_dict["purpose"].items(), key=operator.itemgetter(1), reverse=True)

    """
    # Plotly Basic Bar Chart to display usage (purpose/need)
    data_canada = px.data.gapminder().query("country == 'Canada'")
    fig = px.bar(data_canada, x='year', y='pop')
    fig.show()
    """

    return render_template("stats.html", counters=counter_dict, purpose=purpose_sorted)


@app.route("/about")
def about():
    data.counter_up("counter_data.json", "page_views", "about")
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
