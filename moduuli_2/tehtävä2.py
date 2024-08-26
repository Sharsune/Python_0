import math

säde_str = input("Mikä on ympyrän säde?\n")
säde = float(säde_str)
pinta_ala = float(math.pi * (säde*2))
print("Pinta-ala on " + str(pinta_ala) + ".")
