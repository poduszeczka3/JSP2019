print("podaj q")
q = float(input())

print("podaj n")
n = float(input())

print("podaj a1")
a1 = float(input())

def Suma1(a1,q,n):
    return a1*((1.-(q**n))/(1.-q))
def Suma2(a1,n):
    return a1*n

if q==1:
    print("suma = ", Suma2(a1,n))
else:
    print("suma = ", Suma1(a1,q,n))