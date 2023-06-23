from flask import Flask, render_template,request
from pymongo import MongoClient
import datetime
app = Flask(__name__)
client = MongoClient("mongodb+srv://fanuel:Kbsdaf123!@cluster0.xzjgpxo.mongodb.net/")



entries = []
@app.route("/", methods = ["GET", "POST"])

def home():
    if request.method == "POST":
        content = request.form.get("post")
        date = datetime.datetime.today().strftime("%Y-%m-%d")
        entries.append((content, date))
    entries_format = [
        (entry[0],
        entry[1],
        datetime.datetime.strptime(entry[1],"%Y-%m-%d").strftime("%b %d"))
        for entry in entries
    ]
    return render_template("home.html", entries = entries_format)