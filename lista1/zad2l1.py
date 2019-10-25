import numpy as np
a=3.
b=4.
st=47.
alfa=st*np.pi/180.
P=a*b*np.sin(alfa)
print("Pole trójkąta o bokach",a,"i",b,",pomiędzy którymi jest kąt o mierze",st,"stopni wynosi:",round(P,2))