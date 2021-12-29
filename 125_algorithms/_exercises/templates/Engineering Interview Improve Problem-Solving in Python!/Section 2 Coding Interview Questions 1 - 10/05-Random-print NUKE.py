#n = 100
# 
_______ random
___ print_random_del(l):
    ___ i __ r..(l..(l),0,-1):
        index_to_delete  random.randint(0, i - 1)
        print(l[index_to_delete], index_to_delete)
        del l[index_to_delete]
        
___ print_random(l):
    ___ i __ r..(l..(l),0,-1):
        index_to_delete  random.randint(0, i - 1)
        print(l[index_to_delete], index_to_delete)
        l[index_to_delete]  l[i - 1]

print_random([1, 2, 7, 4,5, 6, 3])