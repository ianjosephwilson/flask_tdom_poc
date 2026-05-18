from string.templatelib import Template

from flask import Flask
from flask_tdom import render_template


app = Flask(__name__)


def Layout(children: Template) -> Template:
    return t"""<!doctype html>
<html lang="en-US">
<head><meta charset="utf8"></head>
<body>
{children}
</body>
</html>
"""


@app.route("/")
def hello_world():
    return render_template(t"<{Layout}><p>Hello, World!</p></{Layout}>")
