from operator import truediv

luvut = []
c = 0
luku = int(input("Anna uusi luku.\n"))

while True:
    luvut.append(luku)
    luku = input("Anna uusi luku.\n")
    c += 1
    if luku == "":
        break
    luku = int(luku)

luvut.sort(reverse=True)
if c < 5:
    for i in range(0, c):
        print(luvut[i])
else:
    for i in range(1, 5):
        print(luvut[i])
