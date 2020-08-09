num_ele, ele_type = [int(i) ___ i in input().split()]


ele = []
unique = []

w___ le.(ele) < ele_type:
    num_count = [int(x) ___ x in input().split()]
    num_count.sort()
    #finding out unique elements in the list
    ___ x in num_count:
        __ x not in unique:
            unique.append(x)
            
    #counting the occurence of the element in the list
    ___ i in range(le.(unique)):
        count_store = num_count.count(unique[i])
        ele.append(count_store)
        
        
___ k in ele:
    print(k,end=(' '))