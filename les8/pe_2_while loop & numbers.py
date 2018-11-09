while True:
    woord = raw_input("Geef een string van vier letters: ");

    if len(woord) == 4:
        print("Inlezen van correcte string: " + woord + " is geslaagd");

        break;

    print(woord + " heeft " + str(len(woord)) + " letters");