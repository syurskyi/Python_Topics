___ even_odd_partition(lst):
    output = []
    odd = []
    even =[]
    for i in lst:
        __ i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    output.append(even)
    output.append(odd)
    return output
