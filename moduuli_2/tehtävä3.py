import math

kanta_str = input("Mikä on suorakulmion kanta?\n")
korkeus_str = input("Entä korkeus?\n")
kanta = float(kanta_str)
korkeus = float(korkeus_str)
pinta_ala = float(kanta * korkeus)
piiri = float((kanta*2) + (korkeus*2))
print("Piiri on " + str(piiri) + " ja pinta-ala on " + str(pinta_ala) + ".")
