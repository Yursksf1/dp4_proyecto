"""
Leer el archivo `palabras_a_e_i_o_u.txt` y generar 5 archivos según el contenido que se procese del archivo inicial
Todas la palabras que inicien con a
Todas la palabras que inicien con e
Todas la palabras que inicien con i
Todas la palabras que inicien con o
Todas la palabras que inicien con u

Al finalizar el programa se deben generar estos 5 archivos con su respectivo contenido y un mensaje por consola que tenga el resumen de cuantas palabras inciaron con cada vocal.
"""

def escribir_y_contar(cont, letra, line):
    name_file = "palabas_{}.txt".format(letra)

    f = open(name_file, "a")
    f.write("{} \n".format(line))
    f.close()

    return cont + 1

f = open("palabras_a_e_i_o_u.txt", "r")
lines = f.read().split('\n')

vocales = {
}

for line in lines:
    letra = line[0]
    if letra not in vocales:
        vocales[letra] = 0

    vocales[letra] = escribir_y_contar(vocales[letra], letra, line)

for i in vocales.keys():
    print("estoy imprimiendo el numero de palabras con {}: ".format(i), vocales[i])