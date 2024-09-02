import random

def noppa(tahkot):
    i = random.randint(1,tahkot)
    return i

tahkot = int(input("Anna nopan maksimisilmäluku."))
while True:
    heitto = noppa(tahkot)
    print(heitto)
    if heitto == tahkot:
        exit()