#! /usr/local/bin/python3

import os
import os.path
import datetime
import SzyfrCezara
import random

def pesel():
    year = random.randint(1901,2019)
    if year <= 1999:
       month = random.randint(1,12)
    elif year >= 2000:
       month = random.randint(1,12) + 30 # odróżnienie milenium
    odd_months = (1, 3, 5, 7, 8, 10, 12, 21, 23, 25, 27, 28, 30, 32)
    even_months = (4, 6, 9, 11, 24, 26, 29, 31)
 
    if month in odd_months:
       day = random.randint(1,31)
    elif month in even_months:
       day = random.randint(1,30)      
    # dla lutego
    else:
       if year % 4 == 0 and year != 1900:
          day = random.randint(1,29)
       else:
          day = random.randint(1,28)
 
    four_random = random.randint(1000,9999)
    four_random = str(four_random)
 
    y = '%02d' % (year % 100)
    m = '%02d' % month
    dd = '%02d' % day
    a = int(y[0])
    b = int(y[1])
    c = int(m[0])
    d = int(m[1])
    e = int(dd[0])
    f = int(dd[1])
    g = int(four_random[0])
    h = int(four_random[1])
    i = int(four_random[3])
    j = int(four_random[3])
 
    check = a + 3 * b + 7 * c + 9 * d + e + 3 * f + 7 * g + 9 * h + i + 3 * j
 
    if check % 10 == 0:
       last_digit = 0
    else:
       last_digit = 10 - (check % 10)
 
    y = '%02d' % (year % 100)
    m = '%02d' % month
    d = '%02d' % day
    pesel = y+m+d+str(four_random)+str(last_digit)
    return pesel

def sprawdzPesel(pesel):
       return (int(pesel[10])==(100000-sum(x*int(y) for x,y in zip([1,3,7,9,1,3,7,9,1,3],pesel)))%10)

def sprawdzPlec(pesel):
    if int(pesel[-2])%2:
        return 'mezczyzna'
    else:
        return 'kobieta'

def sprawdzDate(pesel):
    dzien = int(pesel[4:6])
    miesiac = int(pesel[2:4])
    if miesiac > 30:
        rok = int("20"+pesel[0:2])
        miesiac -= 30
    elif miesiac <= 12:
        rok = int("19"+pesel[0:2])

    return rok,miesiac,dzien

def zadanie1():
    print("\n> Zadanie 1")
    plik = input("> Podaj plik ze scieżką: ")
    while 1:
        try:
            shift = int(input("> Podaj wartosc przesuniecia do szyfru cezara: "))
            if shift <= 10 and shift >= 1:
                break
            else:
                print("\a% ERROR! Liczba musi byc w przedziale 1-10")
        except ValueError:
            print("\a% ERROR! Podałeś coś co nie jest liczbą całkowitą!")
    if os.path.exists(plik):
        try:
            with open(plik,'r') as of:
                lines = of.readlines()
        except IOError:
            print("\a% ERROR! Nie można otworzyć pliku!")
        if len(lines) == 0: 
            print("> Plik jest pusty!")
            return None
        ciphered = []
        for linia in lines:
            ciphered.append(SzyfrCezara.crypting(linia.split('\n')[0],shift))
        katalog = input("> Podaj katalog zapisu pliku: ")
        now = datetime.datetime.now()
        try:
            outfile = "plik_zaszyfrowany{}_{}{}{}.txt".format(shift,now.year, now.month,now.day)
            if len(katalog) == 0:
                katalog = os.getcwd()
            elif os.path.isdir(katalog) == False:
                os.makedirs(katalog)
            with open(os.path.join(katalog,outfile),'w') as of:
                for linia in ciphered:
                    of.write("{} ".format(linia))    
        except IOError:
            print("\a% ERROR! Nie można zapisać do pliku {}!".format(outfile))        
    else:
        print("> Nie ma takiego pliku!")
    
def zadanie2():
    print("\n> Zadanie 2")
    sciezka = input("> Podaj sciezke do katalogu z zaszyfrowanymi plikami: ")
    if len(sciezka) == 0:
        sciezka = os.getcwd()
    if os.path.isdir(sciezka):
        if sciezka[-1] != '/': sciezka += '/'
        os.system("ls "+sciezka+"plik_zaszyfrowany* > zaszyfrowane.lst")
        with open("zaszyfrowane.lst",'r') as of:
            pliki = of.readlines()
        os.system("rm zaszyfrowane.lst")
        for plik in pliki:
            plik = plik.split('\n')[0]
            with open(plik,'r') as of:
                linie = of.readlines()
            n = int(plik.split("plik_zaszyfrowany")[-1].split('_')[0])
            ymd = plik.split('.')[0].split("_")[-1]
            print("plik_deszyfrowany{}_{}.txt".format(n,ymd))
            with open("plik_deszyfrowany{}_{}.txt".format(n,ymd),'w') as of:
                for linia in linie:
                    linia = linia.split('\n')[0]
                    of.write(SzyfrCezara.crypting(linia,n,decipher=True)+" ")
    else:
        print("\n> Nie ma takiego folderu!")
    
def zadanie3():
    print("\n> Zadanie 3")
    try:
        with open("PESEL.txt",'w') as of:
            for i in range(10):
                pes = pesel()
                of.write("{}\n".format(pes))
                print("Pesel nr {}: {}".format(i,pes))
    except IOError:
        print("\a% ERROR! Nie można zapisać do pliku PESEL.txt!")        

def zadanie4():
    print("\n> Zadanie 4")
    if os.path.exists("PESEL.txt"):
        try:
            with open("PESEL.txt",'r') as of:
                pesele = of.readlines()
        except IOError:
            print("\a% ERROR! Nie można wczytać z pliku PESEL.txt!")  
            return None      
        if len(pesele) == 0: 
            print("> Plik jest pusty!")
            return None
        for pes in pesele:
            try:
                pes = pes.split("\n")[0]
                if sprawdzPesel(pes):
                    data = sprawdzDate(pes)
                    plec = sprawdzPlec(pes)
                    with open("PESEL_DANE.txt",'w') as of:
                        string = "nr PESEL {}:\n data urodzenia {:02d}-{:02d}-{};\t płeć: {}\n".format(pes,data[2],data[1],data[0],plec)
                        of.write(string)
                        print(string)
                    
            except ValueError:
                print("\a% Error! Zły format numeru pesel!")

    else:
        print("\a% ERROR! Nie ma takiego pliku!")

def main():
    #zadanie1()
    #zadanie2()
    zadanie3()
    zadanie4()

if __name__ == "__main__":
    main()