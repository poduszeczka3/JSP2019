print("Wpisz n")
n = int(input())

silnia = 1

for i in range(1,n+1): 
    silnia*=i

if n>=0:
    print (str(n)+"! = ",end="") 
    print (silnia)
else:
    print("Zła wartość n")