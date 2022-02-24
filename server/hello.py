from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>este es mi proyecto en flask</p>"


@app.route("/segunda_ruta")
def second_route():
    return "<p>esta es otra ruta</p>"


@app.route("/name/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

if __name__ == '__main__':
   app.run()