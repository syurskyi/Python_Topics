amount_values = i..(input())
results    # list

___ rotate(index, string):
    sub_string1 = string[:index]
    sub_string2 = string[index:]

    rotated_string = sub_string2+sub_string1
    r.. rotated_string

___ i __ r..(amount_values):
    index, string = map(s.., input().s..())
    index = i..(index)
    results.a..(rotate(index, string))

print(*results)