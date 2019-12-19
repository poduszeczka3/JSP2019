import numpy as np

print("Podaj dane pomiarowe (nazwę pliku plik.txt albo ręcznie po spacji):")
dane1 = input()
print()

if ".txt" in dane1:
    print(dane1)
    
    with open(dane1, 'r') as plik:
        tekst = plik.readlines()
        tekst = [line.rstrip('\n') for line in open(dane1)]
        tekst = list(map(int, tekst))
        print(tekst)
else:
    tekst = list(map(int,dane1.split()))
    print(tekst)

print("Średnia: ", np.mean(tekst))
print("Wariancja: ", np.var(tekst))
print("Odchylenie standardowe: ", np.std(tekst))
