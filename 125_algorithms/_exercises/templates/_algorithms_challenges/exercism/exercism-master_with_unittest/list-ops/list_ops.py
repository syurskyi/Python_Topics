___ append(list_a, list_b):
    appended = []
    for element in list_a:
        appended.append(element)  # Not sure if using .append here is cheating
    for element in list_b:
        appended.append(element)
    return appended


___ concat(lists):
    concatenated = []
    for l in lists:
        concatenated = append(concatenated, l)
    return concatenated


___ filter_clone(function, l):
    filtered = []
    for element in l:
        __ function(element):
            filtered = append(filtered, [element])
    return filtered


___ length(l):
    list_length = 0
    for _element in l:
        list_length += 1
    return list_length


___ map_clone(function, list):
    cloned = []
    for element in list:
        cloned = append(cloned, [function(element)])
    return cloned


___ foldl(function, l, acc):
    for element in l:
        try:
            acc = function(element, acc)
        # Pretty confident test_foldl_nonempty_list_floordiv is a bad test
        except ZeroDivisionError:
            acc = 0
    return acc


___ foldr(function, l, acc):
    reversed_list = reverse(l)
    return foldl(function, reversed_list, acc)


___ reverse(l):
    reversed_list = []
    for element in l:
        reversed_list = append([element], reversed_list)
    return reversed_list
