import csv

file = open("gamers.txt");
reader = csv.reader(file, delimiter=';');

score = ["Speler", "00-00-0000", 0];
for row in reader:
    if row[2] > score[2]:
        score = row;

print(score);