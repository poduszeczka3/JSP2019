liczba1 = list(input())
liczba1.reverse ()
tysiace = ('tysiąc','tysiące','tysięcy')
setki = ('sto','dwieście','trzysta','czterysta','pięćset','sześćset','siedemset','osiemset','dziewięćset')
cyfry = ('zero','jeden','dwa','trzy','cztery','pięć','sześć','siedem','osiem','dziewięć','dziesięć','jedenaście','dwanaście','trzynaście','czternaście','piętnaście','szesnaście','siedemnaście','osiemnaście','dziewiętnaście')
dziesiatki = ('dwadzieścia','trzydzieści','czterdzieści','pięćdziesiąt','sześćdziesiąt','siedemdziesiąt','osiemdziesiąt','dziewięćdziesiąt')
slownie = []
for nr, cyfra in enumerate (liczba1):
    if nr in {0,3,6,9}:
        if nr == 3:#sprawdza czy tysiące
            if len (liczba1) > 4 and int (liczba1[nr+1]) == 1:
                slownie.insert (0, tysiace[2])                
            elif 1 < int (cyfra) < 5:
                slownie.insert (0, tysiace[1])
            else:
                slownie.insert (0, tysiace[2])
        if nr+1 < len (liczba1): # Sprawdzam czy to ostatni cyfra
            if int (liczba1[nr+1]) > 1:#sprawdza czy liczba dziesiętna jest powyżej 20                
                if int (cyfra) == 0:
                    continue
                else:
                    slownie.insert (0, cyfry[int (cyfra)])#wpisuje pojedynczą cyfre
            else:# liczby poniżej 20
                if int (cyfra) == 0:
                    continue
                else:# liczby od 1 do 19
                    slownie.insert (0, cyfry[ int(liczba1 [nr+1]+ liczba1 [nr])])
        else:# jeśli to ostatnia cyfra
            if nr > 0 and int (cyfra) == 1:
                if nr == 3:
                    slownie.insert (0, tysiace[0])
            else:
                slownie.insert (0, cyfry [int (cyfra)])
    elif nr in {1,4,7,10}: # reguły dla dziesiątek
        if int(cyfra) == 1 or int (cyfra) == 0:# dla cyfry 0 i 1 nie pisze nic (dla jedynki już wypisano przy poprzednim przebiegu)
            continue
        else: # wypisuje dziesiątki
            slownie.insert (0, dziesiatki[ int (cyfra)-2])
    elif nr in {2,5,8,11}:
        if int (cyfra) == 0:
            continue
        else: # wypisuje setki
            slownie.insert (0, setki[ int (cyfra)-1])
print ("Słownie:"," ".join(slownie))