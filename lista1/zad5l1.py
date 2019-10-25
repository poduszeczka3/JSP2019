import numpy as np
print("Porównamy operacje dzielenia bez reszty oraz funkcje 'floor' oraz 'round' na przykładzie dwóch par liczb:")

a=34.
b=35.
c=3.
print("W wyniku dzielenia bez reszty liczby" ,a, "przez liczbę" ,c, "otrzymujemy wartość:", a//c)
print("W wyniku użycia funkcji 'floor' na wynik działania" ,a, "podzielić na" ,c, "otrzymujemy wartość:", np.floor(a/c))
print("W wyniku użycia funkcji 'round' na wynik działania" ,a, "podzielić na" ,c, "otrzymujemy wartość:", round(a/c,2))

print("W wyniku dzielenia bez reszty liczby" ,b, "przez liczbę" ,c, "otrzymujemy wartość:", b//c)
print("W wyniku użycia funkcji 'floor' na wynik działania" ,b, "podzielić na" ,c, "otrzymujemy wartość:", np.floor(b/c))
print("W wyniku użycia funkcji 'round' na wynik działania" ,b, "podzielić na" ,c, "otrzymujemy wartość:", round(b/c,2))

print("Okazuje się, że dzielenie bez reszty oraz funkcja 'floor' dają ten sam wynik, natomiast funkcja 'round' zaokrągla go.")