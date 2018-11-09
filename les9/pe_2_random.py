import random

def monopolyworp(aantal = 0):
    dobbel1 = random.randint(1, 6);
    dobbel2 = random.randint(1, 6);
    som = dobbel1 + dobbel2;

    if dobbel1 == dobbel2:
        aantal += 1;

        if aantal >= 3:
            print(str(dobbel1) + " + " + str(dobbel2) + " = (direct naar de gevangenis)");
            return;
        else:
            print(str(dobbel1) + " + " + str(dobbel2) + " = " + str(som) + " (dubbel)");
            monopolyworp(aantal);

    else:
        print(str(dobbel1) + " + " + str(dobbel2) + " = " + str(som) + " ");

monopolyworp();