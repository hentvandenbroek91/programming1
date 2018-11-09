uurloon = float(raw_input('Uurloon: '));
uren = float(raw_input('Aantal uur: '));

print('Wat verdien je per uur: ' + str(uurloon));
print('Hoeveel uur heb je gewerkt: ' + str(uren));
print(str(uren) + ' uur werken levert ' + str(uurloon * uren) + ' Euro op');
