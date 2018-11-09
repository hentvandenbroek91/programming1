som = 0;
aantal = 0;

while True:
    getal = int(raw_input("Geef een getal: "));

    if getal == 0:
        break;

    som += getal;
    aantal += 1;

print("Er zijn " + str(aantal) + " getallen ingevoerd, de som is: " + str(som));