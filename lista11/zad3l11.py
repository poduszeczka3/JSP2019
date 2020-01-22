import re 

text = 'Lha 120 n-11: mgławica emisyjna, znajdująca się w gwiazdozbiorze Złotej Ryby. Należy do Wielkiego Obłoku Magellana. https://en.wikipedia.org/wiki/NGC_1763  Wchodzi w skład dużego rejonu gwiazdotwórczego LMC-N11 (N11).'
url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)

print("Adresy URL:",url)