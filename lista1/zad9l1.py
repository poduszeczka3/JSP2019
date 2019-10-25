import cmath as cm

print("podaj liczbę z")
z = complex(input())
print("z =", z)

mod_z = abs(z)
print("|z| =",mod_z)
arg_z = cm.phase(z)
print("argument z =", arg_z)
sprz_z = z.conjugate()
print("sprzężenie z =", sprz_z)
