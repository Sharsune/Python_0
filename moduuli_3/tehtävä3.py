sukupuoli = input("Oletko mies vai nainen?\n")
hemog = input("Hemoglobiiniarvosi?\n")
hemog = int(str(hemog))
if sukupuoli == "Mies" or sukupuoli == "mies" and hemog > 195:
    print("Hemoglobiiniarvosi on korkea.")
elif sukupuoli == "Mies" or sukupuoli == "mies" and hemog < 195 and hemog > 134:
    print("Hemoglobiiniarvosi on normaali.")
elif sukupuoli == "Mies" or sukupuoli == "mies" and hemog < 134:
    print("Hemoglobiiniarvosi on alhainen.")
elif sukupuoli == "Nainen" or sukupuoli == "nainen" and hemog > 175:
    print("Hemoglobiiniarvosi on korkea.")
elif sukupuoli == "Nainen" or sukupuoli == "nainen" and hemog < 175 and hemog > 117:
    print("Hemoglobiiniarvosi on normaali.")
elif sukupuoli == "Nainen" or sukupuoli == "nainen" and hemog < 117:
    print("Hemoglobiiniarvosi on alhainen.")