n = 1
c = 1
while n:
    tunnus = input("Syötä käyttäjätunnus.\n")
    salasana = input("Syötä salasana.\n")
    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa")
        exit()
    if c == 5:
        print("Pääsy evätty")
        exit()
    else:
        print("Käyttäjätunnus tai salasana on väärä.")
        c = c + 1