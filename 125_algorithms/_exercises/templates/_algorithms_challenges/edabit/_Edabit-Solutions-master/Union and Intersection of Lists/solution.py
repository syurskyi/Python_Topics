___ intersection_union(lst1, lst2
    inter =   # list
    uni =   # list
    output = [inter, uni]
    ___ i __ lst1:
        __ i __ lst2:
            inter.append(i)
    ___ x __ inter:
        __ inter.count(x) > 1:
            inter.remove(x)
    ___ z __ lst1:
        __ z __ uni:
            continue
        uni.append(z)
    ___ c __ lst2:
        __ c not __ uni:
             uni.append(c)
    inter.sort()
    uni.sort()
    r_ output
