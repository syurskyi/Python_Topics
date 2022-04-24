amount_value i..(input

generator_list    # list
results    # list

___ generate(num, counter
    
    __(num __ generator_list
        r.. counter
    generator_list.a..(num)
    num **= 2
    num (num//100)%10000
    r.. generate(num, counter+1)

values l.. m..(i.., i.. ).s..()))

___ i __ r..(amount_value
    results.a..(generate(values[i],0
    generator_list.clear()

print(*results)