print("Podaj współczynniki trójmianu kwadratowego ax^2+bx+c:")
a=float(input())
b=float(input())
c=float(input())
if a==0 and b==0 and c==0:
    print("Funkcja jest liniowa i ma nieskończenie wiele miejsc zerowych")
elif a==0 and b==0 and c!=0:
    print("Funkcja jest liniowa i nie ma miejsc zerowych")
elif a==0 and b!=0:
    x=-b/c
    print("Funkcja jest liniowa z miejscem zerowym równym x =",x)
else:
    delta=b**2-4*a*c
    if delta > 0:
        x1=(-b-delta**(1/2))/(2*a)
        x2=(-b+delta**(1/2))/(2*a)
        print("Miejsca zerowe to: x1 =",x1,"i x2 =",x2)
    elif delta == 0:
        x0=-b/(2*a)
        print("Miejsce zerowe to: x0 =",x0)
    elif delta < 0:
        print("Brak rzeczywistych miejsc zerowych :(")
