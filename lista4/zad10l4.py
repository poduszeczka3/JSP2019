print("podaj a")
a = int(input())

print("podaj b")
b = int(input())

def dzielnik(a,b): 
    if(b==0): 
        return a 
    else:
        return dzielnik(b,a%b) 
 
print("NWD liczb",a,"i",b,"wynosi",dzielnik(a,b)) 