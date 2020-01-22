import re 

text = 'Lha120 N-11: mgławica emisyjna, znajdująca się w gwiazdozbiorze Złotej Ryby. Należy do Wielkiego Obłoku Magellana. Wchodzi w skład dużego rejonu gwiazdotwórczego LMC-N11 (N11).'
lista = re.findall(r'\b[ae]\w+\b',text)
print("Słowa rozpoczynające się na 'a' lub 'e' to:",lista)