def gemiddelde(line):
    words = line.split(" ");

    sum = 0;
    for word in words:
        sum += len(word);

    return sum / len(words);

line = raw_input("Zin: ");
print(gemiddelde(line));