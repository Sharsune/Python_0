n = 1
c = 1
while n:
    luku = input("Anna luku.\n")
    a = int(luku)
    c = c + 1
    while c > 1:
        luku = input("Anna luku.\n")
        if str(luku) == "":
            print("Pienin luku: " + str(a) + " ja suurin luku: " + str(b) + ".")
            exit()
        luku = int(luku)
        if c == 2:
            b = luku
        if luku > a and luku > b:
            b = luku
        if luku < a:
            a = luku
        c = c + 1