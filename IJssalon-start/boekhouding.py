import csv
from helper import *
from presentatie import * 




producten = { 
    "Aardbeien-ijs-totaal": 1000,
    "Vanille-ijs-totaal": 2000,
    "Chocolade-ijs-totaal": 1500,
    "Waterijsjes-totaal": 750
}

totaal_inkomsten = som(producten)

with open('boekhouding.csv', 'w', newline='') as csvfile:
    for key, value in producten.items():
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([key,value])
        
print(totaal_inkomsten)
presenteer(producten, totaal_inkomsten)

