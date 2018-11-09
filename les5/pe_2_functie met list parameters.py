def som(getallenLijst):
    som = 0;

    for getal in getallenLijst:
        som += getal;

    return som;

print(som([1, 2, 3]));