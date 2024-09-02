import random


nopat = input("Anna noppien määrä:")
nopat = int(nopat)
summa = 0
for i in range(nopat):
    heitto = random.randint(1,6)
    summa += heitto

print("Heittojen summa on: " + str(summa) + ".")
