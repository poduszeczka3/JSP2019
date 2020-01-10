import numpy as np

r = float(input("Wpisz promień koła: "))

class Koło:
  def __init__(nazwa, obwod, pole):
    nazwa.pole = np.pi*r**2
    nazwa.obwod = 2*np.pi*r
p = Koło("nazwa", r)

print("Pole koła o promieniu r =", r, "wynosi:", p.pole)
print("Obwód koła o promieniu r =", r, "wynosi:", p.obwod)