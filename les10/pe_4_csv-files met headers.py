import csv

file = open("producten.txt", "w");
writer = csv.writer(file);

writer.writerow(["Artikelnummer", "Artikelcode", "Naam", "Voorraad", "Prijs"]);

producten = [
    [121, "ABC123", "Higlight Pen", 231, 0.56],
    [123, "PQR678", "Nietmachine", 587, 9.99],
    [128, "ZYX163", "Bureaulamp", 34, 19.95],
    [137, "MLK709", "Monitorstandaard", 66, 32.50],
    [271, "TRS665", "Ipad hoes", 155, 19.01],
]

for product in producten:
    writer.writerow(product);

file.close();

file2 = open("producten.txt");
reader = csv.reader(file2);

reader.next();
row = reader.next();

product = [row[0], row[1], row[2], row[3], row[4]];
duurste = product;
voorraad = product;
totaal = int(product[3]);

for row in reader:
    if float(row[4]) > float(duurste[4]):
        duurste = row;

    if int(row[3]) < int(voorraad[3]):
        voorraad = row;

    totaal += int(row[3]);

print("Het duurste artikel is " + duurste[2] + " en die kost " + duurste[4] + " Euro");
print("Er zijn slechts " + voorraad[3] + " exemplaren in voorraad van het product met nummer " + voorraad[0]);
print("In totaal hebben wij " + str(totaal) + " producten in ons magazijn liggen");