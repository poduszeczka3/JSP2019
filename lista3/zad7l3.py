print("Wpisz liczbę wyrazów ciągu Fibonacciego, które chcesz zobaczyć")
n = int(input())
print()

def Fibonacci(n): 
    if n==1: return 1
    elif n==2: return 1
    else: return Fibonacci(n-1)+Fibonacci(n-2) 

for i in range(1,n+1):
    print(Fibonacci(i))