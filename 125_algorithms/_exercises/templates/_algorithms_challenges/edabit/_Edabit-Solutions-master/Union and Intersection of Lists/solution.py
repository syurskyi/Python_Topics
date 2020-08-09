___ intersection_union(lst1, lst2
    inter = []
    uni = []
    output = [inter, uni]
    ___ i in lst1:
        __ i in lst2:
            inter.append(i)
    ___ x in inter:
        __ inter.count(x) > 1:
            inter.remove(x)
    ___ z in lst1:
        __ z in uni:
            continue
        uni.append(z)
    ___ c in lst2:
        __ c not in uni:
             uni.append(c)
    inter.sort()
    uni.sort()
    r_ output
