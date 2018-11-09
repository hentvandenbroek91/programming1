import datetime;

file = open("hardlopers.txt", "a");

nu = datetime.datetime.today();
naam = raw_input("Naam: ");

file.write(nu.strftime("%a %d %b %Y, %X") + ", " + naam + "\n");