L=[0,10,8,3,5,4,7]
n=len(L)
s=L[0]
il=L[0]
for i in range(n-1):
    s+=L[i+1]
    il*=L[i+1]
print(s,il)