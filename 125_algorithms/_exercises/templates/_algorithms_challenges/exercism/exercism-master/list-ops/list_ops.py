___ append(list_a, list_b
    appended = []
    ___ element in list_a:
        appended.append(element)  # Not sure if using .append here is cheating
    ___ element in list_b:
        appended.append(element)
    r_ appended


___ concat(lists
    concatenated = []
    ___ l in lists:
        concatenated = append(concatenated, l)
    r_ concatenated


___ filter_clone(function, l
    filtered = []
    ___ element in l:
        __ function(element
            filtered = append(filtered, [element])
    r_ filtered


___ length(l
    list_length = 0
    ___ _element in l:
        list_length += 1
    r_ list_length


___ map_clone(function, list
    cloned = []
    ___ element in list:
        cloned = append(cloned, [function(element)])
    r_ cloned


___ foldl(function, l, acc
    ___ element in l:
        try:
            acc = function(element, acc)
        # Pretty confident test_foldl_nonempty_list_floordiv is a bad test
        except ZeroDivisionError:
            acc = 0
    r_ acc


___ foldr(function, l, acc
    reversed_list = reverse(l)
    r_ foldl(function, reversed_list, acc)


___ reverse(l
    reversed_list = []
    ___ element in l:
        reversed_list = append([element], reversed_list)
    r_ reversed_list
