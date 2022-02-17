import csv

with open('example.csv') as File:
    reader = csv.reader(File)
    for row in reader:
        print(row)
print("")

# otra forma de ver el contenido
import csv

results = []
with open('example.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        results.append(row)

    for i in results:
        print i