def convert(bensa):
    bensa = bensa * 3.785
    return bensa

while True:
    bensa = float(input("Anna bensan määrä galloina."))
    if bensa < 0:
        exit()
    litrat = convert(bensa)
    print(litrat ,"litraa.")