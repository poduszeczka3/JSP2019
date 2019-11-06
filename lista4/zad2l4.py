lista = [] 
n = int(input("Wpisz ilość elementów listy: ")) 

for i in range(0, n): 
    element = int(input()) 
    lista.append(element)

print()

lista = list(dict.fromkeys(lista)) #Usuwanie powtórek
print("lista bez powtórek:")
print(lista)