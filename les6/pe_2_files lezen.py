file = open("kaartnummers.txt");

for line in file:
    line = line.rstrip("\n");
    values = line.split(", ");

    print(values[1] + " heeft kaartnummer: " + values[0]);

file.close();