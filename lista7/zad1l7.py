# Wersja z pętlą for

n = int(input("Ile wyrazów ciągu Fibonacciego chcesz zobaczyć? "))
print()

n1, n2 = 0, 1
if n < 0:
   print("Spadaj śmieciu!")
elif n==0: print(n1)
elif n==1: print(n2)
else:
   for i in range(1,n+1):
        nth = n1 + n2
        n1 = n2
        n2 = nth
        print(n1)
        i += 1

# Wersja rekurencyjna

print()
def Fibonacci(n): 
    if n==0: return 0
    elif n==1: return 1
    elif n==2: return 1
    else: return Fibonacci(n-1)+Fibonacci(n-2) 

if n>0:
    for i in range(1,n+1):
        print(Fibonacci(i))
elif n==0: print(n1)