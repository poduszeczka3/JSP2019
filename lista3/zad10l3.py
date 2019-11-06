for i in range(1,5):
    for j in range(10):
        for k in range(10):
            if i%2==0 and j%2==0 and k%2==0 and 100*i+10*j+k<=400:
                x=100*i+10*j+k
                print(str(x)+",")

x = range(100, 401)
lista=[]
for i in x:
    y = str(i)
    setki = str(y[0])
    setki = int(setki)
    dziesiatki = str(y[1])
    dziesiatki = int(dziesiatki)
    jednosci = str(y[2])
    jednosci = int(jednosci)
    if setki%2 == 0 and dziesiatki%2 == 0 and jednosci%2==0:
        lista.append(i)

print (lista)