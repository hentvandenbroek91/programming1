def seizoen(maand):
    if 3 <= maand <= 5:
        return "lente";
    if 6 <= maand <= 8:
        return "zomer";
    if 9 <= maand <= 11:
        return "herfst";
    if maand == 12 or 1 <= maand <= 2:
        return "winter";

for i in range(1, 13, 1):
    print(str(i) + ", " + seizoen(i));