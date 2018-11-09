def kwadraten_som(grondgetallen):
    som = 0;

    for getal in grondgetallen:
        if getal < 0:
            continue;

        som += getal ** 2;

    return som;

print(kwadraten_som([4, 5, 3, -81]));