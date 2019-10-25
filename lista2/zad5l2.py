#w środek napisu wstawiam inny napis

print("Napisz coś")
napis = input()
n = len(napis) #len liczy liczbę wpisanych znaków
srodek = round(n/2)
napis2 = "urw"
print(napis[0:srodek] + napis2 + napis[srodek:n])