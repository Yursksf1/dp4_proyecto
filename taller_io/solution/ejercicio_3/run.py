"""
Con la lista de comunidades.csv generar una página html por cada persona que contengan el nombre de la persona y la visualización de la imagen.
"""

archivo = open("community.csv", "r")
lines = archivo.read().split('\n')
for line in lines:
    row = line.split(',')
    print(row)
    name = "{}.html".format(row[1])
    f = open(name, "w")
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
    """.format(row[0], row[1], row[2])
    f.write(content)
    f.close()
