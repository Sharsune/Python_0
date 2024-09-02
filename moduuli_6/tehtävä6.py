import math

def calc_pizza(halkaisija, hinta):
    halkaisija_m = halkaisija / 100
    sade = halkaisija_m / 2
    pinta_ala = math.pi * (sade ** 2)
    yksikköhinta = hinta / pinta_ala
    return yksikköhinta

halkaisija1 = float(input("Anna pizzojen halkaisijat:"))
halkaisija2 = float(input())
hinta1 = float(input("Ja sitten pizzojen hinnat:"))
hinta2 = float(input())
print("Lasketaan...")
pizza1 = calc_pizza(halkaisija1, hinta1)
pizza2 = calc_pizza(halkaisija2, hinta2)
if pizza1 < pizza2:
    print(f"Ensimmäinen pizza antaa paremman vastineen rahalle yksikköhintana:{pizza1:6.2f}e/m^2 vs {pizza2:6.2f}e/m^2")
if pizza1 > pizza2:
    print(f"Toinen pizza antaa paremman vastineen rahalle yksikköhintana:{pizza2:6.2f}e/m^2 vs {pizza1:6.2f}e/m^2")