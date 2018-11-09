cijfers = {
    "Hent": 10,
    "Bas": 9.5,
    "Gino": 1,
    "Furgil": 5.5,
    "Rutger": 9.5,
    "Lucas": 6,
    "Patrick": 2,
    "Vincent": 8
}

for naam in cijfers:
    cijfer = float(cijfers[naam]);

    if cijfer > 9:
        print(naam +  ": " + str(cijfer))