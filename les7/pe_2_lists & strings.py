line = "";
strings = [];

while True:
    line = raw_input("Text: ");

    if line == "":
        break;

    strings.append(line);

fourletterstrings = [];

for string in strings:
    if len(string) == 4:
        fourletterstrings.append(string)

print("De nieuw-gemaakte lijst met alle vier-letter strings is: " + str(fourletterstrings));