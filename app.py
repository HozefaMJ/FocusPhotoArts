import os
from flask import Flask, render_template, request, redirect
import requests
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

    requests.post(
        "https://api.mailgun.net/v3/sandboxc0477641953d478e97d3438bba118e0b.mailgun.org/messages",
        auth=("api", "9932e02af2348fa99b2af60a5a3f900b-d5e69b0b-70ba3b86"),
        data={"from": "Mailgun Sandbox <postmaster@sandboxc0477641953d478e97d3438bba118e0b.mailgun.org>",
              "to": "HOZEFA JAORAWALA <hozefa.jaorawala@somaiya.edu>",
              "subject": "New Website Query",
              "text": "Hi FocusPhotoArts you have a new query from " + name +
              ". His/Her email is " + email +
              ". His/Her message is " + message})

    return "success"


if __name__ == '__main__':
    app.run()
