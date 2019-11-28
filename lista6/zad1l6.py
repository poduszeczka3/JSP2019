import trojkat as tr

def main(args):
    print("Wpisz rosnąco długości boków trójkąta:")
    a=float(input())
    b=float(input())
    c=float(input())
    if a>0 and b>0 and c>0 and a+b > c:
        print("Obwód trójkąta:\t", tr.obwod(a,b,c))
        print("Pole trójkąta:\t", tr.pole(a,b,c))
        print("Ten trójkąt jest:\t", tr.boki(a,b,c))
        print("Ten trójkąt jest:\t", tr.katy(a,b,c))
    else: print("Nie ułożę z tych boków trójkąta :(")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))