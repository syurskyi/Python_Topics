#!python3

from flask ______ Flask, render_template, request, session, redirect, url_for, escape
______ webbrowser

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
___ index(
    r_ render_template("index.html")

webbrowser.open('http://127.0.0.1:5000')
app.run()