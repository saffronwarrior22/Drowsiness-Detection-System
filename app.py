from flask import Flask, render_template, redirect, url_for
import subprocess
import sys
from threading import Thread
from main import start_detection

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/start")
def start():

    subprocess.Popen([sys.executable, "main.py"])

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)