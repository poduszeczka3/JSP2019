print("Wpisz liczbe naturalną od 0 do 59")
liczba = int(input())

def slownie(num):
    d = { 0: 'zero', 1: 'jeden', 2: 'dwa', 3: 'trzy', 4: 'cztery', 5: 'pięć', 
          6: 'sześć', 7: 'siedem', 8: 'osiem', 9: 'dziewięć', 10: 'dziesięć',
          11: 'jedenaście', 12: 'dwanaście', 13: 'trzynaście', 14: 'czternaście',
          15: 'piętnaście', 16: 'szesnaście', 17: 'siedemnaście',
          18: 'osiemnaście', 19 : 'dziewiętnaście', 20 : 'dwadzieścia',
          30 : 'trzydzieści', 40 : 'czterdzieści', 50 : 'pięćdziesiąt'}
    k = 1000
    assert(0 <= num)
    if (num < 20): return d[num]
    if (num > 20):
        if num % 10 == 0: return d[num]
        else: return d[num // 10 * 10] + ' ' + d[num % 10]
    raise AssertionError('num is too large:', str(num))

print("Słownie", slownie(liczba))