lentoasemat = {"Helsinki-Vantaa":"EFHK",
           "Berliini":"EDDB",
           "Tukholma":"ESSA",
            "Lontoo":"EGLC",
            "Reykjavik":"BIRK",
            "Kööpenhamina":"EKCH"}
while True:
    x =input("Anna jokin seuraavista komennoista: Uusi lentoasema, Haku tai Lopeta.\n")
    if x.lower() == "uusi lentoasema":
        uusi_koodi = input("Anna uuden lentoaseman ICAO-koodi:")
        uusi_asema = input("Anna uuden lentoaseman nimi:")
        lentoasemat[uusi_asema] = uusi_koodi
    elif x.lower() == "haku":
        koodi = input("Anna ICAO-koodi:")
        for i, code in lentoasemat.items():
            if code == koodi:
                print(f"Koodi vastaa lentoasemaa: {i}.")
                break
    elif x.lower() == "lopeta":
        exit()