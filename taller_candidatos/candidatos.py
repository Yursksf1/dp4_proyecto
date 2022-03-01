from flask import (
    Flask,
    redirect,
    url_for,
    flash,
    request,
    render_template
)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/candidato/<name>")
def get_candidate(name):
    content = ""
    return content

if __name__ == '__main__':
   app.run()