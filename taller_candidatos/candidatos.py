from flask import (
    Flask,
    redirect,
    url_for,
    flash,
    request,
    render_template
)
import csv

lista = []
with open('candidatos.csv') as File:
    reader = csv.reader(File)
    for row in reader:
        lista.append(row)

app = Flask(__name__)


@app.route("/")
def index():
    candidatos = []
    for elemento in lista:
        candidatos.append(
            {
                "id": elemento[0],
                "name": elemento[1]
            }
        )

    return render_template("index.html", lista=candidatos)


@app.route("/candidato/<id>")
def get_candidate(id):
    candidato = None
    nombre = "No se encontro el nombre"
    descripcion = "No se encontro alguna descripcion"
    for elemento in lista:
        if elemento[0] == id:
            candidato = elemento

    if candidato:
        nombre = candidato[1]
        descripcion = candidato[2]


    return render_template(
        "candidato.html",
        candidato=candidato,
        nombre=nombre,
        descripcion=descripcion
    )

if __name__ == '__main__':
   app.run()