#wszystkie znaki identyczne z pierwszym zamieniam na '$' oprócz pierwszego

print("Napisz coś")
a = input()
znak1 = a[0]
print("pierwszy znak:", znak1)
zmieniony_wyraz = a.replace(znak1, "$")
print(znak1 + zmieniony_wyraz[1:])
