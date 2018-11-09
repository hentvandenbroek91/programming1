def wijzig(letterlijst):
    for index, _ in enumerate(letterlijst):
        letterlijst[index] = '';

    letterlijst[0] = 'd';
    letterlijst[1] = 'e';
    letterlijst[2] = 'f';

lijst = ['a', 'b', 'c'];
print(lijst);
wijzig(lijst);
print(lijst);