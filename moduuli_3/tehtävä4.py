vuosiluku = input("Anna vuosiluku.\n")
vuosiluku = int(str(vuosiluku))
if vuosiluku % 4 == 0:
    if vuosiluku % 100 == 0 and vuosiluku % 400 == 0:
        print("Vuosi on karkausvuosi.")
        exit()
    if vuosiluku % 100 == 0 and vuosiluku % 400 != 0:
        print("Vuosi ei ole karkausvuosi")
    else:
        print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")
