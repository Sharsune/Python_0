kaupungit = []
c = 0
print("Anna 5 kaupungin nimeä yksi kerrallaan.")

while c < 5:
    kaupunki = input()
    kaupungit.append(kaupunki)
    c += 1
for i in range(5):
    print(kaupungit[i])