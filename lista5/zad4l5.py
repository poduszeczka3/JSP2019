klucz={'a':'y','e':'i','i':'o','o':'a','y':'e'}

def szyfr_eli(klucz, slow):
 
    # pozbywanie sie powtarzajacych sie liter w kluczu
 
    unikalne_litery_w_kluczu = []
 
    for litera in klucz: 
        if litera not in unikalne_litery_w_kluczu:
            unikalne_litery_w_kluczu.append(litera)
 
    # sklejenie listy liter w jeden tekst
    unikalne_litery_w_kluczu = ''.join(unikalne_litery_w_kluczu)            
 
    # usuwanie liter klucza z alfabetu
 
    alfabet = list('abcdefghijklmnoprstuvwxyz')
 
    for litera in unikalne_litery_w_kluczu:
        if litera in alfabet: # na wypadek gdyby trafiło się coś co nie jest literą
            alfabet.remove(litera)
 
    # sklejenie listy liter w jeden tekst
    reszta_alfabetu = ''.join(alfabet)
 
    print(unikalne_litery_w_kluczu + reszta_alfabetu)