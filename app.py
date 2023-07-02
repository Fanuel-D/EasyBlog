from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import datetime
import certifi

app = Flask(__name__)
client = MongoClient("mongodb+srv://fanuel:Kbsdaf123!@cluster0.xzjgpxo.mongodb.net/", tlsCAFile=certifi.where())
app.db = client.myblog

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        content = request.form.get("post")
        date = datetime.datetime.today().strftime("%Y-%m-%d")
        app.db.entries.insert_one({"post": content, "date": date})

    entries_format = [
        (entry["post"], entry["date"], datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d"))
        for entry in app.db.entries.find({})
    ]
    return render_template("home.html", entries=entries_format)


@app.route("/calendar")
def calendar():
    return render_template('cal.html')


@app.route("/posts")
def get_posts():
    date = request.args.get('date')
    posts = app.db.entries.find({"date": date})
    response = []
    for post in posts:
        response.append({
            "post": post["post"],
            "date": post["date"]
        })
    return jsonify(response)


@app.route("/bookmarks")
def bookmarks():
    return render_template('bookmarks.html')


if __name__ == '__main__':
    app.run()
