import random

def noppa():
    i = random.randint(1,6)
    return i

while True:
    heitto = noppa()
    print(heitto)
    if heitto == 6:
        exit()