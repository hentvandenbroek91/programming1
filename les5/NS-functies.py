def standaardtarief(afstand):
    if afstand < 0:
        return 0.0;

    if afstand > 50:
        return 15 + afstand * 0.6;

    return afstand * 0.8;


def ritprijs(leeftijd, weekend, afstand):
    prijs = standaardtarief(afstand);

    if leeftijd < 12 or leeftijd >= 65:
        if weekend:
            prijs *= 0.65;
        else:
            prijs *= 0.7;
    else:
        if weekend:
            prijs *= 0.6;

    return prijs;

for age in [11, 12, 64, 65]:
    print('leeftijd: ' + str(age))
    print('het is weekend en 30km reizen ' + str(ritprijs(age, True, 30)))
    print('het is geen weekend en 30km reizen ' + str(ritprijs(age, False, 30)))
    print('het is weekend en 70km reizen ' + str(ritprijs(age, True, 70)))
    print('het is geen weekend en 70km reizen ' + str(ritprijs(age, False, 70)))
    print('het is weekend en -3km reizen ' + str(ritprijs(age, True, -3)))
    print('het is geen weekend en -3km reizen ' + str(ritprijs(age, False, -3)))
    print(' ----- ')