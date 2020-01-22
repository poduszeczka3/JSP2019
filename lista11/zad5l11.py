import re 

text = 'LHA120 N-11: mgławica emisyjna, znajdująca się w gwiazdozbiorze ZłotejRyby. Należy do WielkiegoObłokuMagellana. Wchodzi w skład dużego rejonu gwiazdotwórczego LMC-N11 (N11).'
spacje = re.sub(r"(\w)([A-Z])", r"\1 \2", text)
print(spacje)