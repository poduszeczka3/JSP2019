import urllib.request

strona = input("podaj adres strony w formacie 'http://www.': ")
x = str(urllib.request.urlopen(strona).getcode())

if x == "200": print("Taka strona istnieje :)")
else: print("Nie ma takiej strony")