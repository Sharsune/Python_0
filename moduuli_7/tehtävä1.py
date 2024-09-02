vuodenajat = ("talvi","kevät","kesä","syksy")
numero = int(input("Anna kuukauden numero (1-12):"))
vuodenaika = 0
if numero == 12 or numero == 1 or numero == 2:
    vuodenaika = vuodenajat[0]
if numero == 3 or numero == 4 or numero == 5:
    vuodenaika = vuodenajat[1]
if numero == 6 or numero == 7 or numero == 8:
    vuodenaika = vuodenajat[2]
if numero == 9 or numero == 10 or numero == 11:
    vuodenaika = vuodenajat[3]
print(f"{numero}. on {vuodenaika}.")