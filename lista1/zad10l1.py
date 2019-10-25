import cmath as cm
import numpy as np

print("Wpisz część rzeczywistą, a następnie po wciśnięciu 'enter' urojoną liczby zespolonej")
x = int(input())
y = int(input())
z = complex(x,y)
sinz = np.sin(z)
cosz = np.cos(z)

print("Część rzeczywista sin(z): ", sinz.real) 
print("Część urojona sin(z): ", sinz.imag) 
print("Część rzeczywista cos(z): ", cosz.real) 
print("Część urojona cos(z): ", cosz.imag) 
print("sin^2(z) + cos^2(z) =", sinz**2+cosz**2)