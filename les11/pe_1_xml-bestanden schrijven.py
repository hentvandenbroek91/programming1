import xmltodict

file = open("producten.xml")

xml = xmltodict.parse(file)

for artikel in xml['artikelen']['artikel']:
    print(artikel['naam'])