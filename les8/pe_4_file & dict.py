def ticker(filename):
    file = open(filename);
    symbols = {};

    for line in file:
        line = line.rstrip("\n");
        values = line.split(":");

        symbols[values[0]] = values[1];

    return symbols;

symbols = ticker("symbols.txt");
print(symbols);

company = raw_input("Enter company name: ");
if company in symbols:
    print("Ticker symbol: " + symbols[company]);
else:
    print("Company not found!");

symbol = raw_input("Enter symbol: ");
for company in symbols:
    x = symbols[company];

    if x == symbol:
        print("Company: " + company);
        exit(0);
print("Symbol not found");