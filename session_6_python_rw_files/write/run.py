import csv

myData = [["first_name", "second_name", "age"],
          ['Yurley', 'Katerine', '27'],
          ['Maria', 'Cristina', '50']]

myFile = open('example2.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)

print("Writing complete")