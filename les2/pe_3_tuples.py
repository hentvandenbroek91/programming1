letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B');
aantal = [0, 0, 0];

for character in letters:
  aantal[ord(character) - 65] += 1;

print(aantal);
