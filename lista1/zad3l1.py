import numpy as np
print("Podaj długość pierwszego boku trójkąta")
a=float(input())
print("Podaj długość drugiego boku")
b=float(input())
print("Podaj kąt pomiędzy bokami")
st=float(input())
P=a*b*np.sin(st*np.pi/180.)
print("Pole trójkąta o bokach",a,"i",b,",pomiędzy którymi jest kąt o mierze",st,"stopni wynosi:",round(P,2))