import os
from flask import Flask, render_template, request, redirect
import smtplib

app = Flask(__name__, template_folder='./templates',
            static_folder='./templates/static')


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def form():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    query = "Hi FocusPhotoArts you have a new query from " + name + \
        ". His/Her email is " + email + \
        ". His/Her message is " + message

    print(query)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("hozefa.queryinfo@gmail.com", "HozefaJ@96")
    server.sendmail("hozefa.queryinfo@gmail.com",
                    "hozefa24imp@gmail.com", query)

    return("success")
