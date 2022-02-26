from flask import Flask
from markupsafe import escape

app = Flask(__name__)

lista = [
    ['Adriana Moya', 'adrifermo', 'https://www.python.org.co/usuarios/adrianamatallanam/adriana-matallana.jpg'],
    ['Yurley Sanchez', 'yurs_ksf1', 'https://www.python.org.co/usuarios/yurs_ksf1/yurley.jpg'],
]

@app.route("/")
def hello_world():
    return "<p>este es mi proyecto en flask</p>"


@app.route("/segunda_ruta")
def second_route():
    # to something
    content = """
    <!doctype html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport"
                  content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>Document</title>
        </head>
        <body>
            <h1> {} </h1>
            <p> {} </p>
            <img src="{}" alt="">
            <p> esta persona pertenece a la comunidad de python colombia </p>
        </body>
    </html>
    """.format("Yurley", "Yurley K Sanchez F", 'https://www.python.org.co/usuarios/yurs_ksf1/yurley.jpg')
    return content


@app.route("/name/<name>")
def hello(name):
    persona = ['', '', '']
    for i in lista:
        if name == i[1]:
            persona = i

    content = """
        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport"
                      content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                <title>Document</title>
            </head>
            <body>
                <h1> {} </h1>
                <p> {} </p>
                <img src="{}" alt="">
                <p> esta persona pertenece a la comunidad de python colombia </p>
            </body>
        </html>
    """.format(persona[0], persona[1], persona[2])
    return content

if __name__ == '__main__':
   app.run()