import numpy as np
from random import randint

N = int(input("Wpisz wielkość tablicy N: "))
M = int(input("Wpisz górną granicę tablicy M (M>=N): "))

if M>N or M==N:
    x = [randint(0, M) for i in range(0, N)]
    print("Wygenerowana lista to:",x)

    def f(lista):
        sorted_idx = sorted(range(len(lista)), key=lambda k: lista[k])
        return sorted_idx
    print("Posortowana lista to: ",f(x))

    x_argsort = list(np.argsort(x))
    print("Przy użyciu argsort():",x_argsort)
else: print("Nie da się tego posortować!")