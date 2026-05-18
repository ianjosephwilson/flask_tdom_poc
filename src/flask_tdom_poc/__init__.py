from flask import Flask
from flask_tdom import render_template


app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template(t"<p>Hello, World!</p>")
