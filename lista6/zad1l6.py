def obwod(a,b,c):
    o=a+b+c
    return o

def pole(a,b,c):
    p=(a+b+c)/2
    P=(p*(p-a)*(p-b)*(p-c))**(0.5)
    return P

def boki(a,b,c):
    if a != b and b!=c and c!=a: n = "różnoboczny"
    elif a==b and a==c and b==c: n = "równoboczny"
    else: n = "równoramienny"
    return n

def katy(a,b,c):
    if a**2+b**2 > c**2: k = "ostrokątny"
    if a**2+b**2 == c**2: k = "prostokątny"
    if a**2+b**2 < c**2: k = "rozwartokątny"
    return k

def main(args):
    print("Wpisz rosnąco długości boków trójkąta:")
    a=int(input())
    b=int(input())
    c=int(input())
    if a>0 and b>0 and c>0 and a+b > c:
        print("Obwód trójkąta:\t", obwod(a,b,c))
        print("Pole trójkąta:\t", pole(a,b,c))
        print("Ten trójkąt jest:\t", boki(a,b,c))
        print("Ten trójkąt jest:\t", katy(a,b,c))
    else: print("Nie ułożę z tych boków trójkąta :(")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))