from flask import Flask, render_template,request
from pymongo import MongoClient
import datetime
import certifi


def create_app():
    app = Flask(__name__)
    client = MongoClient("mongodb+srv://fanuel:Kbsdaf123!@cluster0.xzjgpxo.mongodb.net/", tlsCAFile=certifi.where())
    app.db = client.myblog




    @app.route("/", methods = ["GET", "POST"])

    def home():

        if request.method == "POST":
            content = request.form.get("post")
            date = datetime.datetime.today().strftime("%Y-%m-%d")
            app.db.entries.insert_one({"post":content, "date":date})
        entries_format = [
            (entry["post"],
            entry["date"],
            datetime.datetime.strptime(entry["date"],"%Y-%m-%d").strftime("%b %d"))
            for entry in app.db.entries.find({})
        ]
        return render_template("home.html", entries = entries_format)
    return app
