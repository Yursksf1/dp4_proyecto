# -*- coding: utf-8 -*-
f = open("song.txt", "r")
cancion = f.read()
cancion_separada_por_lineas = cancion.split("\n")

diccionario_de_palabras = {}
for linea in cancion_separada_por_lineas:
    new_linea = linea.replace("’", '').replace(",", '').replace("!", '').lower()
    palabras = new_linea.split(" ")
    for palabra in palabras:
        if palabra in diccionario_de_palabras:
            diccionario_de_palabras[palabra] = diccionario_de_palabras[palabra] + 1
        else:
            diccionario_de_palabras[palabra] = 1

print(diccionario_de_palabras)

