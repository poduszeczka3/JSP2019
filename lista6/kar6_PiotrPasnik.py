a = {'a':1, 'b':3, 'c':3, 'd':10, 'e':10}

def słownik(s):
    s2 = {}
    for x in s:
        if s[x] not in s2.values(): s2[x] = s[x]
    return s2

print(słownik(a))