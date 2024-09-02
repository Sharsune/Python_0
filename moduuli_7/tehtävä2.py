nimet = set()
while True:
    nimi = input("Anna nimi:")
    if nimi == "":
        break
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        nimet.add(nimi)
        print("Uusi nimi")
for i in nimet:
    print(i)