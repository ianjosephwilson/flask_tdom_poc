from string.templatelib import Template

from flask import Flask
from flask_tdom import render_template, FlaskCtx


app = Flask(__name__)


def Layout(children: Template) -> Template:
    flask_info = FlaskCtx.get()
    return t"""<!doctype html>
<html lang="en-US">
<head><meta charset="utf8"></head>
<body>
<!-- check that flask template context is set -->
{flask_info['request'].host_url}
{children}
</body>
</html>
"""


@app.route("/")
def hello_world():
    return render_template(t"<{Layout}><p>Hello, World!</p></{Layout}>")
