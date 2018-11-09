import xmltodict

file = open("stations.xml")
xml = xmltodict.parse(file)

print("Dit zijn de codes en types van de 4 stations:")
for station in xml['Stations']['Station']:
    print("{}  \t - {}".format(station['Code'], station['Type']))

print("")
print("Dit zijn alle stations met een of meer synoniemen:")
for station in xml['Stations']['Station']:
    if station['Synoniemen']:
        print("{}  \t - {}".format(station['Code'], station['Synoniemen']))

print("")
print("Dit is de langste naam van elk station:")
for station in xml['Stations']['Station']:
    print("{}  \t - {}".format(station['Code'], station['Namen']['Lang']))