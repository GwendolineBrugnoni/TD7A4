from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mongo-container:27017")

db = client.flask_db
collection = db.collection


@app.route('/', methods=('GET', 'POST'))
def index():
    data = collection.find_one()
    return str(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
