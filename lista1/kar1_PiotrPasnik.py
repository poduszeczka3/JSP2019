import numpy as np

#Zadanie 1
a=int(input())
b=int(input())
r=a%b
print(r)

#Zadanie 2
d=float(input())
e=float(input())
f=float(input())
alfa=(np.arccos((d**2+e**2-f**2)/(2*d*e))*180./np.pi)
print(round(alfa,3),"stopni")