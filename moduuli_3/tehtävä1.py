kalapituus = input("Kuinka pitkä kuha on senttimetreinä?\n")
if(int(kalapituus) < 37):
    puuttuvap = int(37 - int(kalapituus))
    print("Palauta kala järveen, pituutta puuttui: " + str(puuttuvap) + " cm.")