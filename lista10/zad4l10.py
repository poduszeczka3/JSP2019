import xml.dom.minidom as rxml

pytanie = input("Czy chcesz wprowadzać ręcznie ścieżkę do pliku? (y/n): ")

if pytanie=="n":
    sciezka = "kursy_walut.xml"
elif pytanie=="y":
    sciezka = input("Podaj pełną ścieżkę do pliku: ")

doc = rxml.parse(sciezka)
print("")
print(doc.firstChild.tagName, "(dostepne kursy):")
print("-----------------------------------")

nazwawaluty = doc.getElementsByTagName('nazwa_waluty')
kurswaluty = doc.getElementsByTagName('kurs_sredni')

for elem in range(0,35):
    print(str(elem+1)+".",nazwawaluty[elem].firstChild.data, ":", kurswaluty[elem].firstChild.data)
print("-----------------------------------")
    
pytanie2 = input("chcesz przeliczyc PLN na wybrana walute? (y/n): ")
lista100 = [9,13,16,24,32,33]
lista10000 = [31]

if pytanie2 == "y":
    pytanie3 = int(input("na jaką walutę chcesz przeliczyc? (podaj numer z tabeli): ")) - 1
    wybrany_kurs = kurswaluty[pytanie3].firstChild.data
    wybrany_kurs = wybrany_kurs.replace(",",".")
    wybrana_waluta = nazwawaluty[pytanie3].firstChild.data
    
    pytanie4 = float(input("podaj kwotę w PLN jaką chcesz przeliczyć: "))

    if pytanie3 in lista100:
        kursowanie = float(wybrany_kurs)/100.
    elif pytanie3 in lista10000:
        kursowanie = float(wybrany_kurs)/10000.
    else:
        kursowanie = float(wybrany_kurs)
    
    wynik = pytanie4/kursowanie
    print("")
    print(pytanie4, "PLN w przeliczeniu na", wybrana_waluta, ":")
    print(wynik)

print("")
pytanie5 = input("chcesz przeliczyć wybraną walutę na inną wybraną walutę? (y/n): ")

if pytanie5 == "y":
    pytanie7 = int(input("z jakiej waluty chcesz przeliczyc? podaj numer z tabeli: ")) - 1
    wybrana_podstawa_kurs = kurswaluty[pytanie7].firstChild.data
    wybrana_podstawa_kurs = wybrana_podstawa_kurs.replace(",",".")
    wybrana_podstawa_waluta = nazwawaluty[pytanie7].firstChild.data
    
    pytanie6_5 = input("Chcesz przeliczyć na PLN? (y/n): ")
    if pytanie6_5 == "n":
        pytanie6 = int(input("na jaką walutę chcesz przeliczyc? podaj numer z tabeli: ")) - 1
        wybrany_kurs = kurswaluty[pytanie6].firstChild.data
        wybrany_kurs = wybrany_kurs.replace(",",".")
        wybrana_waluta = nazwawaluty[pytanie6].firstChild.data
    
        pytanie8 = float(input("podaj kwotę jaką chcesz przeliczyć: "))
    
        if pytanie6 in lista100:
            kursowanie2 = float(wybrany_kurs)/100.
        elif pytanie6 in lista10000:
            kursowanie2 = float(wybrany_kurs)/10000.
        else:
            kursowanie2 = float(wybrany_kurs)
    
        if pytanie7 in lista100:
            kursowanie3 = float(wybrana_podstawa_kurs)/100.
        elif pytanie7 in lista10000:
            kursowanie3 = float(wybrana_podstawa_kurs)/10000.
        else:
            kursowanie3 = float(wybrana_podstawa_kurs)
    
        przelicznik = kursowanie3/kursowanie2
        wynik = pytanie8*przelicznik
    
        print("")
        print(pytanie8, wybrana_podstawa_waluta, "w przeliczeniu na", wybrana_waluta, ":")
        print(wynik)
    else:
        pytanie9 = float(input("podaj kwotę jaką chcesz przeliczyć: "))
        kursowanie2 = 1.
    
        if pytanie7 in lista100:
            kursowanie3 = float(wybrana_podstawa_kurs)/100.
        elif pytanie7 in lista10000:
            kursowanie3 = float(wybrana_podstawa_kurs)/10000.
        else:
            kursowanie3 = float(wybrana_podstawa_kurs)
    
        przelicznik = kursowanie3/kursowanie2
        wynik = pytanie9*przelicznik
    
        print("")
        print(pytanie9, wybrana_podstawa_waluta, "w przeliczeniu na PLN:")
        print(wynik)