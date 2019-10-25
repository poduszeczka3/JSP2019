samogloski = "aąeęiouyó"
spolgloski = "bcćdfghjklmnprstwyzżź"
koniec = False


while koniec == False:
    x = input("Podaj literę:")
    if x in spolgloski:
        print ("Litera {} nalezy do spółgłosek".format(x))
        koniec = True
    if x in samogloski:
        print ("Litera {} nalezy do samogłosek".format(x))
        koniec = True
    if koniec == False:
        print ("Nie podałeś prawidłowej litery. Spróbuj ponownie.")