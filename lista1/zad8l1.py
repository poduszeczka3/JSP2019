print("Wpisz pierwszą liczbę:")
a=float(input())
print("Wpisz drugą liczbę, mniejszą od poprzedniej:")
b=float(input())
if a>b:
    Z=a%b
    Z2=Z**2+3*Z
    print(Z2)
else:
    print("Ty imbecylu! Przecież liczba" ,b, "nie jest mniejsza od", a)