try:
    aantal = int(raw_input("Aantal personen mee op reis: "));

    if aantal == 0:
        print("Delen door nul kan niet!");
    elif aantal < 0:
        print("Negatieve getallen zijn niet toegestaan!");
    else:
        print("De reis kost " + str(4356 / aantal) + " euro per persoon");
except ValueError:
    print("Gebruik cijfers voor het invoeren van het aantal!");
except:
    print("Onjuiste invoer!");