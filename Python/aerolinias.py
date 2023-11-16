import sys
import csv
i.lower() = sys.argv[1]
with open('aerolineas.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        iata = row[0]
        name = row[2]
        
        if i  == name:
            print(iata)
