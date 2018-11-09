def namen():
    namen = {};

    while True:
        naam = raw_input("Volgende naam: ");

        if len(naam) == 0:
            break;

        if naam in namen:
            namen[naam] += 1;
        else:
            namen[naam] = 1;

    for naam in namen:
        print("Er is " + str(namen[naam]) + " student met de naam " + naam);

namen();