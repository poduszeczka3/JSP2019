import pprint

print("podaj rozmiar macierzy w kolejności: wiersze, kolumny")
m = int(input())
n = int(input())

macierz = list(list(range(1*i,(n+1)*i, i)) for i in range(1,m+1))
pprint.pprint(macierz)