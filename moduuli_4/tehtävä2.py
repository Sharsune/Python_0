tuuma = input("Anna tuumat.\n")
tuuma = float(tuuma)
while tuuma > 0:
    if (tuuma) < 0:
        exit()
    cm = float(tuuma * 2.54)
    print(cm)
    tuuma = input("Anna tuumat.\n")
    tuuma = float(tuuma)