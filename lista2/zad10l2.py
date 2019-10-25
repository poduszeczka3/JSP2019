print("Naturalne wielokrotności trójki mniejsze od 100 to:")
x = range(0, 100, 3)
lista = []
for i in x:
    lista.append(i)
print(lista)

print("Usunięcie co trzeciego elementu z powyższej listy począwszy od piątego:")
n = len(lista)
lista2 = []
for i in range(4,n,3):
    lista2.append(lista[i]) #tworzy listę zawierającą co 3 element tej pierwszej
lista3 = list(set(lista) - set(lista2))
print(lista3)

print("Średnia arytmetyczna wyrazów z powyższej listy to:")
suma = sum(lista3)
średnia = suma/len(lista3)
print(round(średnia,4))