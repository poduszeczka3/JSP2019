#sortowanie listy ze względu na jej drugi element: sorted

lista = [(2,8),(5,5),(9,3),(1,0),(3,2),(6,4),(1,9),(10,3),(2,3),(1,7)]
lista = sorted(lista, key=lambda x: x[1])
print(lista)