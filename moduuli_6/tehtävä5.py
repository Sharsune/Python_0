def pariton_pois(lista):
    for i in lista[::-1]:
        if i % 2 != 0:
            lista.remove(i)
    return lista

lista = [10, 5, 88, 7, 1 , 2]
pariton_lista = lista[:]
pariton_lista = pariton_pois(pariton_lista)
print(lista)
print(pariton_lista)