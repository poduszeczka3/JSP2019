def ciag_geometryczny(a1,q,n):
    return a1*q**(n-1)

print("Wpisz wartość pierwszego wyrazu ciągu geometrycznego (a1):")
a1 = input()

print("Wpisz wartość iloczynu ciągu geometrycznego (q):")
q = input()

print("Wpisz nunmer wyrazu tego ciągu, którego wartość chcesz znać:")
n = int(input())

if a1 == "":
    a1 = 1
if q == "":
    q = 2
if (q == "" and a1 == ""):
    q = 2
    a1 = 1

print("Wyraz nr", n, "ciągu geometrycznego o q =", q, "i a1 =", a1, "jest równy:")
print(ciag_geometryczny(int(a1),int(q),n))