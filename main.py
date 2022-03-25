from flask import Flask
from flask import render_template
from flask import url_for
from flask import request

import download_file


app = Flask(__name__)

"""
@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return render_template("helloform.html")
    if request.method == "POST":
        name = request.form["htmlname"]
        place = request.form["htmlplace"]
    else:
        print("Hier hat was nicht funktioniert, sorry. Bitte lade die Seite neu!")

    about_link = url_for("about")
    return render_template("index.html")
"""



@app.route("/", methods=["GET", "POST"])
def urlreceiver():

    return render_template("index.html")

    if request.method == "POST":
        youtube_link = request_form["youtube_link"]
        return (youtube_link)
        print(youtube_link)
    if request.method == "GET":
        return ("Fehlermeldung")
    else:
        return ("da hät di request method nöd funktioniert")





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
