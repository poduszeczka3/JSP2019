# zad 9 lista 3

import pprint

print("podaj rozmiar macierzy")
print("podaj m (pionowy)")
m = int(input())
print("podaj n (poziomy)")
n = int(input())


macierz = list(list(range(1*i,(n+1)*i, i)) for i in range(1,m+1))
pprint.pprint(macierz)