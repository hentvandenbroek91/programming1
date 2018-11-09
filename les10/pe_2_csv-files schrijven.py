import csv
import datetime

bestand = 'inloggers.csv';
file = open(bestand, "w+");
writer = csv.writer(file);

while True:
    naam = raw_input("Wat is je achternaam? ");

    if naam == "einde":
        break;

    voorl = raw_input("Wat zijn je voorletters? ");
    gbdatum = raw_input("Wat is je geboortedatum? ");
    email = raw_input("Wat is je e-mail adres? ");
    nu = datetime.datetime.today();

    writer.writerow([nu.strftime("%a %d %b %Y, %X"), naam, voorl, gbdatum, email]);