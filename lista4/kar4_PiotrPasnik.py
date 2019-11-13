#lista_1=[20,11,[5,-8],[1,-20],5,[-19,-8],-10,[7,-19],-15,[6,-12],[-17,9],2]

def Sort(sub_li):
    sub_li1.sort(key = lambda x: abs(x))
    sub_li2.sort(key = lambda x: abs(x[0]))
    return sub_li1,sub_li2

sub_li1 = [20,11,5,-10,-15,2]
sub_li2 = [[5,-8], [1,-20], [-19,-8], [7,-19],[6,-12],[-17,9]]
lista_1=[sub_li1,sub_li2]

print(Sort(lista_1))