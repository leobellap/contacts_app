from flask import Flask, render_template, request
from db import save_contact, search, delete, show_all


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index/index.html")


@app.route("/new")
def new():
    return render_template("contacts/new.html")


@app.route("/created", methods=["post"])
def created():
    data = request.form
    save_contact(data)
    return render_template("status/success.html")


@app.route("/search", methods=["post"])
def search_user():
    data = request.form
    search(data)
    if search(data):
        return render_template("contacts/contact.html", contact_data=search(data))
    else:
        return render_template("status/failed.html")


@app.route("/success")
def success():
    return render_template("status/success.html")


@app.route("/delete", methods=["post"])
def delete_contact():
    data = request.form
    delete(data)
    return render_template("status/success.html")


@app.route("/delete_all", methods=["post"])
def delete_contact_all():
    data = request.form
    delete(data)
    return render_template("status/success_all.html")


@app.route("/all")
def all():
    data = show_all()
    return render_template("contacts/all.html", contacts_data=data)
