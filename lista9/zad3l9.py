import numpy as np

v0=float(input("Wpisz prędkość początkową: "))
deg=float(input("Wpisz miarę kąta rzutu: "))
rad=deg*np.pi/180
g=10

h=v0**2*np.sin(rad)**2/(2*g)
z=v0**2*np.sin(2*rad)/g
t=2*v0*np.sin(rad)/g

print()
print("Maksymalna wysokość: ",round(h,3),"m")
print("Zasięg rzutu wynosi: ",round(z,3),"m")
print("Czas trwania lotu to:",round(t,3),"s")