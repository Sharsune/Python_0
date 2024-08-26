import random

n = 1
c = 1
while n:
    if c == 1:
        vastaus = random.randint(1,10)
    arvaus = input("Arvaa numero 1-10 väliltä.\n")
    arvaus = int(arvaus)
    if arvaus == vastaus:
        print("Oikein!")
        exit()
    elif arvaus < vastaus:
        print("Liian pieni arvaus")
        c = c + 1
    elif arvaus > vastaus:
        print("Liian suuri arvaus")
        c = c + 1