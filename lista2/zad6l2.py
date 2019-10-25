lista = ["Kasia", "Basia", "Marek", "Darek"]
lista.append("Jozek")

dodaj = ["Ania", "Basia"]
lista.extend(dodaj)

lista.sort()
print(lista)

print("Czwarty student to:", lista[3])
print("Drugi i pierwszy student to:", lista[0], "i", lista[1])

n = len(lista)
print("Przedostatni i ostatni student to:", lista[n-2], "i", lista[n-1])

b = lista.count("Basia")
for i in range(b):
    lista.remove("Basia")

print(lista)
m = len(lista)
print("Ilość studentów na liście wynosi:", m)

lista = tuple(lista) #tworzenie krotki
print(lista)