file = open("kaartnummers.txt");

count = 0;
biggest = 0;
biggest_line = 0;

for i, line in enumerate(file):
    card_number = int(line.split(", ")[0]);

    if card_number > biggest:
        biggest = card_number;
        biggest_line = i;

    count += 1;

print("Deze file telt " + str(count) + " regels");
print("Het grootste kaartnummer is: " + str(biggest) + " en dat staat op regel " + str(biggest_line + 1));