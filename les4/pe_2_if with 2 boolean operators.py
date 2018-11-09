leeftijd = int(raw_input("Geef je leeftijd: "));
paspoort = raw_input("Paspoort: ");

if leeftijd >= 18 and paspoort == "ja":
    print("Gefeliciteerd, je mag stemmen!");
else:
    print("Helaas");