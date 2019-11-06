import numpy as np

print("podaj kąt")
kat = float(input())

def przelicznik_na_rad(a):
    return a*np.pi/180.
def przelicznik_na_deg(b):
    return b*180./np.pi

print("Chcesz przeliczyć podany kąt na radiany czy stopnie? (rad/deg)")
tak = str(input())

if tak=="rad":
    print("podany kąt w radianach =", przelicznik_na_rad(kat))
elif tak=="deg":
    print("podany kąt w stopniach =", przelicznik_na_deg(kat))
else:
    print("Try again")