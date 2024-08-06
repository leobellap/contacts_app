from flask import Flask, render_template, request
from db import save_contact, search, delete


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/new")
def new():
    return render_template("new.html")


@app.route("/created", methods=["post"])
def created():
    data = request.form
    save_contact(data)
    return render_template("success.html")


@app.route("/search", methods=["post"])
def search_user():
    data = request.form
    search(data)
    if search(data):
        return render_template("contact.html", contact_data=search(data))
    else:
        return render_template("failed.html")


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/delete", methods=["post"])
def delete_contact():
    data = request.form
    delete(data)
    return render_template("/success.html")
