#zmniejszenie stopnia zagnieżdżenia listy: chain

import itertools as it

lista = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
listapodzielona = list(it.chain(*lista))
print("Mniej zagnieżdżona lista:")
print(listapodzielona)