check = 1

while True:
    luku = int(input("Anna kokonaisluku."))
    if luku == 0 or luku == 1:
        print(luku, "Ei ole alkuluku.")
    elif luku > 1:
        for i in range(2, luku):
            if (luku % i) == 0:
                check = 2
                break
    if check == 2:
        check = 1
        print("Luku ei ole alkuluku.")
    elif check == 1:
        print("Luku on alkuluku.")