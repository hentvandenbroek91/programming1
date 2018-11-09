def convert(celcius):
    return celcius * 1.8 + 32;

def table(min, max):
    print("  F\t    C");
    for i in range(min, max + 1, 10):
        print("{:5}\t {:5}".format(convert(i), i));

table(-30, 40);