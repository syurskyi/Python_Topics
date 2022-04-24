amount_values i..(input
results    # list

___ get_seq(Xnext, counter=0
    __(Xnext __ 1
        r.. counter
    ____
        __(Xnext % 2 __ 0
            r.. get_seq(Xnext/2, counter+1)
        ____
            r.. get_seq(3*Xnext+1, counter+1)

XList l.. m..(i.., i.. ).s..()))
___ i __ XList:
    seq get_seq(i)
    results.a..(seq)

print(*results)