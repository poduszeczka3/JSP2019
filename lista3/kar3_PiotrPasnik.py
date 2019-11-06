#Zadanie 1

L=[0,10,8,3,5,4,7]
n=len(L)
for i in range(n):
    if L[i]%2==1:
        print(L[i])
print()

#Zadanie 2

n=5
for i in range(1,n+1): print(str("*")*i)
for i in range(n-1,0,-1): print(str("*")*i)