l1 = [1, 2, 3] 

class podlist: 
    def funk_pl(list1): 
        sublist = [[]]  
        for i in range(len(list1)+1): 
            for j in range(i+1, len(list1)+1):  
                sub = list1[i:j] 
                sublist.append(sub) 
        return sublist

print(podlist.funk_pl(l1))